
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result < 2:
            return result
        is_prime = True
        i = 2
        while i < result:
            if result % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(one, two, three):
    return one + two + three

result = sum_three(2, 7, 6)
print(result)
