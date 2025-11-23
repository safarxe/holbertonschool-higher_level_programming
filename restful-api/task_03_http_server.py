#!/usr/bin/python3
"""
Module for developing a simple API using Python with http.server.
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    A simple HTTP request handler for a basic API.
    """

    def do_GET(self):
        """
        Handles GET requests.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler,
        port=8000):
    """
    Runs the HTTP server.

    Args:
        server_class: The server class to use
        handler_class: The handler class to use
        port: The port to run the server on
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()

