from datetime import datetime
from pathlib import Path
import sys
import traceback
from types import TracebackType


class Logs:
    @staticmethod
    def error(
        context: str,
        error: BaseException | None = None,
        error_traceback: TracebackType | None = None,
    ) -> None:
        if getattr(sys, "frozen", False):
            project_root = Path(sys.executable).resolve().parent
        else:
            project_root = Path(__file__).resolve().parents[3]

        log_directory = project_root / "log"
        log_directory.mkdir(parents=True, exist_ok=True)

        lines = [
            f"[{datetime.now().astimezone().isoformat(timespec='seconds')}] ERROR",
            context,
        ]
        if error is not None:
            lines.append(
                "".join(
                    traceback.format_exception(
                        type(error),
                        error,
                        error_traceback or error.__traceback__,
                    )
                ).rstrip()
            )

        (log_directory / "raven.log").write_text(
            "\n".join(lines) + "\n",
            encoding="utf-8",
        )
