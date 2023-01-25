import csv


def unload_file(file_name, list_of_dict):
    with open(file_name, 'w', newline='', encoding='UTF-8') as data_base:
        writer = csv.writer(data_base, delimiter=';',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(list_of_dict)
    print("Writing complete")


def load_file(path_file):
    new_db = []
    with open(f'{path_file}', 'r', encoding='UTF-8') as File:
        reader = csv.reader(File, delimiter=';',
                            quotechar=',',  quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            new_db.append(row)
    return True, new_db


def ChangeBase(path_file, data_base):
    Status, new_db = load_file(path_file)
    data_base = new_db
    unload_file('database.csv', data_base)
    return Status, data_base


def add_cont(data_base: list, user_dict: dict):
    new_contact = []
    for i in user_dict.values():
        new_contact.append(i)
    print(new_contact)
    data_base.append(new_contact)
    return data_base


def del_cont(database: list, num_str: int):
    database.pop(num_str-1)  # тк с нуля индекс
    return database


def edit_cont(database: str, user_dict: dict, num_str: int):
    userList = []
    for i in user_dict.values():
        userList.append(i)
    database[num_str] = userList
    return database


# возвращаем вырезку из базы

def find_cont(find_str: str, data_base: list) -> list:
    find_data = []
    for item in data_base:
        if find_str.lower() in ' '.join(item).lower():  # не валуес тк лист
            find_data.append(item)
    if len(find_data) != 0:
        for item in find_data:
            i = data_base.index(item)+1  # тк с нуля индекс
            print(
                f'{i:4} | {item[0]:13} | {item[1]:11} | {item[2]:12} | {item[3]}')
    else:
        print()
        print(f'Контакта {find_str} в базе нет')
        print()  
