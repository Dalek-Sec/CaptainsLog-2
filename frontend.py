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
    
    return tags

def display_log_screen_prompt(lb, tags):
    pass