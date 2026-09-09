from backupitem import BackupItem


def main():
    print("Hello from piebackup!")

    first_item = BackupItem("/home/john/Projects/bootdev/piebackup/piebackup/backupfiles/mobydick.txt")
    second_item = BackupItem("/home/john/Projects/bootdev/piebackup/piebackup/backupfiles/testdir/")


    print(f"the file is {first_item.size} big")
    print(f"it is a {first_item.item_extension} type file.")

    if first_item.is_dir():
        print("This is a directory")
    else:
        print("Its not a directory")

    if first_item.is_file():
        print("It is a file")
    else:
        print("it is not a file.")


    print(f"the second file is: a directory ({second_item.is_dir()}), is a file ({second_item.is_file
        ()}, and it is {second_item.size} bytes big.")


if __name__ == "__main__":
    main()
