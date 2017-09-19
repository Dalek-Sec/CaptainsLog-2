import backend
import frontend

lb = backend.Logbook()

#lb.create_entry("Test text.", ["test tag"])
print(lb.recent_entries(["test tag"],10))