# -*- coding:utf-8 -*-
import asyncio
import sys
@asyncio.coroutine
def client_handler(client_reader, client_writer):
    # Runs for each client connected
    # client_reader is a StreamReader object
    # client_writer is a StreamWriter object
    print("Connection received!")
    while True: 
        msgbs = yield from client_reader.read(20)
        msg= msgbs.decode()
        print(msg)
        client_writer.write (msg.encode() )
        client_writer.drain()
        if msg == 'over':
            client_writer.close()
            break
	
if __name__ == '__main__':
  if sys.platform == 'win32':
      pass
  else: #for Linux
      import uvloop
      asyncio.set_event_loop_policy(uvloop.EventLoopPolicy()) 
  loop = asyncio.get_event_loop()
  coro = asyncio.start_server(client_handler, 'localhost', 2222, loop=loop) 
  server = loop.run_until_complete(coro) 
  for socket in server.sockets:
      print("Serving on {}. Hit CTRL-C to stop.".format(socket.getsockname()))  
  try:
      loop.run_forever()
  finally:
      loop.close()



