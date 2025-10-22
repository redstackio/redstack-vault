---
id: 11611631-8941-4405-bb40-96a74cb20144
name: mkpasswd Generate a SHA512-crypt hash
type: command
executor: ''
data: mkpasswd -m sha512crypt -S $_SALT $_PASSWORD
output: 'root@kali:~# mkpasswd -m sha512crypt -S 12345678 secretpass

  $6$12345678$DgaVYkZjVTY58m0juyhsvwGEjwMI9RB5U0U63JEP2as7KF/gNTboh3MC6aE8CjcVHmb1Er9RWwbRQmaHhBUfs/'
created_at: '2019-09-30T20:17:07.157380+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# mkpasswd Generate a SHA512-crypt hash

```bash
mkpasswd -m sha512crypt -S $_SALT $_PASSWORD
```

## Expected Output

```
root@kali:~# mkpasswd -m sha512crypt -S 12345678 secretpass
$6$12345678$DgaVYkZjVTY58m0juyhsvwGEjwMI9RB5U0U63JEP2as7KF/gNTboh3MC6aE8CjcVHmb1Er9RWwbRQmaHhBUfs/
```
