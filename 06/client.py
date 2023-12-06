import socket
import concurrent.futures
import sys
import os
from help import PORT

def process_url(url):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(('localhost', PORT))
        client_socket.sendall(url.encode())
        message = client_socket.recv(1024).decode()
        return message

urls = None

filename = sys.argv[2]
if os.path.isfile(filename):
    with open(filename) as file:
        urls = [line.rstrip() for line in file]
else:
    print("File is not exist!")
    exit()

with concurrent.futures.ThreadPoolExecutor(max_workers=int(sys.argv[1])) as executor:
    for url, message in zip(urls, executor.map(process_url, urls)):
        print(f"Ответ для {url}: {message}")
