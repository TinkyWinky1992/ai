import json


def readfile(file_path):
    with open(file_path, "r") as file:
        dna = file.read().replace("\n", " ")  # replace newline with space

    return dna


def profileFile(username, email, id):
    userdict = {
        "username": username,
        "email": email,
        "id": id
    }
    with open("userdata.json", "w") as outfile:
        json.dump(userdict, outfile, indent=4)

def TakeUserDetails() -> dict:
    with open("userdata.json", 'r') as openfile:
        json_string = openfile.read()
        json_object = json.loads(json_string)
        print(json_object["username"])
    return json_object