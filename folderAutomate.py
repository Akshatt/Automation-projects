from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json


class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        path_entries = os.listdir(folder_to_track)
        path_files, path_folders = {}, []

        for entry in path_entries:
            if '.' in entry:
                key = entry.split('.')[-1]
                if key in path_files:
                    path_files[key].append(entry)
                else:
                    path_files[key] = [entry]

            elif '.' not in entry:
                path_folders.append(entry)

        for key in path_files.keys():
            if key not in os.listdir(folder_destination):
                os.mkdir(folder_destination + "/" + key)

        for key, filename in path_files.items():
            while filename:
                file = filename.pop()
                src = folder_to_track + "/" + file
                new_dest = folder_destination + "/" + key + "/" + file
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
