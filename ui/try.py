import customtkinter as ctk
import os
import threading
import subprocess
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from Crypto.Cipher import AES

class TeleLinkApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Try to set icon using PIL Image
        try:
            icon_path = r"./signal-tower.ico"  # Example location
            self.iconbitmap(icon_path)  # Use for .ico files
        except Exception as e:
            print(f"Error setting icon: {e}")

        # Configure window
        self.title("TeleLink Transceiver")
        self.geometry("800x600")
        self.configure(fg_color="#FFFFFF")

        # Create frame for landing page
        self.landing_frame = ctk.CTkFrame(self, fg_color="white")
        self.landing_frame.pack(expand=True, fill="both")

        # Title Label
        title_label = ctk.CTkLabel(
            self.landing_frame, 
            text="TeleLink Transceiver", 
            font=("Roboto-bold", 24, "bold"),
            text_color="black"
        )
        title_label.pack(pady=(180, 20))

        # Transmit Button
        transmit_button = ctk.CTkButton(
            self.landing_frame, 
            text="Transmit", 
            font=("Roboto", 18),
            command=self.open_transmit_page,
            fg_color="#27AE60",
            hover_color="#2ECC71",
            text_color="white",
            width=200,
            height=50
        )
        transmit_button.pack(pady=20)

        # Receive Button
        receive_button = ctk.CTkButton(
            self.landing_frame, 
            text="Receive", 
            font=("Roboto", 18),
            command=self.open_receive_page,  # Placeholder for future functionality
            fg_color="#2C3E50",
            hover_color="#34495E",
            text_color="white",
            width=200,
            height=50
        )
        receive_button.pack(pady=20)

        # Logo Frame (bottom right)
        logo_frame = ctk.CTkFrame(self.landing_frame, fg_color="white")
        logo_frame.pack(side="bottom", anchor="se", padx=20, pady=20)

        try:
            image_path = r"./telelink.png"
            logo_image = Image.open(image_path).resize((150, 150), Image.LANCZOS)
            logo_photo = ctk.CTkImage(light_image=logo_image, size=(150, 150))
            logo_label = ctk.CTkLabel(logo_frame, image=logo_photo, text="")
            logo_label.photo = logo_photo
            logo_label.pack(fill="both", expand=True)
        except Exception as e:
            print(f"Error loading logo: {e}")
            ctk.CTkLabel(
                logo_frame, 
                text="Telelink", 
                font=("Roboto", 12)
            ).pack()

        # File Selection Page (initially hidden)
        self.file_frame = ctk.CTkFrame(self, fg_color="white")
        self.initialize_file_frame()

    def initialize_file_frame(self):
        """Initialize file selection page."""
        # Selected File Display Frame
        self.file_display_frame = ctk.CTkFrame(self.file_frame, fg_color="white")
        self.file_display_frame.pack(pady=20)

        # File Icon
        self.file_icon_label = ctk.CTkLabel(
            self.file_display_frame, 
            text="📄", 
            font=("Arial", 142), 
            text_color="gray"
        )
        self.file_icon_label.pack(pady=(120, 1))

        # Selected File Path Label
        self.file_path_label = ctk.CTkLabel(
            self.file_display_frame, 
            text="No file selected", 
            text_color="black",
            font=("Arial", 14)
        )
        self.file_path_label.pack(pady=0)

        # File Size Label
        self.file_size_label = ctk.CTkLabel(
            self.file_display_frame, 
            text="", 
            text_color="gray"
        )
        self.file_size_label.pack(pady=5)

        # Transmission Status Label
        self.status_label = ctk.CTkLabel(
            self.file_frame, 
            text="", 
            text_color="green",
            font=("Arial", 12)
        )
        self.status_label.pack(pady=10)

        # File Select Button
        file_select_button = ctk.CTkButton(
            self.file_frame, 
            text="Select File", 
            font=("Arial", 17),
            command=self.select_file,
            fg_color="#2C3E50",
            hover_color="#34495E",
            text_color="white",
            width=200,
            height=50
        )
        file_select_button.pack(pady=(30, 0))

        # Send File Button (initially disabled)
        self.send_file_button = ctk.CTkButton(
            self.file_frame, 
            text="Send File", 
            command=self.send_file,
            fg_color="#27AE60",
            hover_color="#2ECC71",
            text_color="white",
            state="disabled"
        )
        self.send_file_button.pack(side="left", padx=(190, 0))

        # Back Button
        back_button = ctk.CTkButton(
            self.file_frame, 
            text="Back", 
            command=self.show_landing_page,
            fg_color="#E74C3C",
            hover_color="#C0392B",
            text_color="white"
        )
        back_button.pack(side="right", padx=(0, 190))

        # Initialize selected file path
        self.selected_file_path = None

    def open_transmit_page(self):
        """Transition to file selection page for transmission."""
        self.landing_frame.pack_forget()
        self.file_frame.pack(expand=True, fill="both")

    def open_receive_page(self):
        """Placeholder for Receive functionality."""
        tk.messagebox.showinfo("Receive", "This functionality is under development.")

    def show_landing_page(self):
        """Return to the landing page."""
        self.file_frame.pack_forget()
        self.landing_frame.pack(expand=True, fill="both")

    # Remaining methods for file handling and transmission
    # (Select file, send file, and encryption logic remain unchanged.)

if __name__ == "__main__":
    app = TeleLinkApp()
    app.mainloop()
