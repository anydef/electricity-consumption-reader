import uasyncio as asyncio
from machine import UART, Pin
from utime import sleep
from test import random_message
from ubinascii import unhexlify
from sml_parser_light import SmlStreamReader, sml_get_entry, OBIS_NAMES


uart_wire = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5), bits=8,  parity=None, stop=1)
uart_wire.init()

async def receiver():
    sreader = asyncio.StreamReader(uart_wire)


    while True:
        byte_array = await sreader.readline()
        print(byte_array)


print("Registering tasks.")
loop = asyncio.get_event_loop()

# loop.create_task(test_sender())

loop.create_task(receiver())
loop.run_forever()
