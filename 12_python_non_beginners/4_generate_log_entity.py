import os
import string
import random

def generate_log_entry():
    log_entry = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + ' ') for _ in range(100))
    return f"{log_entry}\n"

def create_demo_log_file(file_name, target_size_kb):
    current_size = 0
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_directory, file_name)

    with open(file_path, 'w') as log_file:
        while current_size < target_size_kb * 1024:
            log_entry = generate_log_entry()
            log_file.write(log_entry)
            current_size += len(log_entry)

if __name__ == "__main__":
    demo_log_file_name = "demo_log.txt"
    target_size_kb = 17

    create_demo_log_file(demo_log_file_name, target_size_kb)
    print(f"Demo log file created at: {demo_log_file_name}")
