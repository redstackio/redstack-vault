---
id: 3e6bb2fd-f245-4809-9e9c-021ce92aa72f
name: hashcat-crack-ntlm-hashes
type: command
executor: bash
data: hashcat -m 1000 -a 0 $_HASH_FILE $_WORDLIST
output: null
created_at: '2023-04-06T03:55:58.670566+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - cracking
  - ntlm
verified: true
validated: true
---

# hashcat-crack-ntlm-hashes

## Command

```bash
hashcat -m 1000 -a 0 $_HASH_FILE $_WORDLIST
```

## Description

This command cracks NTLM hashes from a Windows SAM dump using Hashcat in dictionary attack mode (-a 0). Mode 1000 specifies NTLM v1/v2 hashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m 1000 | Hash mode for NTLM | Yes |
| -a 0 | Attack mode: straight dictionary | Yes |
| $_HASH_FILE | File containing NTLM hashes (e.g., hashes.txt) | Yes |
| $_WORDLIST | Path to wordlist (e.g., rockyou.txt) | Yes |

## Examples

### Basic Usage

```bash
hashcat -m 1000 -a 0 hashes.txt rockyou.txt
```

### Advanced Usage

```bash
hashcat -m 1000 -a 0 --increment --increment-min=8 hashes.txt rockyou.txt
```

## Expected Output

Session progress and cracked results:

```
Session..........: hashcat
Status...........: Cracked
...
Administrator:password123
```

Use `hashcat --show hashes.txt` to view all cracked passwords.

## Related

- [[procedures/Windows-LFI-to-RCE-via-Credentials-Files]]
- [[commands/samdump2-extract-hashes-from-sam-system]]
