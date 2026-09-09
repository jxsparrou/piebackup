# This will be the BackupManager object. I think it will hold the list of files to be backed up
# as well as some basic methods for managing the backup process.

import zipfile, pathlib
from backupitem import BackupItem


class BackupManager:
    def __init__(self):
        self.items = []


    def add_item(self, item:BackupItem):
        self.items.append(item)

    def remove_item(self, item:BackupItem):
        self.items.remove(item)

    def list_items(self):
        return self.items

    def validate_items(self):
        pass

    def create_backup(self):
        with zipfile.ZipFile
