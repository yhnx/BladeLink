import os
import numpy as np
from gnuradio import gr
import time

class file_reader(gr.sync_block):
    """
    Reads N bytes from a file and outputs them as a stream.
    Handles dynamic file size changes and end-of-file scenarios.
    """

    def __init__(self, file_path="", n_bytes=0):
        super().__init__(
            name="file_reader",
            in_sig=None,
            out_sig=[np.uint8]
        )
        self.time = time.time()
        self.file_path = file_path
        self.n_bytes = n_bytes
        self.file_position = 0  # Tracks the last read position

    def work(self, input_items, output_items):
        out = output_items[0]
        num_to_fill = len(out)  # Number of bytes to fill
        out[:] = 0  # Default output to zero

        try:

            # Check the current file size
            file_size = os.path.getsize(self.file_path)
            # Open the file in binary read mode
            with open(self.file_path, 'rb') as f:
                # Seek to the current read position
                f.seek(self.file_position)

                # Read data up to the desired number of bytes
                data = f.read(num_to_fill)
        
                # Update the output buffer
                #out=data
                #print(out)
                out[:len(data)] = np.frombuffer(data, dtype=np.uint8)
                #print(out)
               

                #content=f.read()
                #with open(self.file_path, 'wb') as file:
                #    f.write(content)
                #    print(len(content))
                self.file_position+=len(data)
                return len(data)


        except FileNotFoundError:
            # If the file is not found, output zeros
            pass

        return 10
# Example usage:
# block = file_reader("/path/to/file", 1024)
