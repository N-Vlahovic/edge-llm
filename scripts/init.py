import os
from pathlib import Path


SCRIPTS_PATH: Path = Path(os.path.abspath(__file__)).parent


def dotenv_exists() -> bool:
    return os.path.isfile(SCRIPTS_PATH.parent.joinpath('.env'))


def main() -> None:
    print(dotenv_exists())


if __name__ == '__main__':
    main()
