import numpy as np
from gnuradio import gr
import pmt

class TagSwitch(gr.sync_block):
    def __init__(self,tag_key="",button=1):
        gr.sync_block.__init__(self,
                               name="TagSwitch",
                               in_sig=[np.int8],
                               out_sig=[np.int8]*2)
        self.tag_key = tag_key
        self.current_output = 0
        self.button=button

    def work(self, input_items, output_items):
        tags = self.get_tags_in_range(0, 0, len(input_items[0]))
        for tag in tags:
            if pmt.to_python(tag.key) == self.tag_key:
                self.current_output = 1 if self.current_output == 0 else 0
                print(self.current_output)
        
        out_data_1 = output_items[1]
        out_data_0 = output_items[0]

        in_data = input_items[0]

        if(int(self.current_output)):in_data = input_items[0]*0
        else: pass
        

        # Copy input to both outputs
        out_data_0[:] = in_data*self.button
        out_data_1[:] = in_data*self.button

        return len(in_data)
        