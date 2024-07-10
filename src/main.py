from program import Program
from settings import (
    STATISTIC_PATH,
    DAYS_PATH
)
import os


def cls():
    os.system('cls')    


def show_statistic():
    path = 'D:\\CL Утилиты\\Календарь для работы\\data\\main_statistic.txt'
    file = open(path, 'r')
    line = file.readline().strip().split(" ")
    file.close()

    print(f"sessions: {line[0]}")
    print(f"completed: {line[1]}")
    print(f"deleted: {line[2]}\n")


def clear_statistic():
    file = open(STATISTIC_PATH, 'w')
    file.write('0 0 0')
    file.close()
    print("<i> statistic was cleared\n")

def show_menu():
    #cls()
    print("[1] - new session")
    print("[2] - statistic")
    print("[3] - clear statistic")
    print("[4] - exit\n")


def create_session():
    cls()
    days = input("enter number of days: ")

    file = open(DAYS_PATH, 'w')
    file.write(f'0 {days}')
    file.close()

    update_count_of_sessions()


def get_session_state() -> bool:
    file = open(DAYS_PATH, 'r')
    line = file.readline().strip()
    file.close()
    return False if line == '0 0' else True


def update_count_of_sessions():
    file = open(STATISTIC_PATH, 'r')
    line = file.readline().strip().split(" ")
    file.close()

    file = open(STATISTIC_PATH, 'w')
    file.write(f"{int(line[0])+1} {line[1]} {line[2]}")
    file.close()


def main() -> int:
    while True:
        there_is_session = get_session_state()
        if there_is_session:
            program = Program()
            while there_is_session:
                cls()
                program.show_calendar()
                program.show_menu()

                choice = input("\n>>> ")
                
                if choice != '1' and choice != '2':
                    return 0
                
                if program.choice_handler(choice):
                    break

                program.update_session()
                there_is_session = get_session_state()
        else:
            while True:
                show_menu()
                choice = input("\n>>> ").strip()

                if choice == '1':
                    create_session()
                    break
                elif choice == '2':
                    cls()
                    show_statistic()
                elif choice == '3':
                    cls()
                    clear_statistic()
                else:
                    return 0


if __name__ == "__main__":
    cls()
    print("\nexit code",main())