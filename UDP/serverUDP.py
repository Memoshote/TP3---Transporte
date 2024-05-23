import socket

def main():
    host = '127.0.0.1'  # Server IP address
    port = 12345        # Server port

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Bind the socket to the address and port
        s.bind((host, port))

        print("UDP Server is listening...")

        # Receive data from the client
        data, addr = s.recvfrom(1024)
        print(f"Received: {data.decode()} from {addr[0]}:{addr[1]}")

if __name__ == "__main__":
    main()
