# Function to remove both front and back preambles and sequence from file
import time
import subprocess

def rx():
     global content
     
     while(True):
        with open('./rx.tmp', 'rb') as file:

            content = file.read()
            if(len(content)>10):print('conncted')
            time.sleep(1)

            start= content.find(b'sts')
            if start!= -1:
                    print('file recieving')
                    end_name= content.rfind(b'|||')
                    name=content[start+3:end_name]
                    print(name)
                    end_index = content.rfind(b'end')
                    if end_index != -1:
                        start= content.find(b'|||')
                        content = content[start+3:end_index]
                        path='./'+name.decode()
                        with open(path,'wb') as output:
                             output.write(content)
                             with open('./rx.tmp','wb') as output:pass
                        open_file(path)
                        break


def open_file(file_path):
        subprocess.run(["xdg-open", file_path])
