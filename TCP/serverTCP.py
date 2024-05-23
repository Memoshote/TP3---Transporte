import socket

def main():
    host = '127.0.0.1'  # Server IP address
    port = 12345        # Server port

    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to the address and port
        s.bind((host, port))

        # Listen for incoming connections
        s.listen()

        print("TCP Server is listening...")

        # Accept a connection
        conn, addr = s.accept()

        with conn:
            print(f"Connected by {addr}")

            # Receive data from the client
            data = conn.recv(1024).decode()
            print(f"Received: {data} from {addr[0]}:{addr[1]}")

if __name__ == "__main__":
    main()
