def filter_errors(path_in,path_out):
    with open(path_in, "r") as f_in:
        for line in f_in:
            if 'error' in line.lower():
                f_out.write(line)
print(filter_errors("data.txt"))