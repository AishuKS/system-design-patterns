import socket

def udp_echo_server(host="127.0.0.1", port=1234):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    print("UDP Server running on {host}: {port}")
    
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")
        s.sendto(data, addr)
        
udp_echo_server()