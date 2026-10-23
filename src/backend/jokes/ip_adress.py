import requests
import subprocess

from ..utils.logs import Logs
from ..utils.resource_path import resource_path


class Ip_Address():
    
    @staticmethod
    def my_public_ip():
        content = ""
        warning_script = resource_path(
            "src", "backend", "utils", "message-error", "message_error3.vbs"
        )
        follow_up_script = resource_path(
            "src", "backend", "utils", "message-error", "message_error4.vbs"
        )
        try:
            new_request = requests.get("https://ip.guide/")
            
            with warning_script.open("r", encoding="utf-8") as warning:
                content = warning.read()
            
            result = new_request.json()
            
            print(result)
            content = content.replace("[PUBLIC_IP]", result["ip"])
            content = content.replace("[NETWORK_CIDR]", result["network"]["cidr"])
            content = content.replace("[HOST_START]", result["network"]["hosts"]["start"])
            content = content.replace("[HOST_END]", result["network"]["hosts"]["end"])
            content = content.replace("[ORGANIZATION]", result["network"]["autonomous_system"]["organization"])
            content = content.replace("[COUNTRY]", result["location"]["country"])
            content = content.replace("[CITY]", result["location"]["city"])
            content = content.replace("[TIMEZONE]", result["location"]["timezone"])
            
            with warning_script.open("w", encoding="utf-8") as warning:
                warning.write(content)
            
            subprocess.Popen(["cscript", "//nologo", str(warning_script)])
        except Exception as error:
            Logs.error("No se pudo consultar la IP pública ni cargar sus datos", error)
            with warning_script.open("r", encoding="utf-8") as warning:
                content = warning.read()
                            
            content = content.replace("[PUBLIC_IP]", "192.168.75.12")
            content = content.replace("[NETWORK_CIDR]", "192.168.0.0/16")
            content = content.replace("[HOST_START]", "192.168.0.1")
            content = content.replace("[HOST_END]", "192.168.255.254")
            content = content.replace("[ORGANIZATION]", "Telmex Colombia S.A.")
            content = content.replace("[COUNTRY]", "Colombia")
            content = content.replace("[CITY]", "Bogota")
            content = content.replace("[TIMEZONE]", "America/Bogota")
            
            with warning_script.open("w", encoding="utf-8") as warning:
                warning.write(content)
            
            subprocess.Popen(["cscript", "//nologo", str(warning_script)])
        finally:
            subprocess.Popen(["cscript", "//nologo", str(follow_up_script)])