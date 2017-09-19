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
        
    def create_entry(self, text, time=time.time()):
        pass

    def recent_entries(self, quantity):
        pass
