import tkinter as tk

def GetDimensions():
    root.update()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    
def whiteScreen():
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.configure(bg="#DCDCDC")
    root.attributes("-alpha", 1.0)
    # These are your escape hatches
    root.bind("<Escape>", lambda e: root.destroy())

def start_Break():
    root.deiconify() # Show the window
    root.update()
    root.focus_force() 
    root.grab_set() 
    label = tk.Label(root, text="Look Away!", font=("Helvetica", 40), bg="#DCDCDC", fg="black")
    label.place(relx=0.5, rely=0.5, anchor="center") 
    root.after(20000, start_Work) # Wait 20 seconds, then hide window


def start_Work():
    root.grab_release() # Release mouse/keyboard
    root.withdraw()     # Hide the window
    root.after(1200000, start_Break) # Wait 20 minutes, then show white

if __name__ == "__main__":
    root = tk.Tk()
    GetDimensions()
    whiteScreen()
    start_Work()
    root.mainloop()