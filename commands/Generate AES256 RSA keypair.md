---
id: 3c1f1a05-d4f4-4c8e-a965-db78ac8d2c97
name: Generate AES256 RSA keypair
type: command
executor: bash
data: openssl genrsa -aes256 -out $RSA_KEY 4096
output: 'root@kali:~# openssl genrsa -aes256 -out encrypted 4096

  Generating RSA private key, 4096 bit long modulus (2 primes)

  ........................................++++

  ..++++

  e is 65537 (0x010001)

  Enter pass phrase for encrypted:

  Verifying - Enter pass phrase for encrypted:'
created_at: '2019-09-16T23:41:09.220142+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Generate AES256 RSA keypair

```bash
openssl genrsa -aes256 -out $RSA_KEY 4096
```

## Expected Output

```
root@kali:~# openssl genrsa -aes256 -out encrypted 4096
Generating RSA private key, 4096 bit long modulus (2 primes)
........................................++++
..++++
e is 65537 (0x010001)
Enter pass phrase for encrypted:
Verifying - Enter pass phrase for encrypted:
```


