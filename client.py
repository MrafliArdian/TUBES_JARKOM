
import socket
import sys


def http_client(server_host, server_port, filename):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    client_socket.connect((server_host, int(server_port))) 
    
   
    request = f"GET {filename} HTTP/1.1\r\nHost: {server_host}\r\nConnection: close\r\n\r\n"
    client_socket.sendall(request.encode())
    
    response = b""
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response += data
    
    client_socket.close() 
    
    print(response.decode()) 

if __name__ == "__main__":
    if len(sys.argv) != 4: 
        print("Please use this command line format on your terminal: python client.py <server_host> <server_port> <filename>")
        sys.exit(1)
        
    server_host = sys.argv[1]
    server_port = sys.argv[2]
    filename = sys.argv[3]
  
    http_client(server_host, server_port, filename)
