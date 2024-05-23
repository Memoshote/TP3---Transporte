import socket

def main():
    host = '127.0.0.1'  # Server IP address
    port = 9999        # Server port

    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((host, port))

        # Send a message
        message = "Hello, TCP Server!"
        s.sendall(message.encode())

        print(f"Sent: {message}")

if __name__ == "__main__":
    main()
