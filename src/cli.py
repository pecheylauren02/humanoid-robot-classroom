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
    - Task log viewing
"""

from .robot_controller import RobotController

# --- ANSI color codes ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

COMMANDS_GUIDE = f"""
Commands Guide:

1. Ask the robot to deliver an item
   {YELLOW}COMMAND{RESET}: {GREEN}deliver <item> from <source> to <destination>{RESET}

2. Check classroom temperature
   {YELLOW}COMMAND{RESET}: {GREEN}monitor{RESET}

3. Robot greets a student
   {YELLOW}COMMAND{RESET}: {GREEN}greet <name>{RESET}

4. Check what the robot is doing
   {YELLOW}COMMAND{RESET}: {GREEN}status{RESET}

5. Undo the last task the robot did
   {YELLOW}COMMAND{RESET}: {RED}undo{RESET}

6. View recent robot tasks
   {YELLOW}COMMAND{RESET}: {GREEN}view log{RESET}

7. View all robot tasks
   {YELLOW}COMMAND{RESET}: {GREEN}view full log{RESET}

8. Quit the program
   {YELLOW}COMMAND{RESET}: {RED}exit{RESET}

Type {CYAN}'help'{RESET} anytime to see this guide again.
"""


def main():
    robot = RobotController("R-001")
    robot.start()

    print(f"\n🤖{YELLOW} Hello{RESET} Teacher, and welcome! I am your {GREEN}HUMANOID CLASSROOM ROBOT{RESET}, ready to assist you today.")

    teacher_name = input("\nBefore we begin, please tell me your name, Teacher: ").strip().title()
    if not teacher_name:
        teacher_name = "Teacher"
    print(f"\nWonderful to meet you, {CYAN}{teacher_name}{RESET}! I am fully operational and eager to help in your classroom.")
    print(f"\nI can assist with tasks like {GREEN}delivering items{RESET}, {RED}monitoring classroom temperature{RESET}, and {YELLOW}greeting students{RESET}.")

    input("\nPress ENTER to see my command list...")

    print(COMMANDS_GUIDE)
    print(f"\nAll set, {CYAN}{teacher_name}{RESET}! Type a command and I will get right to work:\n")

    while True:
        try:
            cmd = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\nIt seems you are leaving, {CYAN}{teacher_name}{RESET}. I hope I was able to help you! Goodbye 👋")
            break

        if not cmd:
            continue

        parts = cmd.split()
        verb = parts[0].lower()

        if verb == "exit":
            confirm = input(f"\n{CYAN}{teacher_name}{RESET}, are you sure you want me to power down? (y/n): ").strip().lower()
            if confirm in ["y", "yes"]:
                print(f"\nMission complete, {CYAN}{teacher_name}{RESET}! I’m going to recharge. See you next time! 🤖⚡\n")
                break
            else:
                print(f"\nPhew! I am still here. Ready for your next command!\n")
                continue

        elif verb == "help":
            print(f"\nHere is what I can do for you, {CYAN}{teacher_name}{RESET}:")
            print(COMMANDS_GUIDE)

        elif verb == "deliver" and "from" in parts and "to" in parts:
            from_index = parts.index("from") + 1
            to_index = parts.index("to")
            item = parts[1]
            from_loc = " ".join(parts[from_index:to_index])
            to_loc = " ".join(parts[to_index + 1:])
            result = robot.deliver_material(item, from_loc, to_loc)

            # --- Updated delivery feedback logic ---
            if "Delivered" in result:
                print(f"\nAll done, {CYAN}{teacher_name}{RESET}! I successfully delivered {item} from {from_loc} to {to_loc}. 📦✅\n")
            elif "cannot deliver" in result:
                # Forbidden item
                print(f"\n{RED}WARNING{RESET}, {CYAN}{teacher_name}{RESET}! {result}\n")
            elif "failed" in result:
                # Random failure with reason
                print(f"\nOops, {CYAN}{teacher_name}{RESET}! {result}\n")
            else:
                # General fallback (should rarely happen)
                print(f"\nHmm, something unexpected happened with that delivery, {CYAN}{teacher_name}{RESET}. Let's try again.\n")

        elif verb == "monitor":
            res = robot.monitor_environment()
            temp = res.get('temperature')
            issue = res.get('issue')
            if issue:
                print(f"\n{RED}⚠️ ALERT{RESET}, {CYAN}{teacher_name}{RESET}! The classroom temperature is {RED}{temp}{RESET}°C — outside my safe range.\n")
            else:
                print(f"\nThe classroom temperature is {GREEN}{temp}{RESET}°C. Everything is optimal for learning, {CYAN}{teacher_name}{RESET}!\n")

        elif verb == "greet" and len(parts) >= 2:
            name = " ".join(parts[1:])
            greeting = robot.greet_student(name)
            print(f"\nAbsolutely: {greeting}\n")

        elif verb == "status":
            status = robot.get_status()
            state = status.get('state', 'unknown')
            tasks = status.get('task_queue', [])
            print(f"\nCurrent Status, {CYAN}{teacher_name}{RESET}: {state}")
            if tasks:
                print("Here are my pending tasks:")
                for t in tasks:
                    print(f"  - {t}")
            else:
                print("\nNo pending tasks. I am all clear and ready for the next instruction!\n")

        elif verb == "undo":
            last = robot.interaction.undo_last()
            if last:
                action, who = last
                print(f"\n{CYAN}{teacher_name}{RESET}, I undid my last action: {action} for {who or 'robot'}.")
            else:
                print(f"\nNothing to undo right now, {CYAN}{teacher_name}{RESET}. Everything’s up to date!\n")

        # --- NEW: View recent task log ---
        elif verb == "view" and len(parts) >= 2 and parts[1].lower() == "log":
            print("\n--- Last 5 Robot Tasks ---")
            if robot.task_log:
                for entry in robot.task_log[-5:]:
                    print(entry)
            else:
                print("No tasks logged yet.")
            print("-------------------------\n")

        # --- NEW: View full task log ---
        elif verb == "view" and len(parts) >= 3 and parts[1].lower() == "full" and parts[2].lower() == "log":
            print("\n--- Full Robot Task Log ---")
            if robot.task_log:
                for entry in robot.task_log:
                    print(entry)
            else:
                print("No tasks logged yet.")
            print("--------------------------\n")

        else:
            print(f"\nOops! I did not understand that command. Type 'help' to see what I can do.\n")


if __name__ == "__main__":
    main()
