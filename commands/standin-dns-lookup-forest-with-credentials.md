---
type: command
executor: powershell
data: >-
  StandIn.exe --dns --forest --domain $_DOMAIN --user $_USERNAME --pass
  $_PASSWORD
tags:
  - dns-recon
  - active-directory
platforms:
  - Windows
verified: true
validated: true
---

# StandIn DNS Lookup Forest with Credentials

## Command

```powershell
StandIn.exe --dns --forest --domain $_DOMAIN --user $_USERNAME --pass $_PASSWORD
```

## Description

This command authenticates to a specified domain and queries ADIDNS across the entire Active Directory forest to enumerate comprehensive DNS records.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --dns | Enables DNS mode | Yes |
| --forest | Searches the full forest | Yes |
| --domain $_DOMAIN | Target domain name (e.g., redhook.local) | Yes |
| --user $_USERNAME | Authentication username | Yes |
| --pass $_PASSWORD | Authentication password | Yes |

## Examples

### Basic Usage

```powershell
StandIn.exe --dns --forest --domain redhook.local --user RFludd --pass Cl4vi$Alchemi4e
```

### Secure Password Handling

```powershell
$pass = ConvertTo-SecureString 'Cl4vi$Alchemi4e' -AsPlainText -Force
StandIn.exe --dns --forest --domain redhook.local --user RFludd --pass $pass
```

## Expected Output

Forest-wide DNS records, such as:

```
Forest DNS: dc01.child.redhook.local (A record)
Forest DNS: forest-root.com (NS record)
...
(Full forest scan complete)
```

Indicates broad visibility into multi-domain setups.

## Related

- [[procedures/dns-reconnaissance-using-standin-adidns-queries]]
- [[tools/standin]]
