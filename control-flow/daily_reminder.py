Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
time_bounded = input("Is it time-bound? (yes/no): ")
match Priority:
        case "high":
            reminder = f"High priority task: '{task_name}'. Please prioritize this task."
        case "medium":
            reminder = f"Medium priority task: '{task_name}'. Keep track of this task."
        case "low":
            reminder = f"Low priority task: '{task_name}'. This task can be done later."
        case _:
            reminder = f"Priority level '{priority}' not recognied."
if time_bounded == "yes" :
    print(f"Reminder: {reminder}")
else :
    print(f"Note: {reminder}")

