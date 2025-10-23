---
id: e5f3c57e-34be-470f-8101-3eb13a524584
name: ssh2john Extract the Hash from an Encrypted SSH Private Key
type: command
executor: bash
data: python ssh2john.py $_PRIVATE_KEY.enc > $_OUTPUT.txt
output: root@kali:~# python /usr/share/john/ssh2john.py id_rsa.enc > hash.txt
created_at: '2019-10-25T19:09:24.118813+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# ssh2john Extract the Hash from an Encrypted SSH Private Key

```bash
python ssh2john.py $_PRIVATE_KEY.enc > $_OUTPUT.txt
```

## Expected Output

```
root@kali:~# python /usr/share/john/ssh2john.py id_rsa.enc > hash.txt
```


