---
id: 34d33e60-c55a-44ea-81a9-bebf85df269b
name: bruteforce web parameter
type: command
executor: bash
data: 'wfuzz -u http://target-ip/path/index.php?param=FUZZ -w /usr/share/wordlists/rockyou.txt

  '
output: null
created_at: '2020-07-14T18:15:01.552479+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# bruteforce web parameter

```bash
wfuzz -u http://target-ip/path/index.php?param=FUZZ -w /usr/share/wordlists/rockyou.txt

```


