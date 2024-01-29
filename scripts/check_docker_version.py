#/usr/bin/env python3
import json
import re
import subprocess
from typing import Tuple


DOCKER_MIN_VERSION: str = '19.03.0+'


def version_to_int(v: str) -> Tuple[int, int, int]:
    return tuple(map(int, re.sub(r'[^\d.]', '', v).split('.')))


def get_docker_version() -> str:
    try:
        res = json.loads(subprocess.check_output([
            'docker',
            'version',
            '-f',
            'json',
        ]))
        return res['Server']['Version']
    except Exception as err:
        print(f'Exception encoutered when fetching docker version:\n{err}')


def docker_update_needed() -> bool:
    current_version = get_docker_version()
    for a, b in zip(version_to_int(current_version), version_to_int(DOCKER_MIN_VERSION)):
        if a > b:
            return False
        if a < b:
            return True
    return False


def main() -> None:
    exit(1 if docker_update_needed() else 0)


if __name__ == '__main__':
    main()
