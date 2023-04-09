import os
from pathlib import Path
from typing import Union, List
from time import time


class Search:
    def __init__(self, path: Union[Path, str, os.PathLike]):
        self.path = str(path)
        self.final = None
        if not os.path.exists(self.path):
            raise FileExistsError("Path is doesn't exist")

    def search_by_suffix(self, suffix: str, path_object_returns: bool = False) -> List[str]:
        """
        Returns all directories from the specified directory and specified suffix

        Example:
            search = Search(r"C:/Games")

            print(search.search_by_suffix(".db"))


            \>>> 'C:\\Games\\Adobe\\Adobe Premiere Pro 2023\\typesupport\\FntNames.db',

            \>>> 'C:\\Games\\osu!\\collection.db' ...
        """
        start = time()

        if not suffix:
            suffix = ""
        else:
            suffix = ("." + suffix).lower() if suffix[0] != "." else suffix.lower()

        correct_paths = []
        for rootdir, dirs, files in os.walk(self.path):
            for file in files:
                if Path(file).suffix == suffix:
                    goal_path = str(Path(rootdir, file)) if not path_object_returns else Path(rootdir, file)
                    correct_paths.append(goal_path)

        end = time()
        self.final = end - start
        return correct_paths

    def search_by_name(self, file_name: str, path_object_returns: bool = False) -> List[str]:
        """
        Returns all directories from the specified directory and specified suffix

        Example:
            search = Search(r"C:/Games")

            print(search.search_by_name("osu!.exe", path_object_returns=False))

            \>>> ['C:\\Games\\osu!\\osu!.exe']
        """
        start = time()

        correct_paths = []
        for rootdir, dirs, files in os.walk(self.path):
            for file in files:
                if Path(file).name == file_name:
                    goal_path = str(Path(rootdir, file)) if not path_object_returns else Path(rootdir, file)
                    correct_paths.append(goal_path)

        end = time()
        self.final = end - start
        return correct_paths

    @property
    def get_last_search_time(self):
        return self.final

    def search_by_size(self, file_size: Union[int, float], round_search_file_size: bool = True,
                       path_object_returns: bool = False) -> List[str]:
        """
        Returns all directories from the specified directory and specified size in bytes

        Example:
            search = Search(r"C:/Games")

            print(search.search_by_size(1024, round_search_file_size=True))

            \>>> 'C:\\Games\\osu!\\osu!.exe'
        """

        start = time()

        correct_paths = []
        for rootdir, dirs, files in os.walk(self.path):
            for file in files:
                search_file = round(
                    os.path.getsize(os.path.join(rootdir, file))) if round_search_file_size else os.path.getsize(
                    os.path.join(rootdir, file))
                if search_file == file_size:
                    goal_path = str(Path(rootdir, file)) if not path_object_returns else Path(rootdir, file)
                    correct_paths.append(goal_path)

        end = time()
        self.final = end - start
        return correct_paths

    def search_by_content(self, file_search_content: str = None, file_search_types: Union[list, set] = ("txt",),
                          path_object_returns: bool = False):
        """
                Returns all directories from the specified directory by content (binary or text content) in file and their type

                Example:
                    search = Search(r"C:/Games")

                    print(search.search_by_content("Hello World!", file_search_types=["txt"]))

                    \>>> 'C:\Games\osu!\Localisation\ru.txt'
                """
        start = time()

        correct_paths = []
        for rootdir, dirs, files in os.walk(self.path):
            for file in files:
                if Path(file).suffix.replace(".", "") in file_search_types:
                    try:
                        file_content = "".join(open(os.path.join(rootdir, file), "r", encoding='utf-8').readlines())
                    except UnicodeDecodeError:
                        file_content = str(open(os.path.join(rootdir, file), "rb").readlines())

                    if file_search_content in file_content:
                        goal_path = str(Path(rootdir, file)) if not path_object_returns else Path(rootdir, file)
                        correct_paths.append(goal_path)

        end = time()
        self.final = end - start
        return correct_paths


if __name__ == "__main__":
    from pprint import pprint

    folder = r"D:/Games"  # or Path(r"D:/Games")
    search = Search(folder)
    print(search.search_by_content("lection"))
