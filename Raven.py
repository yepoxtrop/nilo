import os

from src.frontend import Interface;

if __name__ == "__main__":
    if not os.path.exists("pics"):
        os.mkdir("pics")
    app = Interface()