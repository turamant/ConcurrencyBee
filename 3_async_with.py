import asyncio


async def get_conn(host, port):
    class Conn:
        async def put_data(self):
            print('send data')
            await asyncio.sleep(2)
            print('sand data')

        async def get_date(self):
            print('get data')
            await asyncio.sleep(2)
            print('got data')

        async def close(self):
            print('connection close')
            await asyncio.sleep(2)
            print('connection closed')

    print('connection settings')
    await asyncio.sleep(2)
    print('connection close')
    return Conn()


class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return self.conn
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()

async def main():
    async with Connection('localhost', 9001) as conn:
        send_task = asyncio.create_task(conn.put_data())
        receive_task = asyncio.create_task(conn.get_date())

        await send_task
        await receive_task


if __name__ == '__main__':
    asyncio.run(main())
