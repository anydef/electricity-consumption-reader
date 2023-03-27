import uasyncio as asyncio
import boot

from uasyncio import Event
from heartbeat import heartbeat
from machine import UART, Pin
from test import emit_samples
from uart_receiver import Meter, receiver
from pushgateway_client import send_readings
import webserver_async as webserver

uart_connection = UART(1, baudrate=9600,
                       tx=Pin(4),
                       rx=Pin(5),
                       bits=8,
                       parity=None,
                       stop=1)
uart_connection.init()

message_event = Event()
meters: dict[str, Meter] = {
    '0100010800ff': Meter(name="electricity_reading_total",
                          display_name="Reading Total",
                          unit='Wh',
                          obi_key='0100010800ff',
                          ),
    '01000f0700ff': Meter(name="electricity_reading_effective",
                          display_name="Reading Effective",
                          unit='Wh',
                          obi_key='01000f0700ff',
                          )
}


async def main():
    boot.init()

    asyncio.create_task(asyncio.start_server(
        webserver.create_server(meters=meters), "0.0.0.0", 80
    ))
    asyncio.create_task(receiver(uart=uart_connection, meters=meters, event=message_event))
    asyncio.create_task(send_readings(event=message_event, meters=meters))
    asyncio.create_task(emit_samples())
    await heartbeat()

try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()
