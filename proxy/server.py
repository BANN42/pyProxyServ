import socket as sk

# V1 request description
class Req:
     def __init__(self, srcIp ,dstIp, header):
          self.srcIp = srcIp
          self.dstIp = dstIp
          self.header = header

class Server_R:
     def __init__(self ,host, reqSrc , reqDst):
          self.host = host
          self.reqSrc =reqSrc
          self.reqDst = reqDst

     # establish connection to the server
     def establishConnection(self):pass
     # receive request
     def receiveRequest(self):pass
     # redirect Request
     def redirectReq(self, ClientReq ):pass
     # filter Request
     def filterReq(self,clientReq) :pass
     # prevent Request
     def preventReq(self, clientReq): pass
     # analyzer Request
     def analyzerReq(self , clientReq) : pass
     
