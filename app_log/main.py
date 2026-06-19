from datetime import datetime
import os


def app_log(message):
    now = datetime.now()
    with open("app_log.txt", "a") as f:
        f.write(f"{now} :- {message}\n")
    
app_log("App started")
app_log("App running")
app_log("App closed")

with open("app_log.txt", "r") as f:
    logs = f.read()
print(logs)


if os.path.exists("app_log.txt"):
    with open("app_log.txt", "r") as f:
        logs = f.read()
    print(logs)
else:
    print(f"{f} is not exist")



