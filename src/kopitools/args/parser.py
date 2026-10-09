from typing import Any
import sys

class Parser:
    def __init__(self):
        self.options  = {}
        self.commands = {}
        self.argv = sys.argv

    def option(
        self,
        name: str,
        receives: Any,
        default: Any,
    ):
        pass

    def command(
        self,
        name: str,
    ):
        pass

    def collect(self) -> dict[str, Any]:
        pass
