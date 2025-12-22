---
id: 93030853-8ca6-411f-894e-2da3480f9d9c
name: john-crack-krb5tgs
type: command
executor: bash
data: john $_HASH_FILE --format=krb5tgs --wordlist=$_WORDLIST
output: null
created_at: '2023-01-11T21:03:47.247694+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
tags:
  - john
  - kerberos
  - password-cracking
verified: true
validated: true
---

# john-crack-krb5tgs

## Command

```bash
john $_HASH_FILE --format=krb5tgs --wordlist=$_WORDLIST
```

## Description

This command uses John the Ripper to crack a Kerberos 5 TGS hash in krb5tgs format via a dictionary attack. It is an alternative to Hashcat for CPU-based cracking of Kerberoasted hashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_HASH_FILE | Path to the hash file (e.g., hash.txt) | Yes |
| --format=krb5tgs | Specify format for Kerberos 5 TGS hashes | Yes |
| --wordlist=$_WORDLIST | Path to the password dictionary (e.g., rockyou.txt) | Yes |
| -incremental | Switch to incremental mode after wordlist | No |
| --fork | Parallel cracking on multi-core | No |

## Examples

### Basic Usage

```bash
john hash.txt --format=krb5tgs --wordlist=rockyou.txt
```

### Advanced Usage

```bash
john hash.txt --format=krb5tgs --wordlist=rockyou.txt --fork=4
```

## Expected Output

Progress display:

```
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [RC4 HMAC])
...
Password123      (user)
1g 0:00:00:05 DONE (2023-01-01 12:00) 0.2g/s 1234Kp/s 1234Kc/s 1234KC/s
Use the "--show" option to display all of the cracked passwords reliably
```

View cracked passwords with: john --show --format=krb5tgs hash.txt

## Related

- [[procedures/Crack-Kerberos-5-TGS-Hash]]
- [[tools/John-the-Ripper]]
