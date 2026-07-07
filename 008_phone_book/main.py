def add_contact(contacts, name, phone):
    if name in contacts:
        return False
    contacts[name] = phone
    return True


def find_contact(contacts, name):
    if name not in contacts:
        return None
    return contacts.get(name)


def remove_contact(contacts, name):
    if name not in contacts:
        return False
    del contacts[name]
    return True


def update_contact(contacts, name, phone):
    if name not in contacts:
        return False
    contacts[name] = phone
    return True


def main():
    add_command = "add"
    find_command = "find"
    show_command = "show"
    remove_command = "remove"
    update_command = "update"
    exit_command = "exit"
    contacts = {}

    while True:
        command = input(f"Введите команду: ").strip().lower()
        if command == exit_command:
            print("До встречи!")
            break
        elif command == add_command:
            contact_name = input("Введите имя контакта: ").strip()
            contact_phone = input("Введите телефон контакта: ").strip()
            if add_contact(contacts, contact_name, contact_phone):
                print("Контакт успешно добавлен.")
            else:
                print("Контакт с таким именем уже существует.")
        elif command == find_command:
            contact_name = input("Введите имя контакта: ").strip()
            contact_phone = find_contact(contacts, contact_name)
            if contact_phone is not None:
                print(f"Телефон контакта {contact_name}: {contact_phone}")
            else:
                print(f"Контакт {contact_name} не найден в списке.")
        elif command == show_command:
            if not contacts:
                print("Телефонная книга пуста.")
                continue
            for key, value in sorted(contacts.items()):
                print(f"{key}: {value}")
        elif command == remove_command:
            contact_name = input("Введите имя контакта: ").strip()
            if remove_contact(contacts, contact_name):
                print(f"Контакт {contact_name} успешно удалён")
            else:
                print(f"Контакт {contact_name} не найден в списке.")
        elif command == update_command:
            contact_name = input("Введите имя контакта: ").strip()
            contact_phone = input("Введите телефон контакта: ").strip()
            if update_contact(contacts, contact_name, contact_phone):
                print("Контакт успешно обновлён.")
            else:
                print("Контакт с таким именем не существует.")
        else:
            print("Такой команды не существует.")


if __name__ == '__main__':
    main()