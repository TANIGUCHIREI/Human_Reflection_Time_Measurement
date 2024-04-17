import asyncio
import time
async def  main1():
    while True:

        await asyncio.sleep(1)
        print("HELLO!")

async def main2():
    while True:
        await asyncio.sleep(2)
        print("main2だよ")

async def m_main():
    await asyncio.wait([main1(),main2()])
loop = asyncio.get_event_loop()
loop.run_until_complete(m_main())
loop.close()
