---
id: 40970bc8-a8d7-4448-9164-1591fc573ddb
name: crackmapexec-enumerate-user-descriptions
type: command
executor: bash
data: crackmapexec ldap $_DOMAIN -u $_USERNAME -p $_PASSWORD -M user-desc
output: null
created_at: '2023-04-06T03:56:04.400504+00:00'
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

# crackmapexec-enumerate-user-descriptions

## Command

```bash
crackmapexec ldap $_DOMAIN -u $_USERNAME -p $_PASSWORD -M user-desc
```

## Description

This command uses CrackMapExec to enumerate Active Directory user descriptions via authenticated LDAP queries. It helps identify passwords stored in description fields during credential discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain name (e.g., lab.local) | Yes |
| $_USERNAME | Domain username for authentication | Yes |
| $_PASSWORD | Password for the username | Yes |
| -M user-desc | Module to enumerate user descriptions | Built-in |

## Examples

### Basic Usage

```bash
crackmapexec ldap lab.local -u user -p pass -M user-desc
```

### With Specific DC

```bash
crackmapexec ldap 10.0.2.11 -u user -p pass -M user-desc
```

## Expected Output

```
USER-DESC    lab.local:389  dc01 [+] Found following users:
USER-DESC    lab.local:389  dc01 User: admin description: Password: Secret123
```

## Related

- [[procedures/Enumerate-Passwords-in-AD-User-Descriptions]]
- [[commands/crackmapexec-get-user-descriptions-kdc]]
