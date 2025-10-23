---
id: d363c224-ae15-4e97-b80e-d9798e118c9d
name: openssl Remove Passphrase from RSA Key
type: command
executor: bash
data: openssl rsa -in $_PRIVATE_KEY.enc -out $_PRIVATE_KEY
output: 'root@hackers:~# openssl rsa -in id_rsa -out id_rsa_unencrypted

  Enter pass phrase for id_rsa:

  writing RSA key'
created_at: '2019-09-16T20:11:43.105485+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# openssl Remove Passphrase from RSA Key

```bash
openssl rsa -in $_PRIVATE_KEY.enc -out $_PRIVATE_KEY
```

## Expected Output

```
root@hackers:~# openssl rsa -in id_rsa -out id_rsa_unencrypted
Enter pass phrase for id_rsa:
writing RSA key
```


