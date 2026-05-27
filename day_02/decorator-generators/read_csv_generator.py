# Generator that will read csv file line by line

def read_large_file_gen(filePath):
    with open(filePath) as file:
        for line in file:
            yield line.strip()
