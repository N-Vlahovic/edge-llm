#/usr/bin/env python3
import json
import os
import re
from pathlib import Path
import subprocess
from typing import Tuple


DOCKER_MIN_VERSION: str = '19.03.0+'
SCRIPTS_PATH: Path = Path(os.path.abspath(__file__)).parent
DOCKER_UPDATE_FILE: Path = SCRIPTS_PATH.joinpath('update_docker.sh')


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


def run_rocker_update_script() -> int:
    subprocess.run(['sudo', 'bash', DOCKER_UPDATE_FILE])


def main() -> None:
    if docker_update_needed():
        print('updating docker')
        run_rocker_update_script()
    else:
        print('docker already up to date')


if __name__ == '__main__':
    main()
