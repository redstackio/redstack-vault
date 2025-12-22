---
id: 8e84bac8-475b-407d-8cb2-915e23028ede
name: crackmapexec-get-user-descriptions-kdc
type: command
executor: bash
data: >-
  crackmapexec ldap $_DC_IP -u $_USERNAME -p $_PASSWORD --kdcHost $_DC_IP -M
  get-desc-users
output: null
created_at: '2023-04-06T03:56:04.400565+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - ad-enumeration
  - ldap
verified: true
validated: true
---

# crackmapexec-get-user-descriptions-kdc

## Command

```bash
crackmapexec ldap $_DC_IP -u $_USERNAME -p $_PASSWORD --kdcHost $_DC_IP -M get-desc-users
```

## Description

This command uses CrackMapExec's get-desc-users module to enumerate AD user descriptions, specifying the KDC host for direct DC targeting. Useful when domain resolution is unavailable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DC_IP | IP address of the domain controller | Yes |
| $_USERNAME | Domain username for authentication | Yes |
| $_PASSWORD | Password for the username | Yes |
| --kdcHost $_DC_IP | Specify KDC host | Yes |
| -M get-desc-users | Module for user description enumeration | Built-in |

## Examples

### Basic Usage

```bash
crackmapexec ldap 10.0.2.11 -u user -p pass --kdcHost 10.0.2.11 -M get-desc-users
```

## Expected Output

```
GET-DESC... 10.0.2.11       389    dc01    [+] Found following users:
GET-DESC... 10.0.2.11       389    dc01    User: krbtgt description: Key Distribution Center Service Account
```

## Related

- [[procedures/Enumerate-Passwords-in-AD-User-Descriptions]]
- [[commands/crackmapexec-enumerate-user-descriptions]]
