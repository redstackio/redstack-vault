---
id: f33b5dea-2d7d-47b3-a674-b8c90bf7bf4f
type: command
executor: bash
data: smbmap -H $_TARGET_IP -d $_DOMAIN -u $_USERNAME -p $_PASSWORD
output: null
created_at: '2023-04-06T03:56:03.238094+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - discovery
  - smb
verified: true
validated: true
---

# smbmap-domain-credentials-enumeration

## Command

```bash
smbmap -H $_TARGET_IP -d $_DOMAIN -u $_USERNAME -p $_PASSWORD
```

## Description

Enumerates shares using domain credentials for authenticated access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H | Target IP | Yes |
| -d | Domain name | Yes |
| -u | Username | Yes |
| -p | Password | Yes |
| $_TARGET_IP | Target IP | Yes |
| $_DOMAIN | e.g., DOMAIN.LOCAL | Yes |
| $_USERNAME | Domain user | Yes |
| $_PASSWORD | User password | Yes |

## Examples

### Basic Usage

```bash
smbmap -H 10.10.10.10 -d DOMAIN.LOCAL -u USERNAME -p Password123*
```

## Expected Output

```
[+] Authenticated shares: SYSVOL (rw), Users (ro)
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/SMBMap]]
