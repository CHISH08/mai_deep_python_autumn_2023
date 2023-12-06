import unittest
import socket
import json
PORT = 16573

class TestServer(unittest.TestCase):
    def test_server_response(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(('localhost', PORT))
            client_socket.sendall(b'http://example.com')
            response = client_socket.recv(1024).decode()
            self.assertEqual(response, '{"domain": 4, "in": 3, "example": 2, "this": 2, "for": 2, "use": 2, "is": 1}')
    def test_server_response_type(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(('localhost', PORT))
            client_socket.sendall(b'http://example.com')
            response = client_socket.recv(1024).decode()
            self.assertTrue(isinstance(response, str))
    def test_server_response(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(('localhost', PORT))
            client_socket.sendall(b'http://143523')
            response = client_socket.recv(1024).decode()
            response = json.loads(response)
            self.assertTrue('error' in response.keys())
                             
if __name__ == '__main__':
    unittest.main()
