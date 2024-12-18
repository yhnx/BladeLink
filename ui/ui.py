import customtkinter as ctk
import os
import threading
import subprocess
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk  # Import Image and ImageTk
from Crypto.Cipher import AES

class TransmittingApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Try to set icon using PIL Image
        try:
            # Load the icon
            icon_path = r"./signal-tower.ico"  # Example location
            try:
                self.iconbitmap(icon_path)  # Use for .ico files
            except tk.TclError:
                pass
        except Exception as e:
            print(f"Error setting icon: {e}")

        # Configure window
        self.title("TeleLink Communications")
        self.geometry("800x600")
        self.configure(fg_color="#FFFFFF")

        # Create frame for landing page
        self.landing_frame = ctk.CTkFrame(self, fg_color="white")
        self.landing_frame.pack(expand=True, fill="both")

        try:
            image_path = r"./bladeLINK.png"  # Ensure this path is correct
            title_image = Image.open(image_path)
            title_image = title_image.resize((300, 140), Image.LANCZOS)  # Resize if needed
            title_photo = ctk.CTkImage(light_image=title_image, size=(300, 140))  # Convert to CTkImage
            title_label = ctk.CTkLabel(
                self.landing_frame, 
                image=title_photo, 
                text=""
            )
            title_label.pack(pady=(120, 0))
        except Exception as e:
            print(f"Error loading title image: {e}")


        # Start Button
        transmit_button = ctk.CTkButton(
            self.landing_frame, 
            text="Transmit", 
            font=("Roboto", 18),
            command=self.open_file_page,
            fg_color="#2ECC71",  # Emerald
            hover_color="#27AE60",  # Green Sea
            text_color="white",
            width=200,  # Adjust the width as needed
            height=50  
        )
        transmit_button.pack(pady=(40,20))

        # Recieve Button
        recieve_button = ctk.CTkButton(
            self.landing_frame, 
            text="Recieve", 
            font=("Roboto", 18),
            #command=self.open_recieve_page,
            fg_color="#3498DB",  # Peter River
            hover_color="#2980B9",  # Belize Hole
            text_color="white",
            width=200,  # Adjust the width as needed
            height=50  
        )
        recieve_button.pack(pady=(20,0))

        # Logo Frame (bottom right)
        logo_frame = ctk.CTkFrame(self.landing_frame, fg_color="white")
        logo_frame.pack(side="bottom", anchor="se", padx=20, pady=20)

        # Load and display logo using PIL Image and ImageTk.PhotoImage
        try:
            image_path = r"./telelink.png"
            logo_image = Image.open(image_path)  # Use PIL to open the image
            logo_image = logo_image.resize((150, 150), Image.LANCZOS)  # Resize if needed
            logo_photo = ctk.CTkImage(light_image=logo_image, size=(150, 150))  # Convert to CTkImage
            logo_label = ctk.CTkLabel(
                logo_frame, 
                image=logo_photo, 
                text=""
            )
            logo_label.photo = logo_photo  # Keep reference to avoid garbage collection
            logo_label.pack(fill="both", expand=True)
        except Exception as e:
            print(f"Error loading logo: {e}")
            logo_label = ctk.CTkLabel(
                logo_frame, 
                text="Telelink", 
                font=("Roboto", 12)
            )
            logo_label.pack()

        # File Selection Page (initially hidden)
        self.file_frame = ctk.CTkFrame(self, fg_color="white")
        
        # Selected File Display Frame
        self.file_display_frame = ctk.CTkFrame(self.file_frame, fg_color="white")
        self.file_display_frame.pack(pady=20)

        # File Icon
        self.file_icon_label = ctk.CTkLabel(
            self.file_display_frame, 
            text="📄", 
            font=("Arial", 142),  # Increase the font size
            text_color="gray"
        )
        self.file_icon_label.pack(pady=(120,1))

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
            fg_color ="#2C3E50",
            hover_color="#34495E",
            text_color="white",
            width=200,  # Adjust the width as needed
            height=50   # Adjust the height as needed
        )
        file_select_button.pack(pady =(30,0))

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
        self.send_file_button.pack(side="left", padx=(190,0))

        # Back Button
        back_button = ctk.CTkButton(
            self.file_frame, 
            text="Back", 
            command=self.show_landing_page,
            fg_color="#E74C3C",
            hover_color="#C0392B",
            text_color="white"
        )
        back_button.pack(side="right", padx=(0,190))

        # Initialize selected file path
        self.selected_file_path = None

    def open_file_page(self):
        """Transition to file selection page"""
        self.landing_frame.pack_forget()
        self.file_frame.pack(expand=True, fill="both")

    def show_landing_page(self):
        """Return to landing page"""
        self.file_frame.pack_forget()
        self.landing_frame.pack(expand=True, fill="both")

        # Reset UI elements
        self.status_label.configure(text="")
        self.send_file_button.configure(state="disabled")
        self.file_path_label.configure(text="No file selected")
        self.file_size_label.configure(text="")
        self.file_icon_label.configure(text_color="gray")

    def select_file(self):
        """Open file dialog to select a file"""
        self.selected_file_path = filedialog.askopenfilename()
        if self.selected_file_path:
            # Update file name
            file_name = os.path.basename(self.selected_file_path)
            self.file_path_label.configure(text=file_name)
            
            # Update file size
            file_size = os.path.getsize(self.selected_file_path)
            size_str = self.format_file_size(file_size)
            self.file_size_label.configure(text=f"Size: {size_str}")
            
            # Change file icon color and enable send button
            self.file_icon_label.configure(text_color="black")
            self.send_file_button.configure(state="normal")

    def format_file_size(self, size_bytes):
        """Convert file size to human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0

    def send_file(self):
        """Send file using Telelink.py"""
        if not self.selected_file_path:
            tk.messagebox.showerror("Error", "Please select a file first!")
            return

        # Disable send button during transmission
        self.send_file_button.configure(state="disabled")

        # Clear any previous status message
        self.status_label.configure(text="")

        def run_telelink():
            try:
                # Set environment variable for file path
                tmp_file = "./input.tmp"  # Temporary file path

                def add_preamble():
                        # Example binary string
                    binarypreamble = b'11000110101100111111010110101000011010110011111000110101100'
                    file_path = self.selected_file_path
                    with open(file_path, 'rb') as file:
                        plaintext = file.read()
                    preamble = binarypreamble * 30
                    detect_sequence = b'sts'  # Sequence to detect preamble
                    
                    with open(tmp_file, 'wb') as output:
                        file_name = os.path.basename(self.selected_file_path)
                        #file = bytes(file_name)
                        output.write(preamble + detect_sequence + detect_sequence + plaintext + detect_sequence + preamble)

                        #Encryption
                        def pad(data):
                            # Padding the data to be a multiple of 16 bytes
                            return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

                        def encrypt_file(file_path, key):
                            global ciphertext
                            with open(file_path, 'rb') as file:
                                plaintext = file.read()

                            plaintext = pad(plaintext)
                            cipher = AES.new(key, AES.MODE_ECB)  
                            ciphertext = cipher.encrypt(plaintext)


                        predefined_key = b'WeAreTeleLink'

                        # Encrypt the file
                        #encrypt_file(self.selected_file_path, predefined_key)

                #Adds the preamble
                add_preamble()

                # Start Telelink.py as a subprocess
                process = subprocess.Popen(
                    ['python3', './Telelink_transmitter.py'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                # Capture output and errors from Telelink.py
                stdout, stderr = process.communicate()

                if process.returncode == 0:
                    # Success: Update the UI
                    self.after(0, self.handle_transmission_success, stdout)
                else:
                    # Failure: Handle the error
                    self.after(0, self.handle_transmission_error, stderr)

            except subprocess.CalledProcessError as e:
                # Handle subprocess errors
                self.after(0, self.handle_transmission_error, str(e))
            except Exception as e:
                # Handle other unexpected errors
                self.after(0, self.handle_transmission_error, str(e))

        # Run in a separate thread to prevent GUI freezing
        threading.Thread(target=run_telelink, daemon=True).start()

    def handle_transmission_success(self, output):
        """Handle successful file transmission"""
        self.status_label.configure(
            text="✅ Transmission Successful", 
            text_color="green"
        )
        self.send_file_button.configure(state="normal")
        
        # Optional: Show output from Telelink.py if needed
        if output:
            tk.messagebox.showinfo("Transmission Details", output)

    def handle_transmission_error(self, error):
        """Handle transmission errors"""
        self.status_label.configure(
            text="❌ Transmission Failed", 
            text_color="red"
        )
        self.send_file_button.configure(state="normal")
        tk.messagebox.showerror("Error", error)

if __name__ == "__main__":
    app = TransmittingApp()
    app.mainloop()
