---
type: command
executor: bash
data: hashcat -m 5600 -a 0 $_HASH_FILE $_WORDLIST
tags:
  - hash-cracking
  - credential-access
platforms:
  - Linux
verified: true
validated: true
---

# hashcat-crack-netntlmv2

## Command

```bash
hashcat -m 5600 -a 0 $_HASH_FILE $_WORDLIST
```

## Description

This command uses Hashcat to crack NetNTLMv2 hashes captured from NTLM relay attacks, performing a straight dictionary attack to recover plaintext passwords from Active Directory user accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -m 5600 | Hash mode for NetNTLMv2 | Yes |
| -a 0 | Attack mode: straight (dictionary) | Yes |
| $_HASH_FILE | Path to file containing NetNTLMv2 hashes (one per line) | Yes |
| $_WORDLIST | Path to dictionary wordlist file | Yes |

## Examples

### Basic Usage

```bash
hashcat -m 5600 -a 0 hashes.txt rockyou.txt
```

### Advanced Usage

```bash
hashcat -m 5600 -a 0 hashes.txt crackstation.txt -r rules/best64.rule
```

## Expected Output

Session progress:

Session..........: hashcat
Status...........: Running
Hash.Mode........: 5600 (NetNTLMv2)
...

Upon cracking:

<full_hash>:RecoveredPassword

Use hashcat --show hashes.txt to view all cracked passwords.

## Related

- [[procedures/Active-Directory-MitM-and-Password-Cracking]]
- [[tools/Hashcat]]
