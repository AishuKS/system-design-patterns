import socket

def tcp_echo_server(host = "127.0.0.1", port = 1234):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    print(f"TCP Server running on {host}: {port}")
    
    conn, addr = s.accept()
    print("Connected by: ", addr)
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Received: ", data.decode())
        conn.sendall(data)
        
    conn.close()
    s.close()

tcp_echo_server()