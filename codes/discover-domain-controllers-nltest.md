---
id: 29071edf-5d6a-4721-bece-d900632bec8d
name: discover-domain-controllers-nltest
type: code
language: cmd
verified: true
created_at: '2023-04-06T03:56:28.627097+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - domain
  - discovery
  - dc
validated: true
---

# discover-domain-controllers-nltest

## Code

```cmd
nltest /DCLIST:$_DOMAIN_NAME
nltest /DCNAME:$_DOMAIN_NAME
nltest /DSGETDC:$_DOMAIN_NAME
```

## Description

Batch of nltest commands to discover domain controllers: list all (/DCLIST), get authenticating DC (/DCNAME), and detailed info (/DSGETDC). Essential for mapping Active Directory infrastructure in domain environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_DOMAIN_NAME | Fully qualified domain name | contoso.com |

## Usage

Execute in CMD on a domain-joined machine to gather DC details for lateral movement, like targeting the PDC for replication attacks. Substitute $_DOMAIN_NAME before running.

## Detection

- Network logs for nltest traffic to port 389/445
- Event ID 4768/4771 for DC locator queries
- Command line auditing capturing nltest executions

## Related

- [[procedures/windows-user-enumeration-and-privilege-check]]
- [[commands/nltest-dclist-domain]]
