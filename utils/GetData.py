import csv


def get_data(path):
    file = open(path, "r")
    reader = csv.reader(file)
    next(reader, None)
    rows=[]
    for row in reader:
        rows.append(row)

    return rows



