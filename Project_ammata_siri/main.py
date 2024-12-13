import tkinter as tk
from main_menue import MainFrame
from option import OptionsFrame

root = tk.Tk()
root.title("User Interface")
root.geometry("400x400")
root.resizable(False, False)  # Disable resizing and fullscreen scaling

# Frame instances
main_frame = MainFrame(root, lambda: options_frame.show())
options_frame = OptionsFrame(root, lambda: main_frame.show())

# Show the main frame initially
main_frame.show()

# Run the application
root.mainloop()
