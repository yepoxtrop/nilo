import os

from src.frontend import Interface;
from src.backend.utils.logs import Logs

if __name__ == "__main__":
    try:
        if not os.path.exists("pics"):
            os.mkdir("pics")
        if not os.path.exists("log"):
                    os.mkdir("pics")
        app = Interface()
    except Exception as error:
        Logs.error("Falló el inicio de Raven", error)
        raise