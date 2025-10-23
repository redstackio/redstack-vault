---
id: 34533ddb-6ab6-4db2-aec1-95a8abb48363
name: Encrypt a Password with Cisco Type 7
type: command
executor: bash
data: python ciscot7.py -e -p '$_PASSWORD'
output: 'root@kali:~/Documents/ciscot7# python ciscot7.py -e -p ''secrets!''

  Encrypted password: 03175e08140a355f0f'
created_at: '2020-03-12T21:23:02.213528+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Encrypt a Password with Cisco Type 7

```bash
python ciscot7.py -e -p '$_PASSWORD'
```

## Expected Output

```
root@kali:~/Documents/ciscot7# python ciscot7.py -e -p 'secrets!'
Encrypted password: 03175e08140a355f0f
```


