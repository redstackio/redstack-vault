---
type: command
executor: powershell
data: StandIn.exe --dns --limit 20
tags:
  - dns-recon
  - active-directory
platforms:
  - Windows
verified: true
validated: true
---

# StandIn DNS Lookup with Limit 20

## Command

```powershell
StandIn.exe --dns --limit 20
```

## Description

This command performs an ADIDNS query using StandIn to enumerate up to 20 DNS records in the current domain, providing a quick overview of network topology without excessive output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --dns | Enables DNS record querying mode | Yes |
| --limit 20 | Restricts results to 20 entries | Yes |

## Examples

### Basic Usage

```powershell
StandIn.exe --dns --limit 20
```

### With Output Redirection

```powershell
StandIn.exe --dns --limit 20 > dns_output.txt
```

## Expected Output

A list of DNS records, such as:

```
DNS Record 1: dc01.redhook.local (A record)
DNS Record 2: sqlserver.redhook.local (SRV record)
...
(Total: 15 records found)
```

Success is indicated by enumerated records showing domain infrastructure. Empty output may indicate permission issues.

## Related

- [[procedures/dns-reconnaissance-using-standin-adidns-queries]]
- [[tools/standin]]
