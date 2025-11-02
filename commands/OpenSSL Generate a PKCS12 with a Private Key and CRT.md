---
id: 570de42e-6634-4e21-a797-2044baa13f40
name: OpenSSL Generate a PKCS12 with a Private Key and CRT
type: command
executor: ''
data: openssl pkcs12 -export -out $_PKCS12.pfx -inkey $_PRIVATE_KEY -in $_SIGNED_CRT
output: "root@kali:~# openssl pkcs12  -export -out test1.pfx -inkey private.key -in\
  \ signed.crt \nEnter Export Password:\nVerifying - Enter Export Password:"
created_at: '2019-09-30T19:48:33.639137+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[openssl]]'
---

# OpenSSL Generate a PKCS12 with a Private Key and CRT

```bash
openssl pkcs12 -export -out $_PKCS12.pfx -inkey $_PRIVATE_KEY -in $_SIGNED_CRT
```

## Expected Output

```
root@kali:~# openssl pkcs12  -export -out test1.pfx -inkey private.key -in signed.crt 
Enter Export Password:
Verifying - Enter Export Password:
```


