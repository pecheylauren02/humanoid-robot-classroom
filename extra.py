"""
Humanoid Classroom Robot System
---------------------------------
This implementation reflects the UML Class, Sequence, and Activity Diagrams 
for the Humanoid Classroom Robot System. 

Classes:
    - RobotController
    - TaskManager
    - DeliveryTask
    - SensorModule
    - InteractionModule

Key Features:
    - Delivery task creation, execution, and error handling
    - Temperature monitoring and anomaly detection
    - Interaction logging and greetings
    - State transitions for the RobotController
"""

import json
from .robot_controller import RobotController

def main():
    robot = RobotController("R-001")
    robot.start()
    print("\nWelcome to the Humanoid Classroom Robot System!\n")
    input("Press ENTER to continue...")

    print("\nThis robot can help you with classroom tasks like delivering items, monitoring the environment, and greeting students.")
    input("\nPress ENTER to see the commands...")

    print("""
          Commands Guide:

          1. Ask the robot to deliver an item
          Command: deliver <item> from <source> to <destination>

          2. Check classroom temperature
          Command: monitor

          3. Robot greets a student
          Command: greet <name>

          4. Show what the robot is doing
          Command: status

          5. Undo the last action
          Command: undo

          6. Quit the program
          Command: exit
        """)

    print("\nWelldone, now you know the commands, type one of the commands shown to start:")


    while True:
        try:
            cmd = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting CLI.")
            break
        if not cmd:
            continue
        parts = cmd.split()
        verb = parts[0].lower()
        if verb == "exit":
            break
        if verb == "deliver" and len(parts) >= 4:
            item = parts[1]
            from_loc = parts[2]
            to_loc = " ".join(parts[3:])
            print(robot.deliver_material(item, from_loc, to_loc))
        elif verb == "monitor":
            res = robot.monitor_environment()
            print(res)
        elif verb == "greet" and len(parts) >= 2:
            name = " ".join(parts[1:])
            print(robot.greet_student(name))
        elif verb == "status":
            print(json.dumps(robot.get_status(), indent=2))
        elif verb == "undo":
            undone = robot.interaction.undo_last()
            print("Undid:", undone)
        else:
            print("Unknown or malformed command.")

if __name__ == "__main__":
    main()
