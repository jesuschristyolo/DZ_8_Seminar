def show_all():
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    print(data)
    file.close()
    for i in data:
        print(i)


def find_contact():
    find_string = input("Введите поисковый запрос")
    file = open('sample.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for index, data_str in enumerate(data):
        if find_string in data_str:
            print("found data= ", data_str)
    file.close()


def addcontact():
    file = open('sample.txt', 'a', encoding='UTF-8')
    data = input("Введите фамилию, телефон, комментарий (разделяя ;)")  # .split(';')
    data += '\n'
    file.write(data)
    file.close()


def change_person():
    old_value = input("Введите, какое значение вы ищете: ")
    new_value = input("Введите новое значение: ")
    file = open('sample.txt', 'r', encoding='UTF-8')
    filedata = file.read()
    file.close()

    newdata = filedata.replace(old_value, new_value)

    file = open('sample.txt', 'w', encoding='UTF-8')
    file.write(newdata)
    file.close()


def delete_person():
    delete_string = input("Введите запись которую хотите удалить: ")
    with open('sample.txt', 'r', encoding='UTF-8') as file:
        filedata = file.readlines()
    with open('sample.txt', 'w', encoding='UTF-8') as file:
        for data_str in filedata:
            if delete_string not in data_str:
                file.write(data_str)


def main_menu():
    print('Main menu')
    print('1.Показать всю книгу')
    print('2.Добавить новую запись')
    print('3.Редактировать запись')
    print('4.Поиск контакта')
    print('5.Назад в меню')
    print('6.Удалить контакт')


if __name__ == '__main__':
    main_menu()

    while True:
        choose = int(input("Введите пункт меню: "))
        if choose == 2:
            addcontact()
        if choose == 4:
            find_contact()
        if choose == 1:
            show_all()
        if choose == 3:
            change_person()
        if choose == 5:
            main_menu()
        if choose == 6:
            delete_person()
