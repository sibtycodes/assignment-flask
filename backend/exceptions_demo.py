import json

try:
    with open("tasks.json", "r") as f:
        data = json.load(f)

    print("Tasks loaded:", data)

except FileNotFoundError:
    print("Error: tasks.json file is missing.")

except json.JSONDecodeError:
    print("Error: JSON format is invalid.")

except Exception as e:
    print("Unexpected error:", e)
