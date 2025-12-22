---
type: command
executor: bash
data: >-
  evil-winrm -i $_TARGET_IP -u $_USERNAME [-s $_SCRIPTS_PATH] [-e $_EXES_PATH]
  [-P $_PORT] [-p $_PASSWORD] [-H $_NTLM_HASH] [-U $_URL] [-S] [-c
  $_PUBLIC_KEY_PATH] [-k $_PRIVATE_KEY_PATH] [-r $_REALM]
output: null
platforms:
  - Windows
tags:
  - winrm
  - lateral-movement
  - advanced-auth
verified: true
validated: true
---

# evil-winrm-general-connect

## Command

```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME [-s $_SCRIPTS_PATH] [-e $_EXES_PATH] [-P $_PORT] [-p $_PASSWORD] [-H $_NTLM_HASH] [-U $_URL] [-S] [-c $_PUBLIC_KEY_PATH] [-k $_PRIVATE_KEY_PATH] [-r $_REALM]
```

## Description

Full syntax for evil-winrm connection, supporting script/exec paths, SSL, key auth, and multiple credential types for flexible remote access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i, --ip | Target IP | Yes |
| -u, --user | Username | Yes |
| -s, --scripts-path | Path to upload scripts | No |
| -e, --executables-path | Path to upload exes | No |
| -P, --port | WinRM port | No |
| -p, --password | Password | No |
| -H, --hash | NTLM hash | No |
| -U, --url | Basic auth URL | No |
| -S | Enable SSL | No |
| -c, --pub-key | Public key path | No |
| -k, --priv-key | Private key path | No |
| -r, --realm | Realm/domain | No |

## Examples

### With Script Upload

```bash
evil-winrm -i 10.0.0.20 -u admin -p pass -s /tmp/scripts
```

### Key-Based Auth

```bash
evil-winrm -i target -u user -c pubkey.pem -k privkey.pem -S
```

## Expected Output

Connection successful with shell prompt and any upload confirmations.

## Related

- [[procedures/windows-winrm-credential-access]]
- [[tools/Evil-WinRM]]
