import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import subprocess
import threading

class TextFrame:
    def __init__(self, root, switch_back_callback):
        self.root = root
        self.switch_back_callback = switch_back_callback

    def show(self):
        # Clear the existing window content
        for widget in self.root.winfo_children():
            widget.destroy()

        # Heading
        heading = tk.Label(self.root, text="Write Your Text Message", font=("Arial", 15))
        heading.pack(pady=20)

        # Text entry widget
        text_entry = tk.Text(self.root, width=30, height=10, font=("Arial", 11))
        text_entry.pack(pady=10)

        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

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
            self.root.update_idletasks()  # Update the window to get its dimensions
            x_position = self.root.winfo_width() - 110  # Adjust for image size and padding
            y_position = self.root.winfo_height() - 90
            image_label.place(x=x_position, y=y_position)
        except Exception as e:
            print(f"Failed to load image: {e}")

        # Function to run external script in a separate thread
        def run_qpsk_script_with_text():
            try:
                os.environ['INPUT_FILE'] = self.selected_image_path
                os.environ['OUTPUT_FILE'] = "./output.tmp"  # Define output file path
                subprocess.run(["python3", "tx.py",self.selected_image_path,"jpeg"], check=True)
                subprocess.run(["python3", "Telelink.py"], check=True)
                messagebox.showinfo("Execution Complete", "QPSK script executed successfully.")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Script execution failed: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected error: {e}")

        # Save button
        def save_and_send():
            threading.Thread(target=run_qpsk_script_with_text).start()

        save_button = ttk.Button(button_frame, text="Send", command=save_and_send, width=20, style="Custom.TButton")
        save_button.grid(row=0, column=0, padx=10)

        # Cancel button
        cancel_button = ttk.Button(button_frame, text="Cancel", command=self.switch_back_callback, width=20, style="Custom.TButton")
        cancel_button.grid(row=0, column=1, padx=10)
