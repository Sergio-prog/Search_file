import os
from pathlib import Path
from typing import Union, List


class Search:
    def __init__(self, path: Union[Path, str, os.PathLike]):
        self.path = str(path)

    def search_by_suffix(self, suffix: str, path_object_returns: bool = False) -> List[str]:
        """
        Returns all directories from the specified directory and specified suffix

        Example:
            search = Search(r"C:/Games")

            print(search.search_by_suffix(".db"))


            \>>> 'C:\\Games\\Adobe\\Adobe Premiere Pro 2023\\typesupport\\FntNames.db',

            \>>> 'C:\\Games\\osu!\\collection.db' ...
        """
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

        return correct_paths

    def search_by_name(self, name: str, path_object_returns: bool = False) -> List[str]:
        """
        Returns all directories from the specified directory and specified suffix

        Example:
            search = Search(r"C:/Games")

            print(search.search_by_name("osu!.exe", path_object_returns=False))

            \>>> 'C:\\Games\\osu!\\osu!.exe'
        """
        correct_paths = []
        for rootdir, dirs, files in os.walk(self.path):
            for file in files:
                if Path(file).name == name:
                    goal_path = str(Path(rootdir, file)) if not path_object_returns else Path(rootdir, file)
                    correct_paths.append(goal_path)

        return correct_paths


if __name__ == "__main__":
    from pprint import pprint

    folder = r"D:/Games"  # or Path(r"D:/Games")
    search = Search(folder)
    pprint(search.search_by_suffix(".gif"))
