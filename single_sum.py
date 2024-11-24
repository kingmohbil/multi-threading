import time

from termcolor import colored
from common.file_sum import sum_txt_file

start_time = time.time()
print(colored("Program started executing... 🏃‍", 'green'))

res = 0

for i in range(40):
    file_path = f"data/data {(i % 10) + 1}.txt"
    with open(file_path, 'r') as file:
        lines = file.readlines()
        res += sum_txt_file(lines)

end_time = time.time()

execution_time = end_time - start_time

print(colored(f"Program result: {res}", 'yellow'))
print(colored(f"Program finished executing... ✅ in {round(execution_time, 2)}s", 'green'))

exit(0)
