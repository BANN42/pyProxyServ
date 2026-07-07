class Utils:
     
     @staticmethod
     def parse_http_request(request):
         lines = request.split("\r\n")
         request_line = lines[0]
         HttpMethod, path, HttpVersion = request_line.split(" ")
         headers = {}
         for line in lines[1:]:
             if line == "":
                 break
             key, value = line.split(": ", 1)
             headers[key] = value
         return {
             "HttpMethod": method,
             "path": path,
             "HttpVersion": HttpVersion,
             "headers": headers
         }

      # receive all
      
      def receive_all(client_socket):
          buffer = b""
          while True:
              data = client_socket.recv(4096)
              if not data:
                  break
              buffer += data
          return buffer
      # send all
      def send_all(client_socket, data):
               total_sent = 0
          while total_sent < len(data):
              sent = client_socket.send(data[total_sent:])
              if sent == 0:
                  raise RuntimeError("Socket connection broken")
              total_sent += sent
              
