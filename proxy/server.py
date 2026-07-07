import socket as sk
from Proxy import ProxyServer
import threading as thread

HOST = "127.0.0.1"
PORT = 2002
ENCODING="utf-8"
DECODING="utf-8"
BUFFER_LENGTH = 1024
class Server:
     def __init__(self):
          self.socketServer = sk.create_server((HOST, PORT), family=sk.AF_INET)
          

     def run(self):
          self.socketServer.listen()
          print("Server Is Running ....")
          while True:
               (clientSocket , clientAddr )=self.socketServer.accept()
               data = self.receive(clientSocket)

     def receive(self , clientSocket):
          data = clientSocket.recv(BUFFER_LENGTH)
          ReqInfo = {
               "srcReq" : data,
               "srcIp" : clientAddr[0],
               "dstIp" : HOST,
               "dstPort" : PORT,
               "packetLength" : len(data),
          }
          data = data.decode(DECODING)
          return ReqInfo

     def Response(self , clientSocket , data):
          clientSocket.sendall(data.encode(ENCODING))

     
          

     def close(self):
          self.socketServer.close()


     
     
