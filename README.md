# piebackup
The backup tool that I am designing for a bootdev project. We'll see how it goes.

I will attempt to be doing this with python. This is a learning project that I hope to expand in the future. 

## Goals for a boot.dev submission
- accept files and directories through CLI
- maintain a list of things that need to be backed up
- let the user review/remove items in the list
- choose a backup name and destination
- create a zip archive of the list of backed up items
- create a report of the successes and failures that happen along the way

## 1 - first steps?
I think I am going to treat this like a journal for my ideas and plans and notes, etc. 

Lets start with the backup manager logic. We'll have it as its own object. Each object should probably have its own file.

BackupManager - object that manages the backup process. This object should hold the list of items to be backed up as well as some of the basic methods for managing the backup process.

BackupManager
├── items
├── add_item()
├── remove_item()
├── list_items()
├── validate_items()
└── create_backup()

BackupItem
├── path
├── exists()
├── is_file()
├── is_directory()
└── size()

BackupItem - object that represents the item to be backed up. Might contain some metadata about the item, such as its name, size, and last modified date; but I am undecided on how to approach this.


note for me: run uv sync on the other computer to update the venv virt environment
