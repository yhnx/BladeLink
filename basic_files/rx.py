# Function to remove both front and back preambles and sequence from file
from os import name
import time
import subprocess
def remove_preamble(file_path):
    global content
    
    detect_sequence = b'sts'

    #with open(file_path, 'rb') as file:
        #content = file.read()

    start_index = content.find(detect_sequence)
    if start_index != -1:
        content = content[start_index + len(detect_sequence):]

    end_index = content.rfind(detect_sequence)
    if end_index != -1:
        content = content[:end_index]

def tag():
     global content
     detected=False
     typs=[b'mp3',b'jpeg',b'mp4']
     
     while(True):
        with open('./rx.tmp', 'rb') as file:

            content = file.read()
            if(len(content)>10):print('conncted')
            time.sleep(1)

            start= content.find(b'sts')
            if start!= -1:
                    print('file recieving')
                    end_name= content.rfind(b'|||')
                    name=content[start:end_name]
                    print(name)
                    end_index = content.rfind(b'end')
                    if end_index != -1:
                        start= content.find(b'|||')
                        content = content[start:end_index]
                        with open('./'+name.decode(),'wb') as output:
                             output.write(content)
                             with open('./rx.tmp','wb') as output:pass
                        break


# Remove both front and back preambles and sequence from the output.tmp file
tag()