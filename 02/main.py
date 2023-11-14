"""
Файл для 2 дз
"""

import json
import time
import json_gen


def mean(k):
    """
    Декоратор для функции, которая выводит среднее по времени среди k последних вызовов
    """
    avg_time_k = []
    avg_time_k_sum = 0

    def _mean(func):
        def wrapper(*args, **kwargs):
            nonlocal avg_time_k
            nonlocal avg_time_k_sum
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            time_taken = end_time - start_time
            avg_time_k.append(time_taken)
            avg_time_k_sum += time_taken
            if len(avg_time_k) > k:
                avg_time_k_sum -= avg_time_k[0]
                avg_time_k.pop(0)
            print(avg_time_k_sum / len(avg_time_k))
            return res

        return wrapper

    return _mean


PARAM = 10


@mean(PARAM)
def parse_json(json_str: str, keyword_callback, required_fields=None, keywords=None):
    """
    Парсер json
    """
    json_doc = json.loads(json_str)
    if keywords in json_doc.keys():
        lst = [
            str(keyword_callback(word)) if word == required_fields else word
            for word in json_doc[keywords].split()
        ]
        json_doc[keywords] = " ".join(lst)
    return json_doc


def main(count_iter):
    """
    main function for tests
    """
    for _ in range(count_iter):
        json_string, key, req_fields = json_gen.generate()
        __ = parse_json(json_string, len, req_fields, key)
