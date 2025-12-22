---
type: code
language: powershell
verified: true
tags:
  - active-directory
  - discovery
  - trust-enumeration
platforms:
  - Windows
validated: true
---

# powershell-get-all-trust-relationships

## Code

```powershell
([System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()).GetAllTrustRelationships()

SourceName          TargetName                    TrustType      TrustDirection
----------          ----------                    ---------      --------------
domainA.local      domainB.local                  TreeRoot       Bidirectional
```

## Description

This PowerShell snippet queries the current Active Directory domain using .NET classes to retrieve all trust relationships. It outputs a table showing source and target domains, trust types (e.g., TreeRoot, Forest), and directions (e.g., Bidirectional, Inbound). Useful for mapping domain interconnections during reconnaissance.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | This code has no user-defined variables; it uses the current domain context automatically. | N/A |

## Usage

Run this in PowerShell on a domain-joined Windows machine with authenticated domain access. It requires the ActiveDirectory module implicitly via .NET. Integrate into scripts for automated trust discovery or use standalone to output to CSV for analysis: Add `| Export-Csv trusts.csv` at the end.

## Detection

- Monitor PowerShell execution logs (Event ID 4104) for .NET DirectoryServices calls.
- Audit AD object queries in Event ID 4662.
- Network traffic to domain controllers on LDAP ports (389/636) from unexpected hosts.

## Related

- [[procedures/Domain-Trust-Enumeration]]
- [[commands/nltest-list-trusted-domains]]
