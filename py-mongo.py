# from http import server
# import pymongo;
import requests
import threading
import json
from email.message import Message
from http.server  import HTTPServer,BaseHTTPRequestHandler 
# _db_lock=threading.Lock()
# print("Hello Anvayaa")

class message(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write('hello boss'.encode())
        self.wfile.write(result .encode())


data = requests.get('https://jsonplaceholder.typicode.com/users')
result=json.dumps(data.json())



posts= requests.get('https://jsonplaceholder.typicode.com/posts')
postresult=json.dumps(posts.json())



comments= requests.get('https://jsonplaceholder.typicode.com/comments')
commentresult=json.dumps(comments.json())


album= requests.get('https://jsonplaceholder.typicode.com/albums')
albumresult=json.dumps(album.json())


photos= requests.get('https://jsonplaceholder.typicode.com/photos')
photosresult=json.dumps(photos.json())



todo= requests.get('https://jsonplaceholder.typicode.com/todos')
todosresult=json.dumps(todo.json())



def printit():
  threading.Timer(1.0, printit).start()
  print(":::::::::::::::::::::::::::::::::::::::todos:::::::::::::::::::::/n")
  print(todosresult)
  print(":::::::::::::::::::::::::::::::::::::::photos:::::::::::::::::::::/n")
  print(photosresult)
  print(":::::::::::::::::::::::::::::::::::::::albums:::::::::::::::::::::/n")
  print(albumresult)
  print(":::::::::::::::::::::::::::::::::::::::comments:::::::::::::::::::::/n")
  print(commentresult)
  print(":::::::::::::::::::::::::::::::::::::::posts:::::::::::::::::::::/n")
  print(postresult)
  print(":::::::::::::::::::::::::::::::::::::::users :::::::::::::::::::::/n")
  print(result)
  print("hello from here")

printit()
PORT=2222
server=HTTPServer(('',PORT),message)
print("Server Listening On Port %s" %PORT)
server.serve_forever()