def readfile(file_path):
    with open(file_path, "r") as file:
        dna = file.read().replace("\n", " ")  # replace newline with space

    return dna