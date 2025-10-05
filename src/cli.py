# src/cli.py
from .robot_controller import RobotController

def main():
    robot = RobotController("R-001")
    robot.start()
    print("Commands: deliver <item> <from> <to>, monitor, greet <name>, status, undo, exit")
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
            import json
            print(json.dumps(robot.get_status(), indent=2))
        elif verb == "undo":
            undone = robot.interaction.undo_last()
            print("Undid:", undone)
        else:
            print("Unknown or malformed command.")
if __name__ == "__main__":
    main()
