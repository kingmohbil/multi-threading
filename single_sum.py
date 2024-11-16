import time

from termcolor import colored
from common.file_sum import sum_txt_file

start_time = time.time()
print(colored("Program started executing... 🏃‍♂️", 'green'))

res = 0

for i in range(12):
    file_path = f"data/data.txt"
    res += sum_txt_file(file_path)

end_time = time.time()

execution_time = end_time - start_time

print(colored(f"Program result: {res}", 'yellow'))
print(colored(f"Program finished executing... ✅ in {round(execution_time, 2)}s", 'green'))
