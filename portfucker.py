import socketserver

file = open('portscan.log', 'a')

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        file.write(f"[portfucker] Portscan detected, client: {self.client_address[0]}\n")
        file.flush()

addr = ('0.0.0.0', 23)
with socketserver.TCPServer(addr, RequestHandler) as server:
    print("doing funnies")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("CTRL-C, stopping.")
    finally:
        file.close()
