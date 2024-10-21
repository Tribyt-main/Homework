import time
import multiprocessing

"""start = time.time()"""


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        a = file.read().splitlines()
        all_data.append(a)
    print(all_data)


"""filenames = [f'./file {number}.txt' for number in range(1, 5)]
for name in filenames:
    read_info(name)
end = time.time()
print(f'Время затраченное на выполнение функции: {end - start}')"""

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        start = time.time()
        pool.map(read_info, filenames)
    end = time.time()
    print(f'Время затраченное на выполнение функции: {end - start}')
