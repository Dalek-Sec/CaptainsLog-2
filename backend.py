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
        self.logs.insert(dict(text=text, time=time))
        self.check_tags(tags)
        entry_id = self.logs.find_one(text=text, time=time)["id"]

    def check_tags(self, tags, create_if_missing=True):
        all_tags_exist = True
        for tag in tags:
            if self.tags.find_one(name=tag) is None:
                all_tags_exist = False
                if create_if_missing is True:
                    self.tags.insert(dict(name=tag))

        return all_tags_exist

    def recent_entries(self, quantity):
        pass
