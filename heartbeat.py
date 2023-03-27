import uasyncio as asyncio


from machine import Pin


async def heartbeat():
    onboard_led = Pin("LED", Pin.OUT)
    onboard_led.off()
    while True:
        onboard_led.on()
        await asyncio.sleep(0.25)
        onboard_led.off()
        await asyncio.sleep(5)