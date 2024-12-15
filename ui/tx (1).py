# from Crypto.Cipher import AES




def add_preamble():
        # Example binary string
    binarypreamble = b'11000110101100111111010110101000011010110011111000110101100'
    file_path =input()
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    preamble = binarypreamble * 300
    detect_sequence = b'sts'  # Sequence to detect preamble
    
    with open('/home/praveen/Desktop/tx.tmp', 'wb') as output_file:
        output_file.write(preamble + detect_sequence + plaintext + detect_sequence + preamble)




# #Encryption
# def pad(data):
#     # Padding the data to be a multiple of 16 bytes
#     return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

# def encrypt_file(file_path, key):
#     global ciphertext
    
#     plaintext = pad(plaintext)
#     cipher = AES.new(key, AES.MODE_ECB)  
#     ciphertext = cipher.encrypt(plaintext)

  



# # Encryption details

# predefined_key = b'Hello_IamMihiran'

# # Encrypt the file
# encrypt_file(file_path, predefined_key)

#Adds the preamble
add_preamble()
