import os

note_file = os.path.join("../data", "notes.txt")


def get_actionInput(actionInput):
    print("actionnnn: ", actionInput)


def save_note(note):
    if not os.path.exists(note_file):
        open(note_file, "w")

    with open(note_file, "a") as f:
        f.writelines([note + "\n"])

    return "note Saved"
