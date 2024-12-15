import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw


class OptionsFrame:
    def __init__(self, root, switch_frame_callback, text_frame_callback, image_frame_callback, video_frame_callback, sound_frame_callback):
        self.root = root
        self.switch_frame_callback = switch_frame_callback
        self.text_frame_callback = text_frame_callback
        self.image_frame_callback = image_frame_callback
        self.video_frame_callback = video_frame_callback
        self.sound_frame_callback = sound_frame_callback

    def show(self):
        # Clear the existing window content
        for widget in self.root.winfo_children():
            widget.destroy()

        # Add heading
        heading = ttk.Label(self.root, text="What do you need to transmit", font=("Arial", 15))
        heading.pack(pady=20)

        style = ttk.Style()
        style.configure("Custom.TButton",
                        font=('calibri', 12, 'bold')
                        )
        try:
            # Load the image
            image_path = r"C:\\Users\\Bathiya Dissanayake\\Downloads\\tele-removebg-preview.png"  # Replace with your image path
            img = Image.open(image_path)
            img.thumbnail((100, 100))  # Resize the image to fit better (optional)
            img_tk = ImageTk.PhotoImage(img)

            # Create an image label
            image_label = tk.Label(self.root, image=img_tk)
            image_label.image = img_tk  # Keep a reference to avoid garbage collection

            # Use the `place()` method to position at bottom-right
            # x=width - image_width, y=height - image_height
            self.root.update_idletasks()  # Update the window to get its dimensions
            x_position = self.root.winfo_width() - 110  # Adjust for image size and padding
            y_position = self.root.winfo_height() - 90
            image_label.place(x=x_position, y=y_position)
        except Exception as e:
            print(f"Failed to load image: {e}")

        # Add a back button to return to the previous frame
        back_button = ttk.Button(self.root, text="←", command=self.switch_frame_callback, style="Custom.TButton")
        back_button.place(x=10, y=10)

        # Create a frame for the buttons
        button_frame = ttk.Frame(self.root)
        button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Add Text, Image, and Video buttons
        text_button = ttk.Button(button_frame, text="Text", command=self.text_frame_callback, width=20, style="Custom.TButton")
        image_button = ttk.Button(button_frame, text="Image", command=self.image_frame_callback, width=20, style="Custom.TButton")
        video_button = ttk.Button(button_frame, text="Video", command=self.video_frame_callback, width=20, style="Custom.TButton")
        sound_button = ttk.Button(button_frame, text="Audio", command=self.sound_frame_callback, width=20, style="Custom.TButton")

        text_button.pack(pady=10)
        image_button.pack(pady=10)
        video_button.pack(pady=10)
        sound_button.pack(pady=10)