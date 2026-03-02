import socket


def init_server(ip: str, port: int) -> socket.socket:
    s = socket.socket()
    s.bind((ip, port))
    s.listen()
    return s


s = init_server("127.0.0.1", 8000)

while True:
    c, addr = s.accept()
    print(c.recv(1024).decode())
    print(addr)
    body ="""
<html>
  <body>
    <h1>Hello world!</h1>
  </body>
</html>
    """
    CRLF = "\r\n"
    header = "HTTP/1.1 200 OK"
    response = header + CRLF + CRLF + body
    c.send(response.encode())
    c.close()
    print("------------------------")
