import socket

def tcp_echo_client(server_host="127.0.0.1", server_port=1234):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_host, server_port))
    
    message = input()
    s.sendall(message.encode())
    data = s.recv(1024)
    print("Echoed from server", data.decode())
    
    s.close()

tcp_echo_client()