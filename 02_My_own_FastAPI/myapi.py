'''
This file will contain the following:
    framework logic
    router
    decorators
    server
    It will use inbuilt python libraries like socket and json
'''
import socket
import json

class MiniAPI:

    def __init__(self):
        # Store routes
        self.routes = {
            "GET": {},
            "POST": {},
            "PUT": {},
            "DELETE": {}
        }

    # GET Decorator------------------------------
    def get(self, path):
        def decorator(func):
            self.routes["GET"][path] = func
            return func
        return decorator

    # POST Decorator------------------------------
    def post(self, path):
        def decorator(func):
            self.routes["POST"][path] = func
            return func
        return decorator

    # PUT Decorator------------------------------
    def put(self, path):
        def decorator(func):
            self.routes["PUT"][path] = func
            return func
        return decorator

    # DELETE Decorator------------------------------
    def delete(self, path):
        def decorator(func):
            self.routes["DELETE"][path] = func
            return func
        return decorator

    def run(self, host="127.0.0.1", port=8000):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 and TCP because HTTP uses TCP.
        # Reuse port quickly
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind host and port
        server_socket.bind((host, port))
        server_socket.listen(5)  # Listen for incoming connections. 5 is the maximum number of queued connections.
        server_socket.settimeout(1) # Timeout for graceful shutdown
        print(f"Server running on http://{host}:{port}")

        try:
            while True:
                try:
                    client_socket, address = server_socket.accept()
                    request = client_socket.recv(1024).decode()
                    response = self.handle_request(request)
                    client_socket.sendall(response)
                    client_socket.close()

                except socket.timeout:
                    pass

        except KeyboardInterrupt:
            print("\nServer stopped gracefully.")
        finally:
            server_socket.close() # Releases port, socket, and memory resources while Otherwise: port may remain busy
            print("Socket closed.")

    # -----------------------------
    # Handle Incoming Request
    # -----------------------------
    def handle_request(self, request):
        try:
            # Split headers and body properly
            parts = request.split("\r\n\r\n")
            headers_part = parts[0]
            body = ""
            if len(parts) > 1:
                body = parts[1]
            # Split header lines
            lines = headers_part.split("\r\n")
            # First request line
            first_line = lines[0]
            method, path, _ = first_line.split()

            print(f"{method} {path}")
            # -----------------------------
            # GET Request
            # -----------------------------
            if method == "GET":

                if path in self.routes["GET"]:
                    result = self.routes["GET"][path]()
                    return self.create_response(result)

            # -----------------------------
            # POST Request
            # -----------------------------
            elif method == "POST":

                data = {}
                if body.strip():
                    data = json.loads(body)
                if path in self.routes["POST"]:
                    result = self.routes["POST"][path](data)
                    return self.create_response(result)

            # -----------------------------
            # PUT Request
            # -----------------------------
            elif method == "PUT":

                data = {}
                if body.strip():
                    data = json.loads(body)
                if path in self.routes["PUT"]:
                    result = self.routes["PUT"][path](data)
                    return self.create_response(result)

            # -----------------------------
            # DELETE Request
            # -----------------------------
            elif method == "DELETE":
                if path in self.routes["DELETE"]:
                    result = self.routes["DELETE"][path]()
                    return self.create_response(result)
            return self.not_found_response()
        except Exception as e:
            return self.server_error_response(str(e))

    # -----------------------------
    # Create HTTP Response
    # -----------------------------
    def create_response(self, data):
        json_data = json.dumps(data) # Convert Python Dictionary → JSON

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json\r\n"
            "\r\n"
            f"{json_data}"
        )
        return response.encode() # Convert String → Bytes because Sockets send bytes only.

    # -----------------------------
    # 404 Response
    # -----------------------------
    def not_found_response(self):
        response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: application/json\r\n"
            "\r\n"
            '{"error": "Route not found"}'
        )
        return response.encode() # Convert String → Bytes because Sockets send bytes only.

    # -----------------------------
    # 500 Response
    # -----------------------------
    def server_error_response(self, error):
        response = (
            "HTTP/1.1 500 Internal Server Error\r\n"
            "Content-Type: application/json\r\n"
            "\r\n"
            f'{{"error": "{error}"}}'
        )
        return response.encode() # Convert String → Bytes because Sockets send bytes only.

