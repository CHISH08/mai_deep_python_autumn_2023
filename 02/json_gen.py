"""
Generate json
"""
import json
import random
from faker import Faker


def generate():
    '''
    Создание тестов с помощью faker
    '''
    fake = Faker()
    data_json = {}
    key_count = random.randint(0, 20)
    for i in range(key_count):
        data_json[fake.name()] = fake.text()


    index = random.randint(0, len(data_json.keys()) + 4)
    key = (list(data_json.keys()) + [fake.name() for i in range(5)])[index]
    if index < len(data_json.keys()):
        words = (list(data_json.values())[index]).split() + ['fake' for i in range(15)]
        index_to_word = random.randint(0, len(words) - 1)
        words = words[index_to_word]
    else:
        words = 'fake'

    return str(json.dumps(data_json)), key, words
