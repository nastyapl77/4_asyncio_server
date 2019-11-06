import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    print(message, 'gotten from client')

    writer.write(data)
    await writer.drain()

    writer.close()


async def main(HOST, PORT):
    coroutine = asyncio.start_server(handle_echo, HOST, PORT)
    asyncio.ensure_future(coroutine, loop=loop)


HOST = 'localhost'
PORT = 5555

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = loop.create_task(main(HOST, PORT))
    loop.run_forever()
