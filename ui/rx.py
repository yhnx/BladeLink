# Function to remove both front and back preambles and sequence from file
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
     
     while(not(detected)):
        with open('./rx.tmp', 'rb') as file:
            content = file.read()
        time.sleep(1) 
        for tag in typs:
            position= content.rfind(tag)
            if position != -1:
                remove_preamble('./rx.tmp')
                if(tag==b'jpeg'):
                    with open("./out.jpg", 'wb') as file:
                        file.write(content)
                        detected=True
                        subprocess.run(["open","./out.jpg"])
                if(tag==b'mp3'):
                    with open("./out.mp3", 'wb') as file:
                        file.write(content)
                        subprocess.run(["open","./out.mp3"])
                        detected=True
                if(tag==b'ts'):
                    with open("./out.ts", 'wb') as file:
                        file.write(content)
                        subprocess.run(["open","./out.ts"])
                        detected=True
                if(tag==b'mp4'):
                    with open("./out.mp4", 'wb') as file:
                        file.write(content)
                        subprocess.run(["open","./out.mp4"])
                        detected=True
                    print("detected")


# Remove both front and back preambles and sequence from the output.tmp file
tag()
