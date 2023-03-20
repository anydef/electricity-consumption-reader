import uasyncio as asyncio
from machine import UART, Pin
from utime import sleep
from test import random_message
from ubinascii import unhexlify
from sml_parser_light import SmlStreamReader, sml_get_entry, OBIS_NAMES
uart_test = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)

init = uart_test.init()


uart_wire = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5), bits=8,  parity=None, stop=1)
uart_wire.init()

async def test_sender():
    swriter = asyncio.StreamWriter(uart_test, {})
    while True:
        await swriter.awrite(random_message())
        await asyncio.sleep(1)

async def receiver():
    sreader = asyncio.StreamReader(uart_wire)

    obis = [
        "0100010800ff",
        "0100020800ff",
        "0100100700ff",
        "0100240700ff",
        "0100380700ff",
        "0100480700ff",
        "010048ffffff", # not part of sample message
    ]

    obis = OBIS_NAMES.keys()

    sml_stream_reader = SmlStreamReader()

    while True:
        byte_array = await sreader.readline()

        for read_pos in range(0, len(byte_array), 10):
            # add bytes to reader, this sould be the output form the UART
            sml_stream_reader.add(byte_array[read_pos:read_pos+10])
            sml_frame = sml_stream_reader.get_frame()

            # full frame was read and parsing can start
            if sml_frame is not None:

                # now extract the entries
                for o in OBIS_NAMES:
                    entry = sml_get_entry(sml_frame, obis=unhexlify(o))

                    # entry was found
                    if entry != None:
                        print("{}".format(entry))
                        print("-> {}[{}]".format(entry.sensor_value(), entry.sensor_unit()))
                    else:
                        print("ERROR: {} not found".format(o))
            else:
                pass
                # print("Frame was empty")


print("Registering tasks.")
loop = asyncio.get_event_loop()

# loop.create_task(test_sender())

loop.create_task(receiver())
loop.run_forever()

# print('UART1:', uart_wire)
# print()

# def rx_handler():
#     received = uart_wire.read()
#     print("Received: ", received)
#     pass
# uart_wire.irq(UART.RX_ANY, handler=rx_handler, wake=machine.IDLE)

# while True:
#     sleep(1)
#     txData = 'Transmitting data'
#     uartTest.write(txData)
# # #     sleep(1)

# # #     # Daten empfangen und ausgeben
# # #     rxData = uartIn.readline()
# # #     print('Data received:', rxData.decode('utf-8'))
 
# # while True:
# #     sleep(1)
# #     txData = 'Transmitting Data'
# #     uart.readline()