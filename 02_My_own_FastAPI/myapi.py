'''
This file will contain the following:
    framework logic
    router
    decorators
    server
'''


import socket
import json


class MiniAPI:

    def __init__(self):
        # Store routes
        self.routes = {
            "GET": {},
            "POST": {}
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


    # Start Server------------------------------
    def run(self, host="127.0.0.1", port=8000):

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server running on http://{host}:{port}")

        while True:

            client_socket, address = server_socket.accept()
            request = client_socket.recv(1024).decode()
            response = self.handle_request(request)
            client_socket.sendall(response)
            client_socket.close()

    # -----------------------------
    # Handle Incoming Request
    # -----------------------------
    def handle_request(self, request):

        try:
            lines = request.split("\r\n")
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

                body = lines[-1]
                data = {}

                if body:
                    data = json.loads(body)

                if path in self.routes["POST"]:
                    result = self.routes["POST"][path](data)
                    return self.create_response(result)

            return self.not_found_response()

        except Exception as e:
            return self.server_error_response(str(e))

    # -----------------------------
    # Create HTTP Response
    # -----------------------------
    def create_response(self, data):

        json_data = json.dumps(data)

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json\r\n"
            "\r\n"
            f"{json_data}"
        )
        return response.encode()

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

        return response.encode()

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

        return response.encode()

