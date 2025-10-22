---
id: 35418129-6db0-4200-babf-9da2688d3366
name: ciscot7.py Decrypt a Cisco Type 7 Password
type: command
executor: bash
data: python ciscot7.py -d -p $_PASSWORD
output: 'root@kali:~/ciscot7# python3 ciscot7.py -d -p 01000307490e121c60

  Decrypted password: secrets!'
created_at: '2019-12-18T20:24:02.189332+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# ciscot7.py Decrypt a Cisco Type 7 Password

```bash
python ciscot7.py -d -p $_PASSWORD
```

## Expected Output

```
root@kali:~/ciscot7# python3 ciscot7.py -d -p 01000307490e121c60
Decrypted password: secrets!
```
