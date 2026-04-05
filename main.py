import tkinter as tk
import signal

WORK_TIME = 1200000   # 20 minutes
BREAK_TIME = 20        # 20 seconds

countdown_id = None

signal.signal(signal.SIGINT, signal.SIG_IGN)  # Ignore Ctrl+C --> KeyboardInterrupt error in my VS Code

def get_dimensions():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")

def white_screen():
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.configure(bg="#DCDCDC")
    root.bind("<Escape>", lambda e: root.destroy())

def countdown(seconds):
    global countdown_id
    if seconds > 0:
        timer_label.config(text=f"{seconds}")
        countdown_id = root.after(1000, countdown, seconds - 1)
    else:
        start_work()

def start_break():
    global countdown_id
    if countdown_id is not None:
        root.after_cancel(countdown_id)
        countdown_id = None

    root.attributes("-alpha", 1.0)
    root.attributes("-topmost", True)
    root.deiconify()
    root.focus_force()
    root.grab_set()
    countdown(BREAK_TIME)

def start_work():
    root.grab_release()
    root.attributes("-alpha", 0.0)
    root.attributes("-topmost", False)
    root.lower()
    root.after(WORK_TIME, start_break)

if __name__ == "__main__":
    print("Program Running...")
    root = tk.Tk()
    get_dimensions()
    white_screen()

    label = tk.Label(root, text="Look Away!", font=("Helvetica", 40), bg="#DCDCDC", fg="black")
    label.place(relx=0.5, rely=0.4, anchor="center")

    timer_label = tk.Label(root, text="", font=("Helvetica", 80, "bold"), bg="#DCDCDC", fg="black")
    timer_label.place(relx=0.5, rely=0.55, anchor="center")

    start_work()
    root.mainloop()