def calc(line:str):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        print(f'Результат: {operand_1 + operand_2}')
    if operation == '-':
        print(f'Результат: {operand_1 - operand_2}')
    if operation == '*':
        print(f'Результат: {operand_1 * operand_2}')
    if operation == '/':
        print(f'Результат: {operand_1 / operand_2}')
    if operation == '%':
        print(f'Результат: {operand_1 % operand_2}')
    if operation == '**':
        print(f'Результат: {operand_1 ** operand_2}')
    if operation == '//':
        print(f'Результат: {operand_1 // operand_2}')

cnt = 0
try:
    with open('data.txt', 'r') as file:
        for line in file:
            cnt += 1
            try:
                calc(line)
            except ValueError as exc:
                if 'unpack' in exc.args[0]:
                    print(f'Ошибка в строке {cnt}, не хватает данных для ответа')
                elif 'int' in exc.args[0]:
                    print(f'Ошибка в строке {cnt}, нельзя перевести в число')
                else:
                    print(f'Ошибка в строке {cnt}, возникла ошибка: {exc} с кодом {exc.args[0]}')
except FileNotFoundError:
    print('Файл с данными не найден')