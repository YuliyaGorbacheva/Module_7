def custom_write(file_name, strings):
    number_string = 0
    strings_positions = {}
    file = open(file_name,'w', encoding='utf-8')
    for string in strings:
        byte_string = file.tell()
        file.write(f'{string}\n')
        number_string += 1
        strings_positions.update({(number_string,byte_string): string})
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