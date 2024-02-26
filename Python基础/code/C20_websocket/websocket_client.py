import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        recvs = await websocket.recv()
        print(recvs)
        while True:
            msg = input("Say:")
            if msg == "quit" or msg == "exit":
                print("Exit websocket")
                break
            await websocket.send(msg)
            recvs = await websocket.recv()
            print(recvs)

asyncio.run(hello())
