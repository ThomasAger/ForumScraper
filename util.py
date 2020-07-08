import numpy as np

def write1dArray(array, name, encoding=None):
    file = open(name, "w", encoding="utf-8")
    for i in range(len(array)):
        file.write(str(array[i]) + "\n")
    file.close()

def importStringArray(file_name, file_type="s", encoding=None):
    with open(file_name, "r", encoding="utf-8") as infile:
        if file_type == "f":
            array = []
            lines = infile.readlines()
            for line in lines:
                array.append(float(line.strip()))
        elif file_type == "i":
            array = [int(float(line.strip())) for line in infile]
        else:
            array = [line.strip() for line in infile]
    return np.asarray(array)