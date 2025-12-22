---
type: command
executor: powershell
data: Convert-NameToSid 'DOMAIN\krbtgt'
output: null
created_at: '2023-04-06T03:56:02.622089+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - sid-resolution
verified: true
validated: true
---

# convert-name-to-sid-powershell

## Command

```powershell
Convert-NameToSid 'DOMAIN\krbtgt'
```

## Description

This PowerShell command, from the ActiveDirectory module, translates a domain account name (user or group) to its Security Identifier (SID). It is ideal for resolving SIDs internally on domain-joined systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'DOMAIN\account' | The domain-qualified name to convert (e.g., DOMAIN\krbtgt) | Yes |

## Examples

### Basic Usage

```powershell
Convert-NameToSid 'high-sec-corp.local\krbtgt'
```

### Advanced Usage

For groups: `Convert-NameToSid 'DOMAIN\Domain Admins'`

## Expected Output

```
S-1-5-21-2941561648-383941485-1389968811-502
```

Returns the SID as a string.

## Related

- [[Related Procedure: Exploit-MS14-068-Kerberos-Checksum-Validation-for-AD-Privilege-Escalation]]
- [[commands/get-user-accounts-with-wmic]]
