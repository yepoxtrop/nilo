import os
import subprocess
from pathlib import Path

from ..models.programs import WindowsBasics, WindowsInstalled


class RamdomApps:
    @staticmethod
    def _show_error() -> None:
        error_script = (
            Path(__file__).resolve().parent.parent
            / "utils"
            / "message-error"
            / "message_error7.vbs"
        )
        subprocess.Popen(["cscript", "//nologo", str(error_script)])

    @staticmethod
    def _run_program(program_path: str) -> None:
        path = Path(program_path)
        if not path.is_file():
            RamdomApps._show_error()
            return

        for _ in range(10):
            try:
                if path.suffix.lower() == ".cpl":
                    os.startfile(str(path))
                else:
                    subprocess.Popen([str(path)])
            except OSError:
                RamdomApps._show_error()
                return

    @staticmethod
    def calculator() -> None:
        RamdomApps._run_program(WindowsBasics.CALCULATOR.value)

    @staticmethod
    def explorer() -> None:
        RamdomApps._run_program(WindowsBasics.EXPLORER.value)

    @staticmethod
    def notepad_system32() -> None:
        RamdomApps._run_program(WindowsBasics.NOTEPAD1.value)

    @staticmethod
    def notepad_windows() -> None:
        RamdomApps._run_program(WindowsBasics.NOTEPAD2.value)

    @staticmethod
    def notepad_windows_apps() -> None:
        RamdomApps._run_program(WindowsBasics.NOTEPAD3.value)

    @staticmethod
    def command_prompt() -> None:
        RamdomApps._run_program(WindowsBasics.CMD.value)

    @staticmethod
    def powershell() -> None:
        RamdomApps._run_program(WindowsBasics.POWERSHELL.value)

    @staticmethod
    def control_panel() -> None:
        RamdomApps._run_program(WindowsBasics.CONTROL.value)

    @staticmethod
    def network_adapters() -> None:
        RamdomApps._run_program(WindowsBasics.NETWORK_ADAPTERS.value)

    @staticmethod
    def paint() -> None:
        RamdomApps._run_program(WindowsBasics.PAINT.value)

    @staticmethod
    def camera() -> None:
        RamdomApps._run_program(WindowsBasics.CAMERA.value)

    @staticmethod
    def chrome() -> None:
        RamdomApps._run_program(WindowsInstalled.CHROME.value)

    @staticmethod
    def edge() -> None:
        RamdomApps._run_program(WindowsInstalled.EDGE.value)

    @staticmethod
    def firefox() -> None:
        RamdomApps._run_program(WindowsInstalled.FIREFOX.value)

    @staticmethod
    def opera() -> None:
        RamdomApps._run_program(WindowsInstalled.OPERA.value)

    @staticmethod
    def brave() -> None:
        RamdomApps._run_program(WindowsInstalled.BRAVE.value)

    @staticmethod
    def steam() -> None:
        RamdomApps._run_program(WindowsInstalled.STEAM.value)

    @staticmethod
    def vscode() -> None:
        RamdomApps._run_program(WindowsInstalled.VCODE.value)

    @staticmethod
    def mysql_workbench() -> None:
        RamdomApps._run_program(WindowsInstalled.WORKBENCH.value)
