from datetime import datetime
from create import note_create
from read import print_note
from update import change_note
from delete import delete_note


def interface():
    print(
        "Это программа заметок. Выберите действие \
        \n 1 - Cоздать заметку \n 2 - Вывести заметку \
        \n 3 - Редактировать заметку \n 4 - Удалить заметку"
    )
    command = int(input("Укажите номер "))
    while command not in [1, 2, 3, 4]:
        print("Некорректный ввод. Попробуйте еще раз ")
        command = int(input("Укажите номер "))

    if command == 1:
        note_create()
    elif command == 2:
        print_note()
    elif command == 3:
        change_note()
    elif command == 4:
        delete_note()
    


if __name__ == "__main__":
    interface()
