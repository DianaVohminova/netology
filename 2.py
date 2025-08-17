# Задание 2
print('Задание 2')
stroka = ''
for _ in range(3):
    print('Введите дату: ', end='')
    data = input()

    print('Введите задачу: ', end='')
    task = input()

    stroka = stroka + data + ' ' + task + '\n'
print(stroka)
