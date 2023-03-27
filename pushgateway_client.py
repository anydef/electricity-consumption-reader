import socket
from uart_receiver import Meter
import uasyncio as asyncio
import config
from uasyncio import Event

cfg = config.read_config()
host = cfg['pushgateway_host']
port = int(cfg['pushgateway_port'])
job = "gas-meter"
instance = cfg['instance']


async def send_readings(event:Event, meters: dict[str, Meter]):
    while True:
        await event.wait()
        try:
            for _, meter in meters.items():
                send_reading(meter)
        except RuntimeError as e:
            print("Failed sending data to pushgateway", e)
        finally:
            event.clear()


def send_reading(meter: Meter):
    """All whitespaces and linebreaks are according to HTTP/1.1 specification. Must be preserved."""
    data = """#TYPE {metric_name} {metric_type}
{metric_name} {value}\n""".format(metric_name=meter.name, 
                                  metric_type='GAUGE', 
                                  value=meter.value, 
                                  )
    request = """POST /metrics/job/{job}/instance/{instance} HTTP/1.1
Host: {host}:{port}
User-Agent: raspberry-pico
Accept: */*
Content-Type: application/x-www-form-urlencoded
Content-Length: {content_length}

""".format(
        content_length=str(len(data)),
        job=job,
        instance=instance,
        host=host,
        port=port
    )
    send(request, data)


def send(request, data):
    print("Sending reading", data)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockaddr = socket.getaddrinfo(host, port)[0][-1]
    try:
        sock.connect(sockaddr)
        sock.send(request.encode("utf-8"))
        sock.send(data.encode("utf-8"))
        res = sock.recv(512)
        print(res)
    except Exception as ex:
        print(ex)
    finally:
        sock.close()

