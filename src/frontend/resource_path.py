import sys
from pathlib import Path


def resource_path(*parts: str) -> Path:
    base_path = Path(
        getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[2])
    )
    return base_path.joinpath(*parts)
