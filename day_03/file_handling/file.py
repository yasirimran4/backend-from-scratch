import csv
import json

from pathlib import Path
# Read CSV File as reader function
def read_csv(filePath):
    with open(filePath) as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Read csv as DictReader
def read_csv_as_dict(filePath):
    with open(filePath) as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row['city']) # Just print City Column

# Write to CSV
def write_to_csv(filePath):
    with open(filePath,'a',newline="") as file:   # 'w' will over write data and 'a' willa pend at last
        writer = csv.writer(file)

        writer.writerow(['6',"Yasir","20","GRW"])   # Will be append at last of file. 


path = Path("data/simple_data.csv")
if path.exists():
    write_to_csv(path)
    read_csv(path)



# Read Json File as reader function
def read_json(filePath):
    with open(filePath) as file:
        data = json.load(file)
        for row in data:
            print(row)


# Write to json
def write_json(filePath):
    with open(filePath, "w") as file:  # Cannot Append data
        data = [{"name": "Yasir"}]
        json.dump(data, file, indent=4)


# Binary Read


def read_image(filePath):
    with open(filePath, "rb") as file:
        read = file.read()
        print(read)


path = Path("day_03/data/sample_data.json")
print(path.exists())
if path.exists():
    write_json(path)
    read_json(path)

path = Path("data/yasir.jpeg")
print(path.exists())
if path.exists():
    read_image(path)


