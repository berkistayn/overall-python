import socketserver
# from AliceBuilder import AliceBuilder
from AliceBuilder_Scanner import AliceBuilder_Scanner as AliceBuilder

# NOTE: Add error handling + input check

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        commands = self.data.decode("utf-8").split(" ")
        called_method = getattr(AB, commands[0])
        if len(commands) > 1:
            response = called_method(*commands[1:])
        else:
            response = called_method()
        
        if response:
            print("Server side, response:", response)
            self.request.sendall(str(response).encode())
        else:
            print("Server side, nothing to respond.")

if __name__ == "__main__":
    AB = AliceBuilder()
    
    HOST, PORT = "172.24.21.180", 100

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

