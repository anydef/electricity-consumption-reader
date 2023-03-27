import uasyncio as asyncio
from sml_parser_light import SmlStreamReader, sml_get_entry, OBIS_NAMES
from ubinascii import unhexlify


async def receiver(uart_wire):
    sreader = asyncio.StreamReader(uart_wire)
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
                for o in obis:
                    entry = sml_get_entry(sml_frame, obis=unhexlify(o))

                    # entry was found
                    if entry != None:
                        print("{}".format(entry))
                        print("-> {}[{}]".format(entry.sensor_value(), entry.sensor_unit()))
