# Libraries
import time
import dataset
# Internal modules
import config
import frontend

class Logbook:
    def __init__(self, database_url=config.database_url):
        # Initailize database
        self.captainslogs_db = dataset.connect(database_url)
        self.logs = self.captainslogs_db["logs"]
        self.logs_to_tags = self.captainslogs_db["logs_to_tags"]

    def create_entry(self, text, tags, entry_time): # TODO: Implement proper use of transactions
        # Create entry
        self.logs.insert(dict(text=text, time=entry_time))
        # Generate tags to entry
        entry_id = self.logs.find_one(text=text, time=entry_time)["id"]
        for tag in tags:
            self.logs_to_tags.insert(dict(entry_id=entry_id, tag=tag))

    def recent_entries(self, tags, quantity): # TODO: Learn how to properly use junction tables
        entries = []
        all_recent_entries = self.logs.find(order_by=["-time"])
        for entry in all_recent_entries:
            entry_tags = [row["tag"] for row in self.logs_to_tags.find(entry_id=entry["id"])]
            if set(tags) - set(entry_tags) == set():
                entries.append(entry)
            if len(entries) >= quantity:
                break

        return entries

    def get_recent_tag_sets(self, quantity):
        tag_sets = []
        all_recent_entries = self.logs.find(order_by=["-time"])
        for entry in all_recent_entries:
            tag_set = sorted([row["tag"] for row in self.logs_to_tags.find(entry_id=entry["id"])])
            if not tag_set in tag_sets:
                tag_sets.append(tag_set)
            if len(tag_sets) >= quantity:
                break
        
        print("FINAL: " + str(tag_sets))
        return tag_sets

class Session:
    def __init__(self, logbook=Logbook()):
        self.lb = logbook
        self.session_tags = frontend.get_session_tags(self.lb)
        while True:
            entry_input = frontend.display_log_screen_prompt(self.lb, self.session_tags)
            self.lb.create_entry(entry_input, self.session_tags, time.time())
