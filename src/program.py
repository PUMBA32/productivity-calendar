from typing import List
from settings import *
import os


class Program:
    __DAYS_PATH = DAYS_PATH
    __STATISTIC_PATH = STATISTIC_PATH
    __ELS_IN_ROW = ELS_IN_ROW

    def __init__(self):
        days_info = self._get_days_info()

        self.__count_of_days = sum(days_info)
        self.__completed_days = days_info[0]


    def _get_days_info(self) -> List[int]:
        '''Считывает файл с двумя числами: число завершенный дней, число оставшихся дней
        и возвращает список с этими числами конвертированными в целочисленный тип'''

        file = open(self.__DAYS_PATH, 'r')
        line = file.readline().strip().split(" ")
        file.close()
        line = [int(el) for el in line]
        return line
    

    def show_calendar(self):
        '''Выводит прямоугольный календарь на основе кол-ва дне, а также выводит статистику:
        Завершенный дни, незавершенные дне, суммарное кол-во дней'''

        arr = ['■' for _ in range(self.__completed_days)]

        for i in range(len(arr)+1, self.__count_of_days+1):
            arr.append(str(i))

        print("\n✅ days:\t", self.__completed_days)
        print("❌ days:\t", self.__count_of_days-self.__completed_days)
        print("ALL days:\t", self.__count_of_days+self.__completed_days, "\n")

        print(
            "="*(len(arr)*6+1 if len(arr) <= self.__ELS_IN_ROW else 49), 
            end="\n| "
        )

        for i, el in enumerate(arr):
            if i != 0 and i % self.__ELS_IN_ROW == 0:
                print(f"\n{"="*49}", end="\n| ")
            print('{:3} |'.format(el), end=" ")

        k = self.__count_of_days % self.__ELS_IN_ROW 

        print(f"\n{"="*(k*6+1)}")        


    def show_menu(self):
        '''Менюшка: отметить день, удалить сессию, выход'''

        print("\n[1] - mark the day")
        print("[2] - delete session")
        print("[3] - exit")

    
    def __cls(self):
        '''Очищает консоль'''

        os.system('cls')


    def choice_handler(self, choice: str) -> bool:
        '''Принимает на вход строку с числом и на его основе вызывает нужную функцию'''
        #? Переделать этот функционал из-за отсутствия необходимости в нем

        if choice == '1':
            self.__markup_day()
        elif choice == '2':
            self.__question_to_delete_session()
            return True
        return False


    def __question_to_delete_session(self):
        '''Уточняет хочет ли пользователь действительно удалить сессию или  он просто криворукий'''

        self.__cls()
        print("\nAre you really wanna delete current session?")
        mes = input("\n(y/n): ").lower().strip()

        if mes == 'y':
            self.__delete_session()


    def __markup_day(self):
        '''Считывает данные с файла обновляет значения и перезаписывает их в тот же файл'''

        line = self.__get_line_by_path(self.__DAYS_PATH)
        old_line = [int(el) for el in line]

        self.__completed_days = old_line[0] + 1
        new_line = f"{self.__completed_days} {old_line[1] - 1}"

        file = open(self.__DAYS_PATH, 'w')
        file.write(new_line)
        file.close()


    def __delete_session(self):
        '''Перезаписывает файл, очищая данные о сессии тем самым удаляя его'''

        file = open(self.__DAYS_PATH, 'w')
        file.write('0 0')
        file.close()
        self.__cls()
        print("<i> Session was closed successfully!\n")

        line = self.__get_line_by_path(self.__STATISTIC_PATH)
        self.__update_deleted_sessions(line)


    def update_session(self): 
        '''Проверяет все ли дни были отмечены, если да, то очищает список дней обновляя статистику'''

        if self.__completed_days == self.__count_of_days:
            file = open(self.__DAYS_PATH, 'w')
            file.write('0 0')
            file.close()

            line = self.__get_line_by_path(self.__STATISTIC_PATH)
            self.__update_completed_sessions(line)


    def __update_completed_sessions(self, line: List[str]):
        '''обновляет показатель законченных дней'''

        file = open(self.__STATISTIC_PATH, 'w')
        file.write(f"{line[0]} {int(line[1])+1} {line[2]}")
        file.close()


    def __update_deleted_sessions(self, line: List[str]):
        '''обновляет показатель удаленных сессий'''

        file = open(self.__STATISTIC_PATH, 'w')
        file.write(f"{line[0]} {line[1]} {int(line[2])+1}")
        file.close()


    def __get_line_by_path(self, path) -> List[str]:
        '''на основе пути до файлы возвращает список со значениями внутри файла'''

        file = open(path, 'r')
        line = file.readline().strip().split(" ")
        file.close()
        return line
    

