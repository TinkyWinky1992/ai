import os
from datetime import datetime

note_file = os.path.join(".", "notes.txt")


def save_note(note):
    if not os.path.exists(note_file):
        open(note_file, "w")

    with open(note_file, "a") as f:
        f.writelines([note + "\n"])

    return "note Saved"


#def get_current_date_and_time() -> str:
    """Returns the current date and time"""
   # now = datetime.now()
  #  return now.strftime("%m/%d/%Y, %H:%M:%S")
