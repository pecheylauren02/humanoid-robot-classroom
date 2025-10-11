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

COMMANDS_GUIDE = """
Commands Guide:

1. Ask the robot to deliver an item
   Command: deliver <item> from <source> to <destination>

2. Check classroom temperature
   Command: monitor

3. Robot greets a student
   Command: greet <name>

4. Check what the robot is doing
   Command: status

5. Undo the last task the robot did
   Command: undo

6. Quit the program
   Command: exit

Type 'help' anytime to see this guide again.
"""

def main():
    robot = RobotController("R-001")
    robot.start()

    print("\nWelcome to the Humanoid Classroom Robot System!\n")
    input("Press ENTER to continue...")

    print("\nThis robot can help you with classroom tasks like delivering items, monitoring the environment, and greeting students.")
    input("\nPress ENTER to see the commands...")

    print(COMMANDS_GUIDE)

    print("\nGreat! Now you can type a command to get started:")

    while True:
        try:
            cmd = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting CLI. Goodbye!")
            break

        if not cmd:
            continue

        parts = cmd.split()
        verb = parts[0].lower()

        if verb == "exit":
            print("Exiting CLI. Goodbye!")
            break

        elif verb == "help":
            print(COMMANDS_GUIDE)

        elif verb == "deliver" and len(parts) >= 4:
            item = parts[1]
            from_loc = parts[2]
            to_loc = " ".join(parts[3:])
            result = robot.deliver_material(item, from_loc, to_loc)
            print(f"\nDELIVERED {item} from {from_loc} to {to_loc}." if result else f"FAILED TO DELIVER {item}.")

        elif verb == "monitor":
            res = robot.monitor_environment()
            temp = res.get('temperature')
            issue = res.get('issue')
            if issue:
                print(f"\nWARNING! Classroom temperature is {temp}°C — outside normal range.")
            else:
                print(f"\nClassroom temperature is {temp}°C. Everything is normal.")

        elif verb == "greet" and len(parts) >= 2:
            name = " ".join(parts[1:])
            print(f"\nRobot says: {robot.greet_student(name)}")

        elif verb == "status":
            status = robot.get_status()
            # Display key info in readable form
            tasks = status.get('tasks', [])
            state = status.get('state', 'unknown')
            print(f"Robot state: {state}")
            if tasks:
                print("Current tasks:")
                for t in tasks:
                    print(f"  - {t}")
            else:
                print("No current tasks.")

        elif verb == "undo":
            last = robot.interaction.undo_last()
            if last:
                action, who = last
                print(f"\nUndid last task: {action} for {who or 'robot'}")
            else:
                print("\nNothing to undo.")

        else:
            print("Unknown or malformed command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
