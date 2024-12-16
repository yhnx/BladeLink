from Crypto.Cipher import AES
import os



input_file = os.environ['INPUT_FILE'] # Define input file path
output_file = os.environ['OUTPUT_FILE']  # Define output file path
tmp_file = "/input.tmp"  # Temporary file path

def add_preamble():
        # Example binary string
    binarypreamble = b'11000110101100111111010110101000011010110011111000110101100'
    file_path =input_file
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    preamble = binarypreamble * 30
    detect_sequence = b'sts'  # Sequence to detect preamble
    
    with open(tmp_file, 'wb') as output:
        output.write(preamble + detect_sequence + ciphertext + detect_sequence + preamble)

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
encrypt_file(input_file, predefined_key)

#Adds the preamble
add_preamble()
