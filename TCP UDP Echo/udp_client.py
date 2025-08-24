import socket

def udp_echo_client(server_host = "127.0.0.1", server_port=1234):
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     
     message = input()
     s.sendto(message.encode(), (server_host, server_port))
     data, addr = s.recvfrom(1024)
     print("Echoed from server: ", data.decode())
     s.close()

udp_echo_client()