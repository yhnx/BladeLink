import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import os
import subprocess
import threading

class ImageFrame:
    def __init__(self, root, switch_back_callback):
        self.display_thumbnail = None
        self.root = root
        self.switch_back_callback = switch_back_callback
        self.selected_image_path = None
        self.thumbnail_canvas = None  # To display the selected thumbnail

    def show(self):
        # Clear the existing window content
        for widget in self.root.winfo_children():
            widget.destroy()

        # Heading
        heading = tk.Label(self.root, text="Select an Image", font=("Arial", 15))
        heading.pack(pady=10)

        style = ttk.Style()
        style.configure("Custom.TButton", font=('calibri', 12, 'bold'))

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

        # Function to display a thumbnail of the selected image
        def browse_image():
            file_path = filedialog.askopenfilename(
                filetypes=[("All Files","* *"),("Image Files", "*.jpeg;*.jpg;*.png")]
            )
            if file_path:
                self.selected_image_path = file_path
                self.display_thumbnail(file_path)
                send_button.config(state=tk.NORMAL)

        # Display the selected thumbnail on the canvas
        def display_thumbnail(file_path):
            if self.thumbnail_canvas:
                self.thumbnail_canvas.destroy()

            self.thumbnail_canvas = tk.Canvas(self.root, width=150, height=150, bg="white", highlightthickness=1, highlightbackground="black")
            self.thumbnail_canvas.pack(pady=10, before=button_frame)

            img = Image.open(file_path)
            img.thumbnail((150, 150))
            img_tk = ImageTk.PhotoImage(img)

            self.thumbnail_canvas.create_image(75, 75, image=img_tk)
            self.thumbnail_canvas.image = img_tk  # Keep a reference

        self.display_thumbnail = display_thumbnail  # Bind method to self

        # Browse button
        browse_button = ttk.Button(text="Browse", command=browse_image, width=20, style="Custom.TButton")
        browse_button.pack()

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        # Function to run QPSK script in a separate thread
        def run_qpsk_script():
            try:
                os.environ['INPUT_FILE'] = self.selected_image_path
                os.environ['OUTPUT_FILE'] = "./output.tmp"  # Define output file path
                
                subprocess.run(["python3", "Telelink.py"], check=True)
                messagebox.showinfo("Execution Complete", "QPSK script executed successfully.")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Script execution failed: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected error: {e}")

        # Send button
        def send_image():
            if self.selected_image_path:
                threading.Thread(target=run_qpsk_script).start()

        send_button = ttk.Button(button_frame, text="Send", command=send_image, state=tk.DISABLED, width=20, style="Custom.TButton")
        send_button.grid(row=0, column=1, padx=10)

        # Cancel button
        cancel_button = ttk.Button(button_frame, text="Cancel", command=self.switch_back_callback, width=20, style="Custom.TButton")
        cancel_button.grid(row=0, column=2, padx=10)
