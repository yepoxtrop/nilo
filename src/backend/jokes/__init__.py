from .open_explorer import Explorer
from .keyboard import KeyboardCommand
from .ip_adress import Ip_Address
from .take_photo import Camera
from .exec_random_apps import RandomApp

JOKES = (
    Explorer.open_explorer,
    Explorer.stop_explorer,
    KeyboardCommand.tab_loop,
    KeyboardCommand.move_window,
    KeyboardCommand.min_view,
    KeyboardCommand.min_win,
    KeyboardCommand.virtual_keyboard,
    KeyboardCommand.configure,
    KeyboardCommand.zoom_view,
    KeyboardCommand.query_random,
    KeyboardCommand.fls_tree,
    Ip_Address.my_public_ip,
    Camera.open_camera,
    Camera.take_photo,
    Camera.take_screen_shot,
    RandomApp.calculator,
    RandomApp.explorer,
    RandomApp.notepad_system32,
    RandomApp.notepad_windows,
    RandomApp.notepad_windows_apps,
    RandomApp.command_prompt,
    RandomApp.powershell,
    RandomApp.control_panel,
    RandomApp.network_adapters,
    RandomApp.paint,
    RandomApp.camera,
    RandomApp.chrome,
    RandomApp.edge,
    RandomApp.firefox,
    RandomApp.opera,
    RandomApp.brave,
    RandomApp.steam,
    RandomApp.vscode,
    RandomApp.mysql_workbench,
)

__all__ = [
    "Explorer",
    "KeyboardCommand",
    "Ip_Address",
    "Camera",
    "RandomApp",
    "JOKES",
]
