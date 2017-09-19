import backend
import frontend

lb = backend.Logbook()

#lb.create_entry("Test text.", ["test tag"])
lb.recent_entries("test tag",10)