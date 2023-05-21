import os
import shutil
import sys

ROOT_PATH = os.path.abspath(os.sep)
FILE_PATH = os.path.dirname(__file__)
DESTINATION_PATH = ""

all_ebook_formats = [".epub", ".pdf", ".mobi", ".ibooks"]


def add_extra_file_types():
    file_type = input("Enter the file type.\n>>>")
    file_type = f".{file_type}"
    all_ebook_formats.append(file_type)
    main_app()


def walk_through_files(path, dest_path):
    """Walk through a given path and find files matching the file_extension
    match"""
    print("Scanning for the following files: ")
    print(all_ebook_formats)
    for (dirpath, dirname, filenames) in os.walk(path):
        for filename in filenames:
            for file_ext in all_ebook_formats:
                if filename.endswith(file_ext):
                    try:
                        shutil.copy(os.path.join(dirpath, filename), dest_path)
                    except Exception as ex:
                        print(ex)


def main_app():
    print("Choose one of the following options:")
    print("1. Scan for Ebooks")
    print("2. Add new Ebook file type.")
    print("q. Exit programs.")
    choice = input(">>> ")
    if choice == "1":
        walk_through_files(ROOT_PATH, DESTINATION_PATH)
        print(f"All Ebooks found have been saved to: {DESTINATION_PATH}")
    elif choice == "2":
        add_extra_file_types()
    elif choice == "q":
        sys.exit()
    elif choice != "1" or choice != "2" or choice != "q":
        print("Invalid choice.\nTry Again.\n>>>")
        main_app()


if __name__ == "__main__":
    print("This tool will scan your computer for any ebook files.")
    DESTINATION_PATH = input("Enter the full destination path..\n>>>")

    while True:
        main_app()
