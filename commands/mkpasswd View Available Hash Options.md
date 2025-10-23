---
id: 8162e457-8625-4c94-ac4b-642ba513522b
name: mkpasswd View Available Hash Options
type: command
executor: bash
data: mkpasswd -m help
output: 'root@hackers:~# mkpasswd -m help

  Available methods:

  sha512crypt     SHA-512

  sha256crypt     SHA-256

  md5crypt        MD5

  descrypt        standard 56 bit DES-based crypt(3)'
created_at: '2019-09-16T18:26:12.739305+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# mkpasswd View Available Hash Options

```bash
mkpasswd -m help
```

## Expected Output

```
root@hackers:~# mkpasswd -m help
Available methods:
sha512crypt     SHA-512
sha256crypt     SHA-256
md5crypt        MD5
descrypt        standard 56 bit DES-based crypt(3)
```


