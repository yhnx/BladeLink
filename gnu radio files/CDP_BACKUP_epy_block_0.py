import numpy as np
from gnuradio import gr
import subprocess
import os
import threading
import time

class vlc_video_sink(gr.sync_block):
    """
    A custom GNU Radio block to view video using VLC
    """

    def __init__(self,video_path=None):
        gr.sync_block.__init__(
            self,
            name="vlc_video_sink",  # Block name
            in_sig=[np.uint8],      # Input is a byte stream
            out_sig=None            # No output signal
        )
        self.video_path = video_path
        # Initialize VLC player
  
    def start(self):
        def open_program():
            time.sleep(10)
            vlc_command = "vlc"  # VLC command for Linux
    
            if not os.path.exists(self.video_path):
                print(f"Error: File not found: {self.video_path}")
                return
            
            try:

                # Launch VLC minimized with the video file
                subprocess.run([vlc_command, "--qt-start-minimized", self.video_path])
            except FileNotFoundError:
                print("Error: VLC Media Player is not installed. Install it using your package manager (e.g., sudo apt install vlc).")


        # Create and start a thread
        program_thread = threading.Thread(target=open_program)
        program_thread.start()

    def stop(self):
        # Stop the VLC player
        try:
            subprocess.run(["pkill", "vlc"])
            print("VLC closed successfully.")
        except Exception as e:
            print(f"Error closing VLC: {e}")

    def work(self, input_items, output_items):
        
        # Consume all input
        return len(input_items[0])




# Main thread can continue doing other tasks
print("Program is running in a separate thread.")