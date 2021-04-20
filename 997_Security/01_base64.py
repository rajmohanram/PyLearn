# base64 encoding of binary octet stream
import base64

# actual data
data = b'rajmohan'
print(f'Actual data is {data.decode("utf-8")}')

# base64 encoded data
encoded_data = base64.b64encode(data)
print(f'Encoded data is {encoded_data.decode("utf-8")}')

# base64 decoded data
decoded_data = base64.b64decode(encoded_data)
print(f'Decoded data is {decoded_data.decode("utf-8")}')