import time

def sum_txt_file(file_path: str) -> float:
    time.sleep(1)
    with open(file_path, 'r') as file:
        res = 0
        for line in file.readlines():
            s = [float(c) for c in line.strip().replace("\n", "").split(" ")]
            res += sum(s)
        return res