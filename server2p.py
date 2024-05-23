import socket
import base64

# Function to decode a Base64 string and save it to a file
def decode_base64_to_image(encoded_string, output_path):
    with open(output_path, "wb") as output_image:
        output_image.write(base64.b64decode(encoded_string))

# TCP server
def server():
    host = "0.0.0.0"  # Listen on all available interfaces
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server listening on port", port)

    while True:
        client_socket, addr = server_socket.accept()
        print("Connection from:", addr)

        # Receive encoded image data
        encoded_image_data = client_socket.recv(4096)

        # Decode and save the image
        decode_base64_to_image(encoded_image_data, "received_image.jpg")

        print("Image received and saved.")

        client_socket.close()

if __name__ == "__main__":
    server()