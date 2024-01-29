#/usr/bin/env python3
import argparse
import subprocess


LLM_SERVICE_NAME: str = 'ollama'

parser = argparse.ArgumentParser()
parser.add_argument(
    '--model',
    '-m',
    required=True,
    type=str,
    help='The model for ollama to pull.',
)
args = parser.parse_args()


def pull_model(model: str) -> None:
    subprocess.run([
        'docker',
        'exec',
        '-it',
        LLM_SERVICE_NAME,
        'ollama',
        'pull',
        model,
    ])


def main() -> None:
    model = args.model
    pull_model(model)


if __name__ == '__main__':
    main()
