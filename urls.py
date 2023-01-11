import os

from django.urls import path, include

from settings import WEBSITE_FOLDER as website


def add_path(file_path: str) -> None:
    print(file_path)
    route = file_path.replace(website, "")
    route = route.replace("__init__", "").replace(".py", "")
    route = route.replace("\\", " ").strip().replace(" ", "/")
    name = file_path.replace("\\", ".").replace(".py", "")
    view = include(name)
    name = name.replace(f"{website}.", "").replace("__init__", "index")
    print(f"route='{route}'\n"
          f"view={view}\n"
          f"name='{name}'\n")
    urlpatterns.append(path(route, view, name=name))


def load(dir_path: str) -> None:
    for file in os.listdir(dir_path):
        if not file.startswith("_") or file == "__init__.py":
            file_path = os.path.join(dir_path, file)
            if os.path.isdir(file_path):
                load(file_path)
            elif os.path.isfile(file_path):
                add_path(file_path)


urlpatterns = []
load(website)
