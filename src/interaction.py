"""
Interaction Module for Humanoid Classroom Robot
------------------------------------------------
Handles user and robot interactions, logging, and undo functionality.

Classes:
    - InteractionModule: Manages interaction logs, displays messages, 
      records actions, and allows undoing the last interaction.

Key Features:
    - Logging actions performed by or for the robot
    - Displaying messages to users or the CLI
    - Undoing the most recent interaction
    - Retrieving full interaction history
"""

from typing import List, Tuple, Optional

class InteractionModule:
    """
    Manages robot-user interactions and logs actions.

    Attributes:
        id (str): Identifier for this interaction module instance.
        interaction_log (List[Tuple[str, str]]): History of all actions.
        undo_stack (List[Tuple[str, str]]): Stack for undoable actions.
    """
    def __init__(self, id_: str):
        self.id = id_
        self.interaction_log: List[Tuple[str, str]] = []
        self.undo_stack: List[Tuple[str, str]] = []

    def display_message(self, message: str) -> None:
        """
        Display a message from the robot.

        Args:
        message (str): Text message to display.
        """
        print(f"[Robot] {message}")

    def get_command(self) -> str:
        # Placeholder for CLI integration — real CLI will call controller directly
        return "noop"
    
    def log_interaction(self, action: str, who: str = "") -> None:
        self.interaction_log.append((action, who))
        self.undo_stack.append((action, who))
        print(f"[InteractionModule] logged: {action} {who}")

    def undo_last(self) -> Optional[Tuple[str, str]]:
        """
        Undo the most recent logged action.

        Returns:
        Optional[Tuple[str, str]]: The undone action and associated actor, or None if no actions to undo.
        """
        if not self.undo_stack:
            return None
        item = self.undo_stack.pop()
        self.interaction_log.append(("undo", item[1]))
        print(f"[InteractionModule] undo: {item}")
        return item

    def get_log(self) -> List[Tuple[str, str]]:
        return list(self.interaction_log)
