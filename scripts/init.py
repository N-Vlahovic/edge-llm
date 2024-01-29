import os
from pathlib import Path


SCRIPTS_PATH: Path = Path(os.path.abspath(__file__)).parent
DOTENV_FILE: Path = SCRIPTS_PATH.parent.joinpath('.env')


def dotenv_exists() -> bool:
    return os.path.isfile(DOTENV_FILE)


def create_dotenv(
    default_port_llm: 8000,
    default_port_webui: 3000,
) -> None:
    def helper(prompt: str, default: int) -> str:
        p = default
        try:
            p = int(input(f'{prompt} Port [default={default}]:\t'))
        except (TypeError, ValueError):
            pass
        return f'{prompt}_PORT={p}'

    port_llm = helper('LLM', default_port_llm)
    port_webui = helper('WEBUI', default_port_webui)

    with open(DOTENV_FILE, 'a') as f:
        f.write(port_llm)
        f.write(port_webui)

def main() -> None:
    if not dotenv_exists():
        create_dotenv()



if __name__ == '__main__':
    main()
