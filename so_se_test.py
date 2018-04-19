from SocketServer import BaseRequestHandler,ThreadingTCPServer
import threading

class Handler(BaseRequestHandler):
    def handle(self):
        address,pid = self.client_address
        print 'connected', address
        while True:
            data = self.request.recv(1024)
            if len(data) > 0:
                print 'receive ', data
                cur_thread = threading.current_thread()
                self.request.sendall('receive')
            else:
                print 'close'
                break
            
if __name__ == '__main__':
    HOST = '192.168.0.8'
    PORT = 11010
    ADDR = (HOST,PORT)
    server = ThreadingTCPServer(ADDR,Handler)
    print 'listing'
    server.serve_forever()
    print server
    
