from pathlib import Path

from src.frontend import Interface;
from src.backend.utils.logs import Logs

if __name__ == "__main__":
    try:
        Path("pics").mkdir(exist_ok=True)
        Path("log").mkdir(exist_ok=True)
        app = Interface()
    except Exception as error:
        Logs.error("Falló el inicio de Raven", error)
        raise