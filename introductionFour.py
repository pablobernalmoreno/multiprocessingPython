import time
import multiprocessing


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)..')
    time.sleep(seconds)
    print('Done Sleeping...')


if __name__ == '__main__':
    start = time.perf_counter()
    for _ in range(10):
        do_something(1.5)
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start,2)} seconds(s)')