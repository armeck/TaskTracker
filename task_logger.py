from datetime import datetime
from pathlib import Path

def log_task(task_text):
    # Current date and time
    now = datetime.now()

    year = now.strftime("%Y")
    month_filename = now.strftime("%m-%B.txt")
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Base directory for logs
    base_dir = Path("task_logs")
    year_dir = base_dir / year

    # Create directories if they don't exist
    year_dir.mkdir(parents=True, exist_ok=True)

    # Monthly file path
    log_file = year_dir / month_filename

    # Write task to file
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"--- {timestamp} ---\n")
        f.write(f"{task_text}\n\n")

    print("✅ Task logged successfully.")

def main():
    print("📝 Task Logger")
    print("Type 'exit' to quit.\n")

    while True:
        task = input("Enter a task: ").strip()

        if task.lower() == "exit":
            print("Goodbye 👋")
            break

        if task:
            log_task(task)
        else:
            print("⚠️ Task cannot be empty.")

if __name__ == "__main__":
    main()
