"""Module for Tic-Tac-Toe game."""

import random
import os
import time

class TicTacGame:
    """
    Класс игры крестики-нолики
    """
    def __init__(self):
        """
        Инициализация класса
        """
        self.matrix = [['-' for _ in range(3)] for _ in range(3)]
        self.step = []
        self.counter = 0

    def people_input_process(self):
        """
        Ввод человека
        """
        while True:
            input_list = input("Введите позицию строки и столбца: ").split()
            if self.is_correct_input(input_list):
                return int(input_list[0]), int(input_list[1])

    def output_process(self, i, j):
        """
        Обновление доски и ее вывод

        :param i: Номер строки.
        :param j: Номер столбца.
        """
        self.matrix[i][j] = 'O' if self.counter % 2 else 'X'
        for row in self.matrix:
            print(*row)
        print()
        self.counter += 1

    def comp_comp_game(self):
        """
        Процесс игры компьютера против компьютера
        """
        while len(self.step) != 9:
            pair = (random.randint(0, 2), random.randint(0, 2))
            if pair not in self.step:
                self.step.append(pair)
        while self.counter < 9:
            i, j = self.step[self.counter]
            self.output_process(i, j)
            if self.check_end():
                print(f"Победил {self.counter % 2 + 1} компьютер!")
                break
            time.sleep(1)
        if not self.check_end():
            print("Ничья!")
        print("Игра завершена!\n\n")

    def comp_people_game(self):
        """
        Процесс игры компьютера против человека
        """
        comp_step = []
        while len(comp_step) != 9:
            pair = (random.randint(0, 2), random.randint(0, 2))
            if pair not in comp_step:
                comp_step.append(pair)
        while self.counter < 9:
            comp_count = 0
            if not self.counter % 2:
                i, j = self.people_input_process()
            else:
                while True:
                    i, j = comp_step[comp_count]
                    if (i, j) not in self.step:
                        self.step.append((i, j))
                        break
                    comp_count += 1
            self.output_process(i, j)
            if self.check_end():
                print("Вы победили!" if self.counter % 2 + 1 == 2 else "Победил компьютер!")
                break
            time.sleep(1)
        if not self.check_end():
            print("Ничья!")
        print("Игра завершена!\n\n")

    def people_people_game(self):
        """
        Процесс игры человека против человека
        """
        while self.counter < 9:
            i, j = self.people_input_process()
            self.output_process(i, j)
            if self.check_end():
                print(f"Победил {self.counter % 2 + 1} пользователь!")
                break
            time.sleep(1)
        if not self.check_end():
            print("Ничья!")
        print("Игра завершена!\n\n")

    def start_game(self):
        """
        Начало игры
        """
        os.system('clear')
        while True:
            type_of_work = input("""
Введите тип режима игры:\n\t1: Компьютер против компьютера
\t2: Компьютер против человека
\t3: Человек против человека
Для выхода введите: 0
Ваш ввод: """)
            os.system('clear')
            self.matrix = [['-' for _ in range(3)] for _ in range(3)]
            self.step = []
            self.counter = 0
            if type_of_work == '1':
                self.comp_comp_game()
            elif type_of_work == '2':
                self.comp_people_game()
            elif type_of_work == '3':
                self.people_people_game()
            elif type_of_work == '0':
                break
            else:
                print("Некорректный режим!")

    def check_end(self):
        """
        Проверка на конец игры
        """
        for i in range(3):
            if self.matrix[i][0] == self.matrix[i][1] == self.matrix[i][2] != '-':
                return True
            if self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] != '-':
                return True

        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] != '-':
            return True
        if self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] != '-':
            return True

        return False

    def is_correct_input(self, input_list):
        """
        Проверка корректности ввода
        :param input_list: ввод пользователя(разделенный по пробелу)
        """
        if len(input_list) == 2:
            if input_list[0] is not None and input_list[1] is not None\
            and (input_list[0].isdigit() and input_list[1].isdigit()):
                input_list[0], input_list[1] = int(input_list[0]), int(input_list[1])
            else:
                print("Должно быть введено 2 ЦЕЛЫХ числа,",
                      "принадлежащих отрезу от 0 до 2 включительно!\n",
                      "Пример ввода: 1 2")
                return False
        else:
            print("Должно быть введено 2 целых числа,",
                  "принадлежащих отрезу от 0 до 2 включительно!\n",
                  "Пример ввода: 1 2")
            return False
        if (input_list[0] in [0, 1, 2] and input_list[1] in [0, 1, 2]):
            if (input_list[0], input_list[1]) not in self.step:
                self.step.append((input_list[0], input_list[1]))
                return True
            print("Позиции:")
            print(*self.step, sep="\n")
            print("уже заняты!")
            return False
        print("Числа i, j должны быть целыми",
              "и принадлежащими отрезу от 0 до 2 включительно!\n",
              "Пример ввода: 1 2")
        return False

if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
