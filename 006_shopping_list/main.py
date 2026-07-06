add_command = "add"
remove_command = "remove"
exit_command = "exit"
show_command = "show"
clear_command = "clear"
purchase_list = list()

while True:
    user_input = input("Команда: ").strip().lower()
    if user_input == exit_command:
        print("До встречи!")
        break
    elif user_input == add_command:
        item_name = input("Название покупки: ").strip()
        if item_name not in purchase_list:
            purchase_list.append(item_name)
            print("Покупка добавлена.")
        else:
            print("Покупка уже есть в списке.")
    elif user_input == remove_command:
        item_name = input("Название покупки: ").strip()
        if item_name not in purchase_list:
            print("Такого пункта нет в списке")
        else:
            purchase_list.remove(item_name)
            print("Покупка удалена.")
    elif user_input == show_command:
        if not purchase_list:
            print("Список покупок пуст.")
        else:
            for index, item in enumerate(purchase_list, start=1):
                print(f"{index}. {item}")
            print(f"Всего покупок: {len(purchase_list)}")
    elif user_input == clear_command:
        if not purchase_list:
            print("Список уже пуст")
            continue
        purchase_list.clear()
        print("Список очищен")
    else:
        print("Неизвестная команда.")



