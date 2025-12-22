---
type: command
executor: powershell
data: 'wmic useraccount get name,sid'
output: null
created_at: '2023-04-06T03:56:02.621965+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - sid-resolution
verified: true
validated: true
---

# get-user-accounts-with-wmic

## Command

```powershell
wmic useraccount get name,sid
```

## Description

This WMIC command queries the local system for all user accounts and their associated Security Identifiers (SIDs). It is effective for enumerating domain and local users on a compromised Windows host in an AD environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| get name,sid | Specifies fields to retrieve: account name and SID | Yes |

## Examples

### Basic Usage

```powershell
wmic useraccount get name,sid
```

### Advanced Usage

Pipe to file for offline analysis: `wmic useraccount get name,sid /format:csv > users.csv`

## Expected Output

```
Administrator  S-1-5-21-3415849876-833628785-5197346142-500   
Guest          S-1-5-21-3415849876-833628785-5197346142-501   
krbtgt         S-1-5-21-297520375-2634728305-5197346142-502   
lambda         S-1-5-21-297520375-2634728305-5197346142-1110 
```

Lists each account name followed by its SID.

## Related

- [[Related Procedure: Exploit-MS14-068-Kerberos-Checksum-Validation-for-AD-Privilege-Escalation]]
- [[commands/lookup-user-sid-with-rpcclient]]
