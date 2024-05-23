import socket

def main():
    host = '127.0.0.1'  # Server IP address
    port = 9999        # Server port

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Send a message
        message = "Hello, UDP Server!"
        s.sendto(message.encode(), (host, port))

        print(f"Sent: {message}")

if __name__ == "__main__":
    main()
