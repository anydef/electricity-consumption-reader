
import uasyncio as asyncio

from uasyncio import Event
from sml_parser_light import SmlStreamReader
from sml_parser_light import sml_get_entry
from sml_parser_light import OBIS_NAMES
from ubinascii import unhexlify


class Meter(object):
    def __init__(self, name, display_name, unit, obi_key):
        self.__unit = unit
        self.__name = name
        self.__display_name = display_name
        self.__value = 0.0
        self.__obi_key = obi_key
        self.mutex = asyncio.Lock()
    
    @property
    def obi_key(self):
        return self.__obi_key
    
    @property
    def display_name(self):
        return self.__display_name

    @property
    def value(self):
        return self.__value

    @property
    def unit(self):
        return self.__unit
 
    @property
    def name(self):
        return self.__name
    
    def __str__(self) -> str:
        return f"{self.__name}: {self.__value} {self.__unit}"   
    
    async def set(self, val):
        await self.mutex.acquire()
        self.__value = val
        self.mutex.release()


async def receiver(uart, meters:dict[str, Meter], event:Event):
    sreader = asyncio.StreamReader(uart)
    obis = OBIS_NAMES.keys()

    sml_stream_reader = SmlStreamReader()

    while True:
        print("Wait for line.")
        byte_array = await sreader.readline()
        print("Received line.")
        for read_pos in range(0, len(byte_array), 10):
            # add bytes to reader, this sould be the output form the UART
            sml_stream_reader.add(byte_array[read_pos:read_pos+10])
            sml_frame = sml_stream_reader.get_frame()

            # full frame was read and parsing can start
            if sml_frame is not None:
                # now extract the entries
                for o in obis:
                    entry = sml_get_entry(sml_frame, obis=unhexlify(o))

                    # entry was found
                    if entry != None:
                        meter = meters.get(entry.obis, None)
                        if not meter:
                            continue
                        try:
                            print("Updateing meter reading", entry)
                            print("Sensor value", entry.sensor_value())
                            await meter.set(entry.sensor_value())
                        except RuntimeError as e:
                            print("Failed processing message value", e)
                event.set()
                
