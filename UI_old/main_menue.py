import tkinter as tk
from tkinter import ttk


class MainFrame:
    def __init__(self, root, switch_frame_callback):
        self.root = root
        self.switch_frame_callback = switch_frame_callback

    def show(self):
        # Clear the existing window content
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create a frame to center the buttons
        frame = ttk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create Start and Exit buttons
        start_button = ttk.Button(frame, text="Start", command=self.switch_frame_callback, width=15)
        exit_button = ttk.Button(frame, text="Exit", command=self.root.destroy, width=15)

        # Arrange buttons in the frame
        start_button.grid(row=0, column=0, padx=10, pady=10)
        exit_button.grid(row=0, column=1, padx=10, pady=10)