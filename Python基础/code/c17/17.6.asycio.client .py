# -*- coding:utf-8 -*-
import asyncio

@asyncio.coroutine
def simple_client():
    # Open a connection and write a few lines by using the StreamWriter object
    reader, writer = yield from asyncio.open_connection('localhost', 2222)
    # reader is a StreamReader object
    # writer is a StreamWriter object
    while True:
        datas = input("Enter your input(over is end): ")
        size = len(datas.encode())
        writer.write((datas).encode()) #+'\n'
        msgbs = yield from reader.read(size)#readline()
        msg= msgbs.decode() #"utf8","ignore"
        print(msg)
        if msg == 'over':
            writer.close()
            break 
loop = asyncio.get_event_loop()
loop.run_until_complete(simple_client())

