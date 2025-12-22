---
id: 54e8e5d3-a5db-47ed-ae1c-2828cfaf0670
name: john-crack-asrep-hash
type: command
executor: bash
data: john --wordlist=$_WORDLIST.txt --format=krb5asrep $_HASH_FILE.txt
output: null
created_at: '2023-01-12T00:17:16.435843+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - john
  - cracking
verified: true
validated: true
---

# john-crack-asrep-hash

## Command

```bash
john --wordlist=$_WORDLIST.txt --format=krb5asrep $_HASH_FILE.txt
```

## Description

This command uses John the Ripper to crack AS-REP hashes in krb5asrep format via dictionary attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --wordlist=$_WORDLIST.txt | Path to dictionary file | Yes |
| --format=krb5asrep | Hash format for AS-REP | Yes |
| $_HASH_FILE.txt | Input hash file | Yes |

## Examples

### Basic Usage

```bash
john --wordlist=rockyou.txt --format=krb5asrep hashes.txt
```

### Advanced Usage

Incremental mode: `john --format=krb5asrep --incremental hashes.txt`

## Expected Output

`Loaded 1 password hash (krb5asrep, Kerberos 5 AS-REP etype 23 [RC4-HMAC])
password123     (username)
1g 0:00:00:02 DONE (2023-01-01 12:00) 0.5g/s 1234Kp/s 1234Kc/s 1234KC/s foo..bar
`

Use `john --show --format=krb5asrep hashes.txt` for results.

## Related

- [[procedures/Crack-AS-REP-Hash-Using-Hashcat-or-John]]
- [[tools/John-the-Ripper]]
