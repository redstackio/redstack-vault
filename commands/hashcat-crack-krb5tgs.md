---
id: 114e3237-8af7-4594-8ddf-23b5e40effda
name: hashcat-crack-krb5tgs
type: command
executor: bash
data: hashcat -m 13100 -a 0 hash.txt password-list.txt
output: null
created_at: '2023-01-11T21:03:47.247233+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Windows
tags:
  - hashcat
  - kerberos
  - password-cracking
verified: true
validated: true
---

# hashcat-crack-krb5tgs

## Command

```bash
hashcat -m 13100 -a 0 $_HASH_FILE $_WORDLIST
```

## Description

This command uses Hashcat to perform a dictionary attack on a Kerberos 5 TGS hash in mode 13100 (TGS-REP etype 23). It is used offline after obtaining hashes from Kerberoasting to recover service account passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m 13100 | Hash mode for Kerberos 5 TGS-REP etype 23 (RC4) | Yes |
| -a 0 | Attack mode: Straight (dictionary) | Yes |
| $_HASH_FILE | Path to the hash file (e.g., hash.txt) | Yes |
| $_WORDLIST | Path to the password wordlist (e.g., rockyou.txt) | Yes |
| -O | Optimized kernel (faster on GPU) | No |
| --force | Ignore warnings (e.g., for OpenCL) | No |

## Examples

### Basic Usage

```bash
hashcat -m 13100 -a 0 hash.txt rockyou.txt
```

### Advanced Usage

```bash
hashcat -m 13100 -a 0 hash.txt rockyou.txt -O --session=krb5
```

## Expected Output

Session progress display:

```
Session..........: hashcat
Status...........: Running
Hash.Mode........: 13100 (Kerberos 5, TGS-REP etype 23)
...
[Cracked] $krb5tgs$23$*user$DOMAIN$service$... : Password123
```

If successful, the cracked password appears in the output or potfile (~/.hashcat/hashcat.potfile).

## Related

- [[procedures/Crack-Kerberos-5-TGS-Hash]]
- [[tools/Hashcat]]
