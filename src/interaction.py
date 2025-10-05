# src/interaction.py
from typing import List, Tuple, Optional

class InteractionModule:
    def __init__(self, id_: str):
        self.id = id_
        self.interaction_log: List[Tuple[str, str]] = []
        self.undo_stack: List[Tuple[str, str]] = []

    def display_message(self, message: str) -> None:
        print(f"[Robot] {message}")

    def get_command(self) -> str:
        # Placeholder for CLI integration — real CLI will call controller directly
        return "noop"
