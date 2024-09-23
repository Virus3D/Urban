def custom_write(file_name: str, strings:list) -> dict:
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for index, line in enumerate(strings):
        tell = file.tell()
        strings_positions[(index+1, tell)] = line
        file.write(line + "\n")
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
