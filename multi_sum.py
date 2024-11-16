from termcolor import colored

import threading
import time

from common.custom_thread import CustomThread
from common.file_sum import sum_txt_file


def sum_txt_file_wrapper(file_paths: list[str]):
    thread_name = threading.current_thread().name
    print(colored(f"{thread_name} started", "blue"))
    total = 0

    for i in file_paths:
        total += sum_txt_file(i)

    print(colored(f"{thread_name}   ended", "yellow"))

    return total


thread1_files = []
thread2_files = []
thread3_files = []
thread4_files = []

for i in range(3):
    file_path = f"data/data.txt"
    thread1_files.append(file_path)
    thread2_files.append(file_path)
    thread3_files.append(file_path)
    thread4_files.append(file_path)


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
