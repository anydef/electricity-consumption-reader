import pico_time
from uart_receiver import Meter


async def write_response(writer, status, response, content_type):
    if not content_type:
        content_type = "text/html"
    writer.write(
        f'HTTP/1.1 {status} OK\r\nContent-type: {content_type}\r\n\r\n')
    writer.write(response)
    await writer.drain()
    await writer.wait_closed()


def create_server(meters: dict[str,Meter]):
    try:

        async def root_handler(**kwargs):
            return (200, f"""serving. system time: {pico_time.local_time()}""", None)

        async def metrics(**kwargs):
            res = [f"{meter.name} {{unit='{meter.unit}'}} {meter.value}" for meter in list(meters.values())]
            print(res)
            return (200, "\r\n".join(res), None)

        async def not_found(**kwargs):
            return (404, "Requested resource not found", None)

        handlers = {
            'GET': {
                '/': root_handler,
                '/metrics': metrics,
            },
        }

        async def serve_client(reader, writer):
            try:
                request_line = await reader.readline()
                print(f"Request {request_line}")

                lines = request_line

                while lines != b"\r\n":
                    lines = await reader.readline()

                request = request_line.decode("utf-8")
                method, uri, protocol = request.split(" ")

                body = await reader.read(1024) if method == 'POST' else b''

                query_params = uri.split("?")
                path = query_params[0]
                query = query_params[1] if len(query_params) > 1 else ''
                handler = handlers.get(method, {}).get(path, not_found)
                # type: ignore
                status, response, content_type = await handler(path=path, query=query, method=method, protocol=protocol,
                                                               uri=uri, body=body)
                # type: ignore
                # type: ignore
                await write_response(writer, status, response, content_type)
            except Exception as e:
                print(e)
            finally:
                await writer.drain()
                await writer.wait_closed()

        print("Webserver initialized.")
        return serve_client
    except Exception as e:
        print(e)
