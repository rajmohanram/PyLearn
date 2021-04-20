# Secure hash and message digest
# hash algorithms SHA1, SHA224, SHA256, SHA384, and SHA512 and  RSA’s MD5
import hashlib
import binascii


# function to calculate md5
def find_md5(msg):
    md5_digest = hashlib.md5(msg).hexdigest()
    print(f'\nMessage: {msg.decode("utf-8")}')
    print(f'Digest value: {md5_digest}')
    print(bin(int(md5_digest, 16))[2:].zfill(128))
    print(f'Digest length: {len(bin(int(md5_digest, 16))[2:].zfill(128))}')


# function to calculate hash value
def find_hash(msg):
    m = hashlib.sha256()
    m.update(msg)
    secure_hash = m.hexdigest()
    print(f'\nMessage: {msg.decode("utf-8")}')
    print(f'Hash value: {secure_hash}')
    print(bin(int(secure_hash, 16))[2:].zfill(256))
    print(f'Hash length: {len(bin(int(secure_hash, 16))[2:].zfill(256))}')


if __name__ == "__main__":
    find_hash(b"This is a plain text message.")
    find_hash(b"This is a plain text massage.")

    find_md5(b"This is a plain text message")