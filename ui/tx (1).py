import sys



def add_preamble(file,filetype):
        # Example binary string
    print(filetype)
    binarypreamble = b'11000110101100111111010110101000011010110011111000110101100'
    file_path =file
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    preamble = binarypreamble * 300
    detect_sequence = b'sts'  # Sequence to detect preamble
    
    with open('./tx.tmp', 'wb') as output_file:
        output_file.write(preamble + detect_sequence + plaintext + detect_sequence+binarypreamble+bytes(int(filetype)) + preamble)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <path_to_python_file>,type" )
        sys.exit(1)

    file = sys.argv[1]
    filetype = sys.argv[2]
    add_preamble(file,filetype)
    print('file created')
