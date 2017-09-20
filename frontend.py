def get_session_tags(lb):
    print(lb.get_recent_tag_sets(5))

    tags = []
    while True:
        tag_input = input("Enter tag, or return empty to continue: ")
        tags.append(tag_input)
    
    return tags

def display_log_screen_prompt(lb, tags):
    pass