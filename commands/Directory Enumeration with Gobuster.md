---
id: c3bf4c07-ff04-4633-bf7a-e800ad7876e1
name: Directory Enumeration with Gobuster
type: command
executor: bash
data: '# gobuster -w wordlist -u URL -t threads

  ./gobuster -u http://example.com/ -w words.txt -t 10'
output: null
created_at: '2023-04-06T03:56:21.812289+00:00'
updated_at: '2023-04-10T20:21:17.629553+00:00'
---

# Directory Enumeration with Gobuster

```bash
# gobuster -w wordlist -u URL -t threads
./gobuster -u http://example.com/ -w words.txt -t 10
```


