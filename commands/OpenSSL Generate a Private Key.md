---
id: 87485eda-ee4c-4049-87ea-330d3f3841b8
name: OpenSSL Generate a Private Key
type: command
executor: ''
data: openssl genrsa -out $_KEY 4096
output: 'root@kali:~# openssl genrsa -out id_rsa 4096

  Generating RSA private key, 4096 bit long modulus (2 primes)

  .................................++++

  ................................................................................................................................

  .....++++

  e is 65537 (0x010001)'
created_at: '2019-09-30T19:48:33.637832+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# OpenSSL Generate a Private Key

```bash
openssl genrsa -out $_KEY 4096
```

## Expected Output

```
root@kali:~# openssl genrsa -out id_rsa 4096
Generating RSA private key, 4096 bit long modulus (2 primes)
.................................++++
................................................................................................................................
.....++++
e is 65537 (0x010001)
```
