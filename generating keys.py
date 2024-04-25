import rsa
import os

def generate_keys(key_dir, key_size=1024):

    if not os.path.exists(key_dir):
        os.makedirs(key_dir)

    public_key, private_key = rsa.newkeys(key_size)

    public_key_file = os.path.join(key_dir, 'p2.pem')
    with open(public_key_file, 'wb') as f:
        f.write(public_key.save_pkcs1('PEM'))

    private_key_file = os.path.join(key_dir, 'p1.pem')
    with open(private_key_file, 'wb') as f:
        f.write(private_key.save_pkcs1('PEM'))

    print(f"Public and private keys have been generated and saved to {key_dir}")

key_directory = r"D:\College\CSS\mini proj\keys"
generate_keys(key_directory)