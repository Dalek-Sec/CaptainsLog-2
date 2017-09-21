# Built in
import shutil
import time
# Installed
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style

def get_session_tags(lb):
    tags = []
    while True:
        width, height = shutil.get_terminal_size()
        print("\n"*height)
        recent_tag_sets = lb.get_recent_tag_sets(10)
        for index, tag_set in enumerate(recent_tag_sets):
            print("["+str(index)+"]:" + str(tag_set))
        print("Selected tags: " + str(tags))
        tag_input = input("Enter tag, tag set number, or return empty to continue: ")
        if tag_input.isdigit():
            try:
                tags += recent_tag_sets[int(tag_input)]
            except IndexError:
                print("Number is outside of range listed")
        elif tag_input == "":
            break
        else:
            tags.append(tag_input)

        tags = list(set(tags))
    
    return tags

def display_log_screen_prompt(lb, tags):
    width, height = shutil.get_terminal_size()
    print("\n"*height)
    # Print previous entries
    recent_entries = lb.recent_entries(tags, height)[::-1]
    for index, entry in enumerate(recent_entries):
        if index == 0 or time.strftime("%x", time.localtime(entry["time"])) != time.strftime("%x", time.localtime(recent_entries[index-1]["time"])):
            print(Fore.LIGHTMAGENTA_EX+("{:-^"+str(width-1)+"}").format(time.strftime("%A, %B %d, %Y", time.localtime(entry["time"]))))
        id_text = Fore.LIGHTBLACK_EX+(Style.BRIGHT if index%2==0 else Style.NORMAL)+str(entry["id"])
        time_text = ("%s[%s" + time.strftime("%H:%M:%S", time.localtime(entry["time"])) + "%s]") % (Fore.GREEN, Fore.LIGHTMAGENTA_EX, Fore.GREEN)
        entry_text = Fore.WHITE+entry["text"]
        print(id_text+time_text+entry_text)

    entry_input = input("Enter entry, or ctrl+c for commands: ")
    return entry_input

