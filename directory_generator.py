from pathlib import Path


class FileHandler:
    def __init__(self, path):
        self._path = Path(path)

    def exists(self):
        if self._path.exists():
            return True
        return False

    def create_files(self, filenames: list):
        self._path.mkdir(parents=True, exist_ok=True)
        for p in filenames:
            _x = Path(self._path / p)
            if _x.exists():
                print(f'File {_x} exists')
                continue
            with open(_x, 'w') as e:
                pass


foo = FileHandler(path='foo/bar')
calibration_files = ['bar.csv', 'foo.csv', 'p.csv', 'asd.csv']
foo.create_files(filenames=calibration_files)


