---
type: command
executor: powershell
data: >-
  .\mimikatz\mimikatz.exe "kerberos::hash /password:AttackerServicePassword
  /user:AttackerService /domain:test.local" exit
tags:
  - mimikatz
  - kerberos
platforms:
  - Windows
verified: true
validated: true
---

# powershell-mimikatz-generate-kerberos-hash

## Command

```powershell
.\mimikatz\mimikatz.exe "kerberos::hash /password:$_PASSWORD /user:$_USERNAME /domain:$_DOMAIN" exit
```

## Description

Generates Kerberos hashes (NTLM/AES) from a plaintext password for account authentication in ticket requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /password:$_PASSWORD | Plaintext password | Yes |
| /user:$_USERNAME | Username/machine | Yes |
| /domain:$_DOMAIN | Target domain | Yes |

## Examples

### Basic Usage

```powershell
.\mimikatz\mimikatz.exe "kerberos::hash /password:AttackerServicePassword /user:AttackerService /domain:test.local" exit
```

## Expected Output

* Kerberos keys (e.g., NTLM: aad3b435b51404eeaad3b435b51404ee).

## Related

- [[procedures/Kerberos-Bronze-Bit-Attack]]
