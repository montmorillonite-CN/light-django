import sys
import os
import shutil


def copy(file: str) -> None:
    shutil.copyfile(os.path.join(dir_name, file), os.path.join(name, file))


if __name__ == "__main__":
    file_path = sys.argv[0]
    command = sys.argv[1]
    args = sys.argv[2:]
    if command == "new":
        dir_name = os.path.dirname(file_path)
        name = args[0]
        os.mkdir(name)
        os.mkdir(os.path.join(name, "website"))
        copy("run.py")
        copy("settings.py")
        copy("urls.py")
