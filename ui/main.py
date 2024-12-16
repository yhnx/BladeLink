import tkinter as tk
from main_menue import MainFrame
from option import OptionsFrame
from Text import TextFrame
from video import VideoFrame
from image import ImageFrame
from Sound import SoundFrame

root = tk.Tk()
root.title("CDP Group Tele-Link")
root.geometry("500x400")

icon_path = r"signal-tower.ico"  # Example location
try:
    root.iconbitmap(icon_path)  # Use for .ico files
except tk.TclError:
    pass

root.resizable(False, False)  # Disable resizing and full-screen scaling

# Frame instances
main_frame = MainFrame(root, lambda: options_frame.show())
options_frame = OptionsFrame(root, lambda: main_frame.show(),
                             lambda: text_frame.show(),
                             lambda: image_frame.show(),
                             lambda: video_frame.show(),
                             lambda: sound_frame.show())
text_frame = TextFrame(root, lambda: options_frame.show())
image_frame = ImageFrame(root, lambda: options_frame.show())
video_frame = VideoFrame(root, lambda: options_frame.show())
sound_frame = SoundFrame(root, lambda: options_frame.show())


# Show the main frame initially
main_frame.show()

# Run the application
root.mainloop()