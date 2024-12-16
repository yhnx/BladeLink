import tkinter as tk
from tkinter import ttk


class OptionsFrame:
    def __init__(self, root, switch_frame_callback):
        self.root = root
        self.switch_frame_callback = switch_frame_callback

    def show(self):
        # Clear the existing window content
        for widget in self.root.winfo_children():
            widget.destroy()

        # Add heading
        heading = ttk.Label(self.root, text="What do you need to transmit", font=("Arial", 10))
        heading.pack(pady=20)

        # Add a back button to return to the previous frame
        back_button = ttk.Button(self.root, text="←", command=self.switch_frame_callback)
        back_button.place(x=10, y=10)

        # Create a frame for the buttons
        button_frame = ttk.Frame(self.root)
        button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Add Text, Image, and Video buttons
        text_button = ttk.Button(button_frame, text="Text", width=15)
        image_button = ttk.Button(button_frame, text="Image", width=15)
        video_button = ttk.Button(button_frame, text="Video", width=15)

        text_button.pack(pady=10)
        image_button.pack(pady=10)
        video_button.pack(pady=10)