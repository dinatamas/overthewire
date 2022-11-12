#!/usr/bin/env python3
#
# Solve the Natas 11 -> 12 Wargame.
# https://medium.com/@n01s/solving-natas-11-df246fcf7828
#
import base64
import json

# Note: the %3D at the end was URL-encoded
data = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSQwt4RUULaAw='
data = base64.b64decode(data)

default_data = {'showpassword':'no', 'bgcolor':'#432423'}
# Note: PHP will not include a space after the comma.
json_encoded = json.dumps(default_data).replace(' ', '')

def xor(lhs, rhs):
    res = ''
    for i, l in enumerate(lhs):
        if i == len(rhs):
            break
        res += chr(l ^ rhs[i])
    return res

key = xor(map(ord, json_encoded), data)
# The original key was smaller, and was repeated.
key = 'qw8J'

default_data['showpassword'] = 'yes'
json_encoded = json.dumps(default_data).replace(' ', '')
# Repeat the key until the size of the new data.
key = (key * ((len(json_encoded) // len(key)) + 1))[:len(json_encoded)]

encrypted = xor(map(ord, key), list(map(ord, json_encoded)))
print(base64.b64encode(encrypted.encode()))
