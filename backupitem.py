# BackupItem - object that represents the item to be backed up.
import pathlib

class BackupItem:
    def __init__(self, file_path: str):
        self.file_path = pathlib.Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"{file_path} not exist, please try again")

        self.item_extension: str = self.file_path.suffix
        if self.file_path.is_dir:
            target_dir = self.file_path
            self.size = 0
            for item in target_dir.glob("*"):
                if item.is_file():
                   self.size += item.stat().st_size
        else:
           self.size = self.file_path.stat().st_size


    def exists(self):
        return self.file_path.exists()

    def is_dir(self):
        return self.file_path.is_dir()

    def is_file(self):
        return self.file_path.is_file()
