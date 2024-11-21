from time import sleep, time
from multiprocessing import Pool

def read_info(name: str) -> None:
    all_data = []
    with open(name, 'r') as f:
        for line in f:
            all_data.append(line)
        print(f'Файл {name} содержит {len(all_data)} строк')

if __name__ == '__main__':
    filenames = [f'module10/Files/file {number}.txt' for number in range(1, 4)]

    start = time()
    for name in filenames:
        read_info(name)

    end = time()
    print(end - start, '(линейно)')

    start = time()
    with Pool() as pool:
        results = pool.map(read_info, filenames)

    end = time()
    print(end - start, '(многопроцессорный)')