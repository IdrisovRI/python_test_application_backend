import json
import asyncio
import websockets


async def test():
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as ws:
        # Part 1 TEST
        message = str(json.dumps({"action": "assets", "message": {}}))
        print('MESSAGE1:{}'.format(message))
        await ws.send(message)

        # Part 2 TEST
        message = str(json.dumps({"action": "subscribe", "message": {"assetId": 1}}))
        print('MESSAGE2:{}'.format(message))
        await ws.send(message)
        while True:
            data = await ws.recv()
            print(data)

asyncio.get_event_loop().run_until_complete(test())
