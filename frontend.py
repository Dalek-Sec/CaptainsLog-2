import shutil

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
    # Print header
    print("\n\n\nDatabase: " + lb.captainslogs_db.url)
    # Print previous entries
    recent_entries = lb.recent_entries(tags, 10)
    for entry in recent_entries:
        print(entry)

    entry_input = input("Enter entry, or ctrl+c for commands: ")
    return entry_input
