---
type: command
executor: powershell
data: StandIn.exe --dns --filter SQL --limit 10
tags:
  - dns-recon
  - active-directory
platforms:
  - Windows
verified: true
validated: true
---

# StandIn DNS Lookup with SQL Filter and Limit 10

## Command

```powershell
StandIn.exe --dns --filter SQL --limit 10
```

## Description

This command queries ADIDNS for DNS records containing 'SQL' (e.g., SQL servers), limited to 10 results, to identify database-related services in the domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --dns | Activates DNS querying | Yes |
| --filter SQL | Filters records matching the keyword 'SQL' | Yes |
| --limit 10 | Caps results at 10 | Yes |

## Examples

### Basic Usage

```powershell
StandIn.exe --dns --filter SQL --limit 10
```

### Combined with File Output

```powershell
StandIn.exe --dns --filter SQL --limit 10 | Tee-Object -FilePath filtered_dns.txt
```

## Expected Output

Filtered DNS entries, for example:

```
Filtered DNS Record: sql01.redhook.local (A: 10.0.0.50)
Filtered DNS Record: _ldap._tcp.sql.redhook.local (SRV)
...
(3 matches found)
```

Look for service locations; no matches suggest absence of SQL infrastructure.

## Related

- [[procedures/dns-reconnaissance-using-standin-adidns-queries]]
- [[tools/standin]]
