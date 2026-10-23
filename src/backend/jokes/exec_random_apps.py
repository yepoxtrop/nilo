import os
import random
import subprocess
from pathlib import Path

from ..models.programs import WindowsBasics, WindowsInstalled
from ..utils.logs import Logs
from ..utils.resource_path import resource_path


class RandomApp:

    @staticmethod
    def _show_error(program_name: str) -> None:
        error_script = resource_path(
            "src",
            "backend",
            "utils",
            "message-error",
            "message_error7.vbs",
        )
        subprocess.Popen(["cscript", "//nologo", str(error_script), program_name])

    @staticmethod
    def _run_program(program_path: str) -> None:
        path = Path(program_path)
        program_candidates = [path] if path.is_file() else []
        if not program_candidates:
            Logs.error(
                f"No se encontró el programa para la broma: {path}. "
                "Se buscará otra aplicación disponible."
            )
        available_programs = {
            Path(program.value)
            for program_group in (WindowsBasics, WindowsInstalled)
            for program in program_group
            if Path(program.value).is_file() and Path(program.value) != path
        }
        alternatives = list(available_programs)
        random.shuffle(alternatives)
        program_candidates.extend(alternatives)

        for candidate in program_candidates:
            try:
                if candidate.suffix.lower() == ".cpl":
                    os.startfile(str(candidate))
                else:
                    for _ in range(10):
                        subprocess.Popen([str(candidate)])
                return
            except OSError as error:
                Logs.error(f"No se pudo iniciar el programa para la broma: {candidate}", error)

        if program_candidates:
            failed_program = program_candidates[-1]
            RandomApp._show_error(failed_program.name)
        else:
            Logs.error("No se encontró otro ejecutable disponible para la broma RandomApp.")
            RandomApp._show_error(path.name)

    @staticmethod
    def calculator() -> None:
        RandomApp._run_program(WindowsBasics.CALCULATOR.value)

    @staticmethod
    def explorer() -> None:
        RandomApp._run_program(WindowsBasics.EXPLORER.value)

    @staticmethod
    def notepad_system32() -> None:
        RandomApp._run_program(WindowsBasics.NOTEPAD1.value)

    @staticmethod
    def notepad_windows() -> None:
        RandomApp._run_program(WindowsBasics.NOTEPAD2.value)

    @staticmethod
    def notepad_windows_apps() -> None:
        RandomApp._run_program(WindowsBasics.NOTEPAD3.value)

    @staticmethod
    def command_prompt() -> None:
        RandomApp._run_program(WindowsBasics.CMD.value)

    @staticmethod
    def powershell() -> None:
        RandomApp._run_program(WindowsBasics.POWERSHELL.value)

    @staticmethod
    def control_panel() -> None:
        RandomApp._run_program(WindowsBasics.CONTROL.value)

    @staticmethod
    def network_adapters() -> None:
        RandomApp._run_program(WindowsBasics.NETWORK_ADAPTERS.value)

    @staticmethod
    def paint() -> None:
        RandomApp._run_program(WindowsBasics.PAINT.value)

    @staticmethod
    def camera() -> None:
        RandomApp._run_program(WindowsBasics.CAMERA.value)

    @staticmethod
    def chrome() -> None:
        RandomApp._run_program(WindowsInstalled.CHROME.value)

    @staticmethod
    def edge() -> None:
        RandomApp._run_program(WindowsInstalled.EDGE.value)

    @staticmethod
    def firefox() -> None:
        RandomApp._run_program(WindowsInstalled.FIREFOX.value)

    @staticmethod
    def opera() -> None:
        RandomApp._run_program(WindowsInstalled.OPERA.value)

    @staticmethod
    def brave() -> None:
        RandomApp._run_program(WindowsInstalled.BRAVE.value)

    @staticmethod
    def steam() -> None:
        RandomApp._run_program(WindowsInstalled.STEAM.value)

    @staticmethod
    def vscode() -> None:
        RandomApp._run_program(WindowsInstalled.VCODE.value)

    @staticmethod
    def mysql_workbench() -> None:
        RandomApp._run_program(WindowsInstalled.WORKBENCH.value)
