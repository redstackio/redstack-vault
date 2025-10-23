---
id: 19d59dda-7054-44b5-81b4-de2d8072e3e1
name: Hashcat Find Hash Mode from Example Hashes
type: command
executor: bash
data: hashcat --example-hashes | grep -C 2 $_VALUE
output: 'root@kali:~# hashcat --example-hashes | grep -C 2 ''\$6\$''


  MODE: 1800

  TYPE: sha512crypt $6$, SHA512 (Unix)

  HASH: $6$72820166$U4DVzpcYxgw7MVVDGGvB2/H5lRistD5.Ah4upwENR5UtffLR4X4SxSzfREv8z6wVl0jRFX40/KnYVvK4829kD1'
created_at: '2019-09-24T22:00:40.484250+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Hashcat Find Hash Mode from Example Hashes

```bash
hashcat --example-hashes | grep -C 2 $_VALUE
```

## Expected Output

```
root@kali:~# hashcat --example-hashes | grep -C 2 '\$6\$'

MODE: 1800
TYPE: sha512crypt $6$, SHA512 (Unix)
HASH: $6$72820166$U4DVzpcYxgw7MVVDGGvB2/H5lRistD5.Ah4upwENR5UtffLR4X4SxSzfREv8z6wVl0jRFX40/KnYVvK4829kD1
```


