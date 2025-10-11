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

    print("\n🤖 Hello, Teacher! I am your Humanoid Classroom Robot, ready to assist you today.")
    
    teacher_name = input("\nBefore we begin, please tell me your name, Teacher: ").strip().title()
    if not teacher_name:
        teacher_name = "Teacher"
    print(f"\nWonderful to meet you, {teacher_name}! I am fully operational and eager to help in your classroom.")
    print("\nI can assist with tasks like delivering items, monitoring classroom temperature, and greeting students.")
    
    input("\nPress ENTER to see my command list...")

    print(COMMANDS_GUIDE)
    print(f"\nAll set, {teacher_name}! Type a command and I will get right to work:\n")

    while True:
        try:
            cmd = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\nIt seems you are leaving, {teacher_name}. I hope I was able to help you! Goodbye 👋")
            break

        if not cmd:
            continue

        parts = cmd.split()
        verb = parts[0].lower()

        if verb == "exit":
            confirm = input(f"\n{teacher_name}, are you sure you want me to power down? (y/n): ").strip().lower()
            if confirm in ["y", "yes"]:
                print(f"\nMission complete, {teacher_name}! I’m going to recharge. See you next time! 🤖⚡")
                break
            else:
                print(f"\nPhew! I’m still here. Ready for your next command!")
                continue

        elif verb == "help":
            print(f"\nHere’s what I can do for you, {teacher_name}:")
            print(COMMANDS_GUIDE)

        elif verb == "deliver" and len(parts) >= 4:
            item = parts[1]
            from_loc = parts[2]
            to_loc = " ".join(parts[3:])
            result = robot.deliver_material(item, from_loc, to_loc)
            if "Delivered" in result:
                print(f"\nAll done, {teacher_name}! I successfully delivered {item} from {from_loc} to {to_loc}. 📦✅")
            else:
                print(f"\nOops, {teacher_name}! I couldn’t deliver {item}. Please check the locations and try again.")

        elif verb == "monitor":
            res = robot.monitor_environment()
            temp = res.get('temperature')
            issue = res.get('issue')
            if issue:
                print(f"\n⚠️ Alert, {teacher_name}! The classroom temperature is {temp}°C — outside my safe range.")
            else:
                print(f"\nThe classroom temperature is {temp}°C. Everything is optimal for learning, {teacher_name}!")

        elif verb == "greet" and len(parts) >= 2:
            name = " ".join(parts[1:])
            greeting = robot.greet_student(name)
            print(f"\nAffirmative, {teacher_name}: {greeting}")

        elif verb == "status":
            status = robot.get_status()
            state = status.get('state', 'unknown')
            tasks = status.get('task_queue', [])
            print(f"\nCurrent Status, {teacher_name}: {state}")
            if tasks:
                print("Here are my pending tasks:")
                for t in tasks:
                    print(f"  - {t}")
            else:
                print("No pending tasks. I’m all clear and ready for the next instruction!")

        elif verb == "undo":
            last = robot.interaction.undo_last()
            if last:
                action, who = last
                print(f"\n{teacher_name}, I undid my last action: {action} for {who or 'robot'}.")
            else:
                print(f"\nNothing to undo right now, {teacher_name}. Everything’s up to date!")

        else:
            print(f"\nOops! I didn’t understand that command. Type 'help' to see what I can do.")

if __name__ == "__main__":
    main()
