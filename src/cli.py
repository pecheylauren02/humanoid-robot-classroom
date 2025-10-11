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

    print("\nHello, Teacher! I am your Humanoid Classroom Robot, ready to assist you today.")
    print("\nI can help with tasks like delivering items, monitoring classroom temperature, and greeting students.")
    input("\nPress ENTER to see my command list...")

    print(COMMANDS_GUIDE)

    print("All set! Type a command and I’ll get right to work:\n")

    while True:
        try:
            cmd = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nIt seems you’re leaving. Goodbye, Teacher!")
            break

        if not cmd:
            continue

        parts = cmd.split()
        verb = parts[0].lower()

        if verb == "exit":
            confirm = input("\nTeacher, are you sure you want me to power down? (y/n): ").strip().lower()
            if confirm in ["y", "yes"]:
                print("\nMission complete, Teacher! I’m going to recharge. See you next time! 🤖👋")
                break
            else:
                print("\nPhew! I’m still here, ready for your next command.")
                continue

        elif verb == "help":
            print("\nHere’s what I can do for you, Teacher:")
            print(COMMANDS_GUIDE)

        elif verb == "deliver" and len(parts) >= 4:
            item = parts[1]
            from_loc = parts[2]
            to_loc = " ".join(parts[3:])
            result = robot.deliver_material(item, from_loc, to_loc)
            if "Delivered" in result:
                print(f"\nAll done, Teacher! I successfully delivered {item} from {from_loc} to {to_loc}.")
            else:
                print(f"\nOops, Teacher! I couldn’t deliver {item}. Please check the locations and try again.")

        elif verb == "monitor":
            res = robot.monitor_environment()
            temp = res.get('temperature')
            issue = res.get('issue')
            if issue:
                print(f"\nAlert, Teacher! The classroom temperature is {temp}°C — outside my safe range.")
            else:
                print(f"\nThe classroom temperature is {temp}°C. Everything is normal for students to learn in optimal conditions!")

        elif verb == "greet" and len(parts) >= 2:
            name = " ".join(parts[1:])
            greeting = robot.greet_student(name)
            print(f"\nAffirmative: {greeting}")

        elif verb == "status":
            status = robot.get_status()
            state = status.get('state', 'unknown')
            tasks = status.get('task_queue', [])
            print(f"\nCurrent Status: {state}")
            if tasks:
                print("Here are my pending tasks:")
                for t in tasks:
                    print(f"  - {t}")
            else:
                print("No pending tasks. I’m all clear!")

        elif verb == "undo":
            last = robot.interaction.undo_last()
            if last:
                action, who = last
                print(f"\nTeacher, I undid my last action: {action} for {who or 'robot'}.")
            else:
                print("\nNothing to undo, Teacher. All is up to date!")

        else:
            print("\nOops, Teacher! I didn’t understand that command. Type 'help' to see what I can do.")

if __name__ == "__main__":
    main()
