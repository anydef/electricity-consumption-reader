import uasyncio as asyncio
from machine import UART, Pin
from utime import sleep


uart_test = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)

init = uart_test.init()


uart_wire = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5), bits=8,  parity=None, stop=1)
uart_wire.init()

async def test_sender():
    swriter = asyncio.StreamWriter(uart_test, {})
    while True:
        await swriter.awrite('Hello uart\n')
        await asyncio.sleep(2)

async def receiver():
    sreader = asyncio.StreamReader(uart_wire)
    while True:
        res = await sreader.readline()
        print('Recieved', res)

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