def sum_txt_file(lines: [str]) -> float:
    res = 0
    for line in lines:
        s = [float(c) for c in line.strip().replace("\n", "").split(" ")]
        res += sum(s)
    return res
