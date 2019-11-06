import asyncio


async def tcp_echo_client(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    message = input('Enter message for server: ')

    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(data, 'returned from server')
    writer.close()
    await writer.wait_closed()


HOST = 'localhost'
PORT = 5555

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = loop.create_task(tcp_echo_client(HOST, PORT))
    loop.run_until_complete(task)
