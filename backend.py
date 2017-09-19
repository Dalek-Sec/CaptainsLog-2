# Libraries
import time
import dataset
# Internal modules
import config

class Logbook:
    def __init__(self, database_url=config.database_url):
        # Initailize database
        self.captainslogs_db = dataset.connect(database_url)
        self.logs = self.captainslogs_db["logs"]
        self.tags = self.captainslogs_db["tags"]
        self.logs_to_tags = self.captainslogs_db["logs_to_tags"]
        
    def create_entry(self, text, tags, time=time.time()): # TODO: Implement proper use of transactions
        # Create entry
        self.logs.insert(dict(text=text, time=time))
        # Generate tags to entry
        entry_id = self.logs.find_one(text=text, time=time)["id"]
        for tag in tags:
            self.logs_to_tags.insert(dict(entry_id=entry_id, tag=tag))

    def recent_entries(self, tags, quantity): # TODO: Learn how to properly use junction tables
        entries = []
        all_recent_entries = self.logs.find(order_by=["-time"])
        for entry in all_recent_entries:
            print("----")
            entry_tags = [row["tag"] for row in self.logs_to_tags.find(entry_id=entry["id"])]
            print(entry_tags)
            print(set(tags) - set(entry_tags))
            if set(tags) - set(entry_tags) == set():
                entries.append(entry)
            if len(entries) >= quantity:
                break

        print("Ret")
        return entries
