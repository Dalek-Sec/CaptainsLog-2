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
        self.check_tags(tags)
        entry_id = self.logs.find_one(text=text, time=time)["id"]
        for tag in tags:
            tag_id = self.tags.find_one(name=tag)["id"]
            self.logs_to_tags.insert(dict(entry_id=entry_id, tag_id=tag_id))

    def check_tags(self, tags, create_if_missing=True):
        all_tags_existed = True
        for tag in tags:
            if self.tags.find_one(name=tag) is None:
                all_tags_existed = False
                if create_if_missing is True:
                    self.tags.insert(dict(name=tag))

        return all_tags_existed

    def recent_entries(self, tags, quantity): # TODO: Learn how to properly use junction tables
        entries = []
        all_recent_entries = self.logs.find(order_by=["-time"])
        for entry in all_recent_entries:
            print("----")
            entry_to_tags = self.logs_to_tags.find(entry_id=entry["id"])
            entry_tags = [self.tags.find_one(id=tag["id"])["name"] for tag in entry_to_tags]
            print(entry_tags)
            #if set()
            if len(entries) >= quantity:
                break
