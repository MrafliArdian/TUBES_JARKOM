import socket
import threading
import os

def handle_client(client_socket):
    try:
        request = client_socket.recv(1024).decode()
        print(f"Thread {threading.current_thread().name}: Received request: {request}")
        
        headers = request.split('\n')
        filename = headers[0].split()[1]
        
        if filename == '/kelompok_ganteng.html':
            filename = '/kelompok_ganteng.html'
        
        filepath = os.getcwd() + filename

        if os.path.exists(filepath):
            with open(filepath, 'rb') as file:
                response_content = file.read()
                response_headers = (
                    "HTTP/1.1 200 OK\n"
                    "Content-Type: text/html\n"
                    f"Content-Length: {len(response_content)}\n"
                    "Connection: close\n\n"
                )
        else:
            response_content = b"<html><body><h1>404 Not Found</h1></body></html>"
            response_headers = (
                "HTTP/1.1 404 Not Found\n"
                "Content-Type: text/html\n"
                "Connection: close\n\n"
            )
        
        response = response_headers.encode() + response_content
        client_socket.sendall(response)
        print(f"Thread {threading.current_thread().name}: Response sent")
    finally:
        client_socket.close()
        print(f"Thread {threading.current_thread().name}: Closed connection")

def main():
    server_ip = '127.0.0.1'
    server_port = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    print(f"Listening on {server_ip}:{server_port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
