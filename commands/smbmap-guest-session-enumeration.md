---
id: 7b52532a-4dab-47f7-8677-3509fc2f2711
type: command
executor: bash
data: smbmap -H $_TARGET_IP -u $_GUEST_USER
output: null
created_at: '2023-04-06T03:56:03.238070+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - discovery
  - smb
verified: true
validated: true
---

# smbmap-guest-session-enumeration

## Command

```bash
smbmap -H $_TARGET_IP -u $_GUEST_USER
```

## Description

Enumerates shares using a guest or invalid user session to bypass basic auth checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H | Target IP | Yes |
| -u | Username (e.g., invaliduser for guest) | Yes |
| $_TARGET_IP | Target IP | Yes |
| $_GUEST_USER | Dummy username like 'invaliduser' | Yes |

## Examples

### Basic Usage

```bash
smbmap -H 10.10.10.10 -u invaliduser
```

## Expected Output

Similar to null session but may reveal more if guest access is allowed:
```
[+] Guest session shares: Users, Public
```

## Related

- [[procedures/Open-Shares-Enumeration]]
- [[tools/SMBMap]]
