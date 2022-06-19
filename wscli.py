import asyncio
import websockets
import json

async def main():
    async with websockets.connect("ws://127.0.0.1:8000/ws/notifications/") as websocket:
        while True:
            recieve = await websocket.recv()
            recieve = json.loads(recieve)
            try:            
                if recieve['message'] == 'ping':
                    send ={'id': recieve['id'], 'message': 'pong'}
                    await websocket.send(json.dumps(send))
            except KeyError:
                print('recieved: ' + str(recieve))
                continue
            
                

asyncio.run(main())