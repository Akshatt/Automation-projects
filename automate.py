from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json


class MyHandler(FileSystemEventHandler):
    i = 1

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_dest = folder_destination + "/" + filename
            os.rename(src, new_dest)


folder_to_track = 'C:/Users/Akshat/Desktop/Course Certificates - Copy'
folder_destination = 'C:/Users/Akshat/Desktop/new_folder'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
