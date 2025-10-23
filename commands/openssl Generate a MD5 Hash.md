---
id: b7369dd4-b1ac-46b6-b9ce-3a3c6165d65c
name: openssl Generate a MD5 Hash
type: command
executor: bash
data: openssl passwd -1 -salt $_SALT $_PASSWORD
output: 'root@hackers:~# openssl passwd -1 -salt 8BytesXX Thisisyourpassword

  $1$8BytesXX$dXGg2H2MnwNoiq6UuVkws/'
created_at: '2019-09-16T18:26:12.712980+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# openssl Generate a MD5 Hash

```bash
openssl passwd -1 -salt $_SALT $_PASSWORD
```

## Expected Output

```
root@hackers:~# openssl passwd -1 -salt 8BytesXX Thisisyourpassword
$1$8BytesXX$dXGg2H2MnwNoiq6UuVkws/
```


