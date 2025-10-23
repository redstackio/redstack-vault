---
id: 537a0376-5bf2-4499-8229-1c3ef12d6deb
name: Generate Public Key from Private
type: command
executor: bash
data: openssl rsa -in $_KEY.priv -pubout > $_KEY.pub
output: 'root@kali:~# openssl rsa -in key -pubout > mykey.pub

  Enter pass phrase for key:

  writing RSA key'
created_at: '2019-11-04T21:31:41.679512+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Generate Public Key from Private

```bash
openssl rsa -in $_KEY.priv -pubout > $_KEY.pub
```

## Expected Output

```
root@kali:~# openssl rsa -in key -pubout > mykey.pub
Enter pass phrase for key:
writing RSA key
```


