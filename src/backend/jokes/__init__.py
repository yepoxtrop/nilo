from .open_explorer import Explorer
from .keyboard import KeyboardCommand
from .ip_adress import Ip_Address
from .take_photo import Camera
from .exec_random_apps import RamdomApps

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
    RamdomApps.calculator,
    RamdomApps.explorer,
    RamdomApps.notepad_system32,
    RamdomApps.notepad_windows,
    RamdomApps.notepad_windows_apps,
    RamdomApps.command_prompt,
    RamdomApps.powershell,
    RamdomApps.control_panel,
    RamdomApps.network_adapters,
    RamdomApps.paint,
    RamdomApps.camera,
    RamdomApps.chrome,
    RamdomApps.edge,
    RamdomApps.firefox,
    RamdomApps.opera,
    RamdomApps.brave,
    RamdomApps.steam,
    RamdomApps.vscode,
    RamdomApps.mysql_workbench,
)

__all__ = [
    "Explorer",
    "KeyboardCommand",
    "Ip_Address",
    "Camera",
    "RamdomApps",
    "JOKES",
]
