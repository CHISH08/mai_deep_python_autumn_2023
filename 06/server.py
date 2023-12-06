'''
- Сервер должен поддерживать взаимодействие с любым числом клиентов;
- Мастер и воркеры это разные потоки в едином приложении сервера;
- Количество воркеров задается при запуске;
- Мастер слушает порт, на который клиенты будут по TCP отправлять урлы для обкачки;
- Мастер принимает запроc и передает его одному из воркеров;
- Воркер читает url от клиента;
- Воркер обкачивает url по http и возвращает клиенту топ K самых
частых слов и их частоту в формате json {"word1": 10, "word2": 5};
- После каждого обработанного урла сервер должен вывести статистику:
сколько урлов было обработано на данный момент суммарно всеми воркерами;
'''

import re
import json
import argparse
from threading import Thread, Semaphore, Lock
import socket
import requests
from bs4 import BeautifulSoup

class Master:
    '''
    class Master(build workers and check peoples request)
    '''
    def __init__(self, n_workers, k_top):
        self.port = 16573
        self.k_top = k_top
        self.worker_semaphore = Semaphore(n_workers)
        self.url_count = 0
        self.lock = Lock()

    def run(self):
        '''
        Run checker
        '''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(('localhost', self.port))
            server_socket.listen(-1)
            print(f'Сервер запущен! PORT: {self.port}')
            try:
                while True:
                    client_socket, _ = server_socket.accept()
                    with self.worker_semaphore:
                        client_thread = Worker(client_socket, self.k_top,\
                                               self.worker_semaphore, self)
                        client_thread.start()
            except KeyboardInterrupt:
                server_socket.close()

    def increment_url_count(self):
        """
        return count url
        """
        with self.lock:
            self.url_count += 1
            print(f"Количество обработанных URL: {self.url_count}")

class Worker(Thread):
    '''
    class workers(work on people request)
    '''
    def __init__(self, client_socket, k_top, semaphore, master):
        super().__init__()
        self.client_socket = client_socket
        self.k_top = k_top
        self.semaphore = semaphore
        self.master = master

    def run(self):
        '''
        Run request processing
        '''
        try:
            urls = self.client_socket.recv(1024).decode()
            data = self.get_top_k_words(urls)
            self.client_socket.sendall(data.encode())
        except socket.error as err:
            print(f"Ошибка сокета: {err}")
        finally:
            self.client_socket.close()
            self.master.increment_url_count()
            self.semaphore.release()

    def get_top_k_words(self, url):
        '''
        Read link text
        '''
        try:
            response = requests.get(url, timeout=0.2)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text()
            words = re.findall(r'\b\w+\b', text.lower())
            word_freq = {}
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
            sorted_word_freq = dict(sorted(word_freq.items(),
                                           key=lambda item: item[1],
                                           reverse=True)[:self.k_top])
            return json.dumps(sorted_word_freq, ensure_ascii=False)
        except requests.RequestException as err:
            return json.dumps({"error": f"Ошибка запроса: {err}"})

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Сервак')
    parser.add_argument('-w', type=int, help='Количество воркеров')
    parser.add_argument('-k', type=int, help='Количество слов с максимальным кол-вом')

    args = parser.parse_args()
    test = Master(args.w, args.k)
    test.run()
