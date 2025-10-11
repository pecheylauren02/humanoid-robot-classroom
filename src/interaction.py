"""
Interaction Module for Humanoid Classroom Robot
------------------------------------------------
Handles user and robot interactions, logging, and undo functionality.

Classes:
    - InteractionModule: Manages interaction logs, displays messages, 
      records actions, and allows undoing the last interaction.

Key Features:
    - Logging actions performed by or for the robot
    - Returning messages to display to users
    - Undoing the most recent interaction
    - Retrieving full interaction history
    - Optional verbose/debug mode for developers
"""

from typing import List, Tuple, Optional


class InteractionModule:
    """
    Manages robot-user interactions and logs actions.

    Attributes:
        id (str): Identifier for this interaction module instance.
        interaction_log (List[Tuple[str, Optional[str]]]): History of all actions.
        undo_stack (List[Tuple[str, Optional[str]]]): Stack for undoable actions.
        verbose (bool): If True, prints debug messages for developers.
    """

    def __init__(self, id_: str, verbose: bool = False):
        self.id = id_
        self.verbose = verbose
        self.interaction_log: List[Tuple[str, Optional[str]]] = []
        self.undo_stack: List[Tuple[str, Optional[str]]] = []

    def display_message(self, message: str) -> str:
        """
        Prepare a message from the robot to show to the user.

        Args:
            message (str): Text message.

        Returns:
            str: Formatted message for display.
        """
        return f"Robot: {message}"

    def log_interaction(self, action: str, who: Optional[str] = None) -> None:
        """
        Record an action in the logs and undo stack.

        Args:
            action (str): Description of the action.
            who (Optional[str]): Who performed or received the action.
        """
        self.interaction_log.append((action, who))
        self.undo_stack.append((action, who))
        if self.verbose:
            print(f"[InteractionModule] logged: {action} {who or 'robot'}")

    def undo_last(self) -> str:
        """
        Undo the most recent logged action.

        Returns:
            str: Friendly message describing what was undone.
        """
        if not self.undo_stack:
            return "Nothing to undo."
        action, who = self.undo_stack.pop()
        self.interaction_log.append(("undo", who))
        if self.verbose:
            print(f"[InteractionModule] undo: {action} {who or 'robot'}")
        return f"Undid last action: {action} for {who or 'robot'}"

    def get_log(self) -> List[Tuple[str, Optional[str]]]:
        """
        Retrieve the interaction log.

        Returns:
            List[Tuple[str, Optional[str]]]: Copy of all logged interactions.
        """
        return self.interaction_log.copy()
