# Digital Certificate Simulation

This project is a comprehensive system designed to emulate the process of digitally signing and verifying PDF certificates for secure online transactions or document authentication. It uses a Streamlit web application to perform operations such as generating digital signatures and verifying them.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Contributing](#contributing)


## Introduction

In this simulation, a digital certificate in PDF format is taken as input. The certificate's contents are hashed to generate a unique digital fingerprint, ensuring the integrity of the document. This hash is then encrypted using a private key, creating a digital signature that uniquely identifies the sender and guarantees the authenticity of the document.

Upon receiving the signed PDF certificate, the client-side application decodes the signature using the corresponding public key. It then hashes the original contents of the PDF to generate another fingerprint. Finally, it compares this new hash with the decrypted signature to verify the integrity and authenticity of the document.

## Features

- **Digital Certificate Input**: Accepts a digital certificate in PDF format as input.
- **Hashing**: Generates a unique digital fingerprint of the certificate's contents.
- **Digital Signature Creation**: Encrypts the hash using a private key to create a digital signature.
- **Signature Verification**: Decodes the signature using a public key and verifies the integrity and authenticity of the document by comparing hashes.

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- PyPDF
- rsa
- hashlib

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/digital-certificate-simulation.git
    cd digital-certificate-simulation
    ```

2. Install the required packages:
    ```sh
    pip install streamlit pypdf rsa
    ```

3. Generate RSA keys and place them in the specified directory (`path\to\your\directory\keys`):
    ```sh
    openssl genpkey -algorithm RSA -out p2.pem
    openssl rsa -pubout -in p2.pem -out p1.pem
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. **Generate Digital Signature**:
    - Upload a PDF file to the application.
    - The application will process the PDF, generate a digital signature, and save the signed document as a text file.

3. **Verify Digital Signature**:
    - Upload the signed text file (DSC) to the application.
    - The application will verify the digital signature and display the results.

## Code Explanation

- **generate_digital_signature**: Generates a hash of the input text and encrypts it using a private key to create a digital signature.
- **append_digital_signature**: Appends the digital signature to the original text.
- **keys**: Loads the RSA private and public keys from the specified directory.
- **CA**: Reads the PDF, extracts text, and generates a digital signature.
- **client**: Verifies the digital signature by comparing the hash of the original text with the decrypted signature.
- **main**: Streamlit application entry point, handles file uploads and operations.


## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/my-feature`.
3. Commit your changes: `git commit -m 'Add my feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Open a pull request.

