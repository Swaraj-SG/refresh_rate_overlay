import tkinter as tk
import win32api
import win32con
import threading
import time

def get_refresh_rate():
    screen = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    return screen.DisplayFrequency

def update_refresh_rate(label):
    while True:
        refresh_rate = get_refresh_rate()
        label.config(text=f"{refresh_rate} Hz")
        time.sleep(1)

def display_refresh_rate():
    root = tk.Tk()
    root.attributes('-topmost', True, '-alpha', 0.7, '-fullscreen', False)
    root.overrideredirect(True)
    root.geometry("150x50+5+5")

    refresh_label = tk.Label(root, text="...", font=("Arial", 20), fg="cyan", bg="black")
    refresh_label.pack(fill=tk.BOTH, expand=True)

    thread = threading.Thread(target=update_refresh_rate, args=(refresh_label,), daemon=True)
    thread.start()
    root.mainloop()

if __name__ == "__main__":
    display_refresh_rate()
