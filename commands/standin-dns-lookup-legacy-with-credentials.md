---
type: command
executor: powershell
data: >-
  StandIn.exe --dns --legacy --domain $_DOMAIN --user $_USERNAME --pass
  $_PASSWORD
tags:
  - dns-recon
  - active-directory
platforms:
  - Windows
verified: true
validated: true
---

# StandIn DNS Lookup Legacy with Credentials

## Command

```powershell
StandIn.exe --dns --legacy --domain $_DOMAIN --user $_USERNAME --pass $_PASSWORD
```

## Description

This command uses legacy authentication to query ADIDNS records in the specified domain, targeting older Active Directory configurations that support NTLM or similar protocols.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --dns | DNS querying mode | Yes |
| --legacy | Enables legacy authentication | Yes |
| --domain $_DOMAIN | Domain to authenticate against | Yes |
| --user $_USERNAME | Username for legacy auth | Yes |
| --pass $_PASSWORD | Password for legacy auth | Yes |

## Examples

### Basic Usage

```powershell
StandIn.exe --dns --legacy --domain redhook.local --user RFludd --pass Cl4vi$Alchemi4e
```

### With Verbose Logging

```powershell
StandIn.exe --dns --legacy --domain redhook.local --user RFludd --pass Cl4vi$Alchemi4e -v
```

## Expected Output

Legacy-compatible DNS records, e.g.:

```
Legacy DNS: legacy-dc.redhook.local (A: 10.0.0.10)
Legacy DNS: _kerberos._tcp.legacy.redhook.local (SRV)
...
(Legacy query successful)
```

Useful for detecting outdated systems.

## Related

- [[procedures/dns-reconnaissance-using-standin-adidns-queries]]
- [[tools/standin]]
