from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json


class MyHandler(FileSystemEventHandler):
    i = 1

    def on_modified(self, event):
        path_entries = os.listdir(folder_to_track)
        path_files, path_folders = [], []

        for entry in path_entries:
            if '.' in entry:
                path_files.append(entry)
            elif '.' not in entry:
                path_folders.append(entry)

        if 'pdfs' not in os.listdir(folder_destination):
            os.mkdir(folder_destination + "/pdfs")

        for filename in path_files:
            src = folder_to_track + "/" + filename
            new_dest = folder_destination + "/pdfs/" + filename
            os.rename(src, new_dest)


folder_to_track = 'C:/Users/Akshat/Desktop/my_folder'
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
