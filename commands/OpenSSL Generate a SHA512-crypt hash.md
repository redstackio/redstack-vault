---
id: 2bd706ab-9af5-49d6-b806-40945e6a6620
name: OpenSSL Generate a SHA512-crypt hash
type: command
executor: bash
data: openssl passwd -6 -salt $_SALT $_PASSWORD
output: 'root@kali:~# openssl passwd -6 -salt 12345678 secretpass

  $6$12345678$DgaVYkZjVTY58m0juyhsvwGEjwMI9RB5U0U63JEP2as7KF/gNTboh3MC6aE8CjcVHmb1Er9RWwbRQmaHhBUfs/'
created_at: '2019-09-30T20:17:07.170333+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# OpenSSL Generate a SHA512-crypt hash

```bash
openssl passwd -6 -salt $_SALT $_PASSWORD
```

## Expected Output

```
root@kali:~# openssl passwd -6 -salt 12345678 secretpass
$6$12345678$DgaVYkZjVTY58m0juyhsvwGEjwMI9RB5U0U63JEP2as7KF/gNTboh3MC6aE8CjcVHmb1Er9RWwbRQmaHhBUfs/
```


