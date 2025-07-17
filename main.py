import os
import subprocess
import py_cui

BOOT_DIR = "./boot_entries"

selected_script = None
menu_widget = None

def get_boot_entries():
    """List .py files in BOOT_DIR"""
    return [f for f in os.listdir(BOOT_DIR) if f.endswith(".py")]

def select_script(root):
    global selected_script, menu_widget
    selected_script = menu_widget.get()
    root.stop()

def exit_program(root):
    global selected_script
    selected_script = None
    root.stop()

def start_tui():
    global menu_widget

    scripts = get_boot_entries()

    root = py_cui.PyCUI(4, 2)
    root.set_title("Python Boot Manager")

    menu_widget = root.add_scroll_menu("Available Boot Scripts", 0, 0, row_span=4, column_span=2)
    menu_widget.add_item_list(scripts)

    menu_widget.add_key_command(py_cui.keys.KEY_ENTER, lambda: select_script(root))
    root.add_key_command(py_cui.keys.KEY_Q_LOWER, lambda: exit_program(root))

    root.start()

def main():
    start_tui()

    if selected_script:
        print(f"\nBooting {selected_script}...\n")
        script_path = os.path.join(BOOT_DIR, selected_script)
        subprocess.run(["python", script_path])

if __name__ == "__main__":
    main()
