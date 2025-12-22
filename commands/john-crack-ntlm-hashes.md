---
id: 90069a0a-3d46-48ae-bd02-41dae054918e
name: john-crack-ntlm-hashes
type: command
executor: bash
data: john --format=NT $_HASH_FILE --wordlist=$_WORDLIST
output: null
created_at: '2023-04-06T03:55:58.670672+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - cracking
  - ntlm
verified: true
validated: true
---

# john-crack-ntlm-hashes

## Command

```bash
john --format=NT $_HASH_FILE --wordlist=$_WORDLIST
```

## Description

This command uses John the Ripper to crack NTLM hashes from a SAM dump in dictionary mode. The --format=NT specifies the NTLM hash format.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --format=NT | Hash format for NTLM | Yes |
| $_HASH_FILE | File with NTLM hashes (e.g., hashes.txt) | Yes |
| --wordlist=$_WORDLIST | Path to dictionary file (e.g., rockyou.txt) | Yes |

## Examples

### Basic Usage

```bash
john --format=NT hashes.txt --wordlist=rockyou.txt
```

### Advanced Usage

```bash
john --format=NT --wordlist=rockyou.txt --rules hashes.txt
```

## Expected Output

Progress and guesses:

```
Loaded 2 password hashes with no different salts (NT [MD4 128/128 SSE2 4x)]
...
Administrator     password123     (Administrator)
1g 0:00:00:05 DONE (2023-10-01 12:00) 20.00g/s 1234Kp/s 1234Kc/s 1234KC/s
```

Use `john --show hashes.txt` for cracked passwords.

## Related

- [[procedures/Windows-LFI-to-RCE-via-Credentials-Files]]
- [[commands/samdump2-extract-hashes-from-sam-system]]
