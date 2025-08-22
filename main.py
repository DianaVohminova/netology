HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя)
show - напечатать все добавленные задачи.
"""
tasks = []
today = []
tomorrow = []
other = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)

    elif command == "show":
        #print(tasks)
        print("Сегодня\n", today)
        print("Завтра\n",tomorrow)
        print("Другие\n",other)

    elif command == "todo":
        task = input("Введите задачу: ")
        tasks.append(task)
        print(f"Задача {task} добавлена")

    elif command == "add":
        data = input("Введите дату: ")
        task = input("Введите задачу: ")
        tasks.append(task)
        print(f"Задача {task} добавлена")
        if data == "Сегодня":
            today.append(task)
        elif data == "Завтра":
            tomorrow.append(task)
        elif data == "Другие":
            other.append(task)

    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        run = False
