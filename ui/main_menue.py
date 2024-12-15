import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw


class MainFrame:
    def __init__(self, root, switch_frame_callback):
        self.root = root
        self.switch_frame_callback = switch_frame_callback

    def show(self):
        # Clear the existing window content
        for widget in self.root.winfo_children():
            widget.destroy()

        try:
            image_path = r"1691477213269.jpg"  # Replace with the path to your image
            img = Image.open(image_path)
            img.thumbnail((300, 300))  # Resize the image to fit the window

            # Create a mask for the rounded corners
            corner_radius = 50  # Adjust this value for the corner radius
            mask = Image.new("L", img.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle(
                [(0, 0), img.size],
                radius=corner_radius,
                fill=255
            )

            # Apply the mask to the image
            rounded_img = Image.new("RGBA", img.size)
            rounded_img.paste(img, (0, 0), mask=mask)

            img_tk = ImageTk.PhotoImage(rounded_img)

            # Display the image with rounded corners
            image_label = tk.Label(self.root, image=img_tk)
            image_label.image = img_tk  # Keep a reference to avoid garbage collection
            image_label.place(x=98, y=50)  # Adjust placement
        except Exception as e:
            print(f"Failed to load image: {e}")

        try:
            # Load the image
            image_path = r"tele-removebg-preview.png"  # Replace with your image path
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

        style = ttk.Style()
        style.configure("Custom.TButton",
                        font=('calibri', 12, 'bold')
                        )

        # Create a frame to center the buttons
        frame = ttk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create Start and Exit buttons
        start_button = ttk.Button(frame, text="Start", command=self.switch_frame_callback, width=20, style="Custom.TButton")
        exit_button = ttk.Button(frame, text="Exit", command=self.root.destroy, width=20, style="Custom.TButton")

        # Arrange buttons in the frame
        start_button.grid(row=0, column=0, padx=10, pady=10)
        exit_button.grid(row=0, column=1, padx=10, pady=10)
