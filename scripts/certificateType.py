import ssl
import socket

def get_ssl_certificate_type(hostname, port):
    try:
        # Establish an SSL connection to the remote server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the server certificate
                cert = ssock.getpeercert()
                cipher = ssock.cipher()

                # Extract certificate details
                key_exchange = cipher[0]  # Key exchange algorithm
                encryption_cipher = cipher[1]  # Encryption cipher

                return key_exchange, encryption_cipher

    except ssl.SSLError as e:
        return None

if __name__ == "__main__":
    hostname = "dsnl.in"  # Replace with the target hostname
    port = 443  # Default HTTPS port

    result = get_ssl_certificate_type(hostname, port)

    if result:
        key_exchange, encryption_cipher = result
        print(f"Key Exchange Algorithm: {key_exchange}")
        print(f"Encryption Cipher: {encryption_cipher}")
    else:
        print("Failed to retrieve SSL certificate type.")
