---
id: e261d8a5-bb8d-4a2c-a950-8596b6c0c31c
name: crack ssh keys
type: command
executor: bash
data: '/usr/share/john/ssh2john.py id_rsa > hash.john

  john --wordlist=/usr/share/wordlists/rockyou.txt hash.john

  '
output: null
created_at: '2020-07-14T18:14:51.372451+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# crack ssh keys

```bash
/usr/share/john/ssh2john.py id_rsa > hash.john
john --wordlist=/usr/share/wordlists/rockyou.txt hash.john

```


