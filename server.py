import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    print(message, 'gotten from client')

    writer.write(data)
    print(f'{data} sent back to client')
    await writer.drain()

    writer.close()
    print(f'Connection finished')


HOST = 'localhost'
PORT = 5555

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    server_task = asyncio.start_server(handle_echo, HOST, PORT)
    loop.run_until_complete(server_task)

    print(f'Server based on {HOST}:{PORT}')
    loop.run_forever()
