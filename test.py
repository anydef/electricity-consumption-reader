from random import randrange
from ubinascii import unhexlify
from machine import UART, Pin
from sml_parser_light import SmlStreamReader, sml_get_entry
import uasyncio as asyncio
from sml_parser_light import SmlStreamReader, sml_get_entry, OBIS_NAMES
from samples import samples
import config

cfg = config.read_config()


uart_test = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)


sml_stream_reader = SmlStreamReader()

def test_parser(line):
    byte_array = line
    for read_pos in range(0, len(byte_array), 10):
        # add bytes to reader, this sould be the output form the UART
        sml_stream_reader.add(byte_array[read_pos:read_pos+10])
        sml_frame = sml_stream_reader.get_frame()

        # full frame was read and parsing can start
        if sml_frame is not None:
            # now extract the entries
            for o in OBIS_NAMES.keys():
                print("OBI", o)
                entry = sml_get_entry(sml_frame, obis=unhexlify(o))

                # entry was found
                if entry != None:
                    print("{}".format(entry))
                    print("-> {}[{}]".format(entry.sensor_value(), entry.sensor_unit()))
                else:
                    print("No record found")


async def emit_samples():
    if not cfg.get('test', False):
        print('Skip test')
        return
   
    print('Start test')

    swriter = asyncio.StreamWriter(uart_test, {})

    while True:
        print('Run test.')

        for line in samples:
            # test_parser(line)
            # asyncio.sleep(1)
            await swriter.awrite(line)
            await asyncio.sleep(3)
        await asyncio.sleep(5)
