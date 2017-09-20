import shutil
import time

def get_session_tags(lb):
    tags = []
    while True:
        recent_tag_sets = lb.get_recent_tag_sets(10)
        for index, tag_set in enumerate(recent_tag_sets):
            print("["+str(index)+"]:" + str(tag_set))
        print("Current tags: " + str(tags))
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
    print(type(recent_entries))
    for index, entry in enumerate(recent_entries):
        if index == 0 or time.strftime("%x", time.localtime(entry["time"])) != time.strftime("%x", time.localtime(recent_entries[index-1]["time"])):
            print(("{:-^"+str(width)+"}").format(time.strftime("%A, %B %d, %Y", time.localtime(entry["time"]))))
        id_text = str(entry["id"])
        time_text = "[" + time.strftime("%H:%M:%S", time.localtime(entry["time"])) + "]"
        entry_text = entry["text"]
        print(id_text+time_text+entry_text)

    entry_input = input("Enter entry, or ctrl+c for commands: ")
    return entry_input
