def decode(num):
    code = '';
    for i in range(1, 20):
        for j in (range(i+1, 21)):
            if num % (i + j) == 0:
                code += f'{i}{j}'
    return code

for num in range(3, 21):
    print(num, '-', decode(num))

