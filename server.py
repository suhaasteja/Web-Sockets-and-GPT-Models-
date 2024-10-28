# server.py
import asyncio
from random import randint
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        # Modify incoming message with a random number
        modified_message = f"[{randint(1, 10)}] {message}"
        await websocket.send(modified_message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # Run server indefinitely

# Run the WebSocket server
if __name__ == "__main__":
    asyncio.run(main())
