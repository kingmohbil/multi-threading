from termcolor import colored

import threading
import time

from common.custom_thread import CustomThread
from common.file_sum import sum_txt_file


def sum_txt_file_wrapper(lines: list[[str]]):
    thread_name = threading.current_thread().name
    print(colored(f"{thread_name} started", "blue"))
    total = 0

    for line in lines:
        total += sum_txt_file(line)

    print(colored(f"{thread_name}   ended", "yellow"))

    return total


thread1_files = []
thread2_files = []
thread3_files = []
thread4_files = []

for i in range(10):
    file_path = f"data/data {i + 1}.txt"

    with open(file_path, 'r') as file:
        lines = file.readlines()

        thread1_files.append(lines)
        thread2_files.append(lines)
        thread3_files.append(lines)
        thread4_files.append(lines)

print(thread1_files)

start_time = time.time()

print(colored("Program Started 🏃\n"))

res = 0

thread1 = CustomThread(target=sum_txt_file_wrapper, args=(thread1_files,))

thread2 = CustomThread(target=sum_txt_file_wrapper, args=(thread2_files,))

thread3 = CustomThread(target=sum_txt_file_wrapper, args=(thread3_files,))

thread4 = CustomThread(target=sum_txt_file_wrapper, args=(thread4_files,))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

res += thread1.join()
res += thread2.join()
res += thread3.join()
res += thread4.join()

end_time = time.time()

execution_time = end_time - start_time
print(colored(f"\nResult: {res}, done in ✅  {round(execution_time, 2)}s", "green"))

exit(0)
