import os
from datetime import datetime

note_file = os.path.join(".", "notes.txt")


def save_schedule(problem, level):
    # Open the note.txt file in append mode
    if not os.path.exists(note_file):
        open(note_file, "w")

    with open(note_file, "a")as file:
        # Write the appointment details in the desired format
        file.writelines([f"Problem: {problem}\n"])
        file.writelines([f"Level of the problem: {level}\n"])
    return "appointment saved"


#