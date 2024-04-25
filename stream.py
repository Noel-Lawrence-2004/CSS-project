# importing required classes
from pypdf import PdfReader
import streamlit as st
import rsa
import hashlib
import os
import io

key_dir = r"D:\College\CSS\mini\keys"

def generate_digital_signature(text, CA_private_key):
    st.write("The data sent is ", text)
    text= text.strip()
    # Hashing of the data
    sha256_hash = hashlib.sha256()
    sha256_hash.update(text.encode('utf-8'))
    hashed_text = sha256_hash.hexdigest()
    # Encryption of the hashed data
    signature = rsa.encrypt(hashed_text.encode(), CA_private_key)
    return signature

def append_digital_signature(signature, text):
    DSC = text +"+"+ signature.hex()
    return DSC

def keys(key_dir):
    global public_key
    p2_file = os.path.join(key_dir, 'p2.pem')
    p1_file = os.path.join(key_dir, 'p1.pem')

    with open(p1_file, 'rb') as f:
        private_key_data = f.read()
        public_key = rsa.PrivateKey.load_pkcs1(private_key_data)

    with open(p2_file, 'rb') as f:
        private_key = rsa.PublicKey.load_pkcs1(f.read())

    return private_key

def CA(pdf):
    private_key = keys(key_dir)
    reader = PdfReader(pdf)
    page = reader.pages[0]
    text = page.extract_text()
    signature = generate_digital_signature(text, private_key)
    return signature, text

def client(file_contents):
    signed_text = file_contents
    signature_delimiter = "+"
    if signature_delimiter in signed_text:
        before_signature, after_signature = signed_text.split(signature_delimiter)
        after_signature = bytes.fromhex(after_signature)
        before_signature = before_signature.strip()


        sha256_hash = hashlib.sha256()
        sha256_hash.update(before_signature.encode('utf-8'))

        digest = sha256_hash.hexdigest()
        try:
            decoded_signature = rsa.decrypt(after_signature, public_key).decode()
        except rsa.pkcs1.DecryptionError:
            st.write("Signature cannot be decoded, Invalid Certificate or Server")
            return
        st.write(f"Decoded Hash: {decoded_signature}")
        st.write("The Hash of the content before signature is ", digest)
        if decoded_signature == digest:
            st.write("The Data in DSC is valid.")
        else:
            st.write("The Data in DSC is altered.")

    else:
        st.write("Invalid DSC text format. Signature delimiter not found.")

def main():
    st.title("Digital Signature Simulation")
    operation = st.radio("Select operation", ("Generate Digital Signature", "Verify Digital Signature"))
    x=keys(key_dir)

    if operation == "Generate Digital Signature":
        uploaded_file = st.file_uploader("Upload PDF file", type=['pdf'])
        if uploaded_file is not None:
            st.write("PDF file uploaded successfully!")
            st.write("Processing...")

            signature, text = CA(uploaded_file)
            st.write("Encryption output:")
            st.code(signature.hex())

            # Save signed document to specified directory
            output_file = r"D:\College\CSS\mini\DSC.txt"
            DSC = append_digital_signature(signature, text)
            with open(output_file, "w") as file:
                file.write(DSC)

            st.write("Digital Signature Component:")
            st.code(DSC)

            st.write("Signed document saved successfully to:", output_file)

    elif operation == "Verify Digital Signature":
        dsc_file = st.file_uploader("Upload DSC text file", type=['txt'])
        if dsc_file is not None:
            st.write("DSC text file uploaded successfully!")
            st.write("Verifying signature...")

            # Read the file contents
            with io.BytesIO(dsc_file.read()) as dsc_buffer:
                file_contents = dsc_buffer.getvalue().decode('utf-8')
            # Call the client function with the file contents
            client(file_contents)

if __name__ == "__main__":
    main()