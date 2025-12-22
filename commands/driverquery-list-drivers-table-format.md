---
id: 597a616d-f33e-4676-bf3e-e50318863a7c
name: driverquery-list-drivers-table-format
type: command
executor: cmd
data: driverquery.exe /fo table /si
output: null
created_at: '2023-04-06T03:56:29.800602+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - drivers
verified: true
validated: true
---

# driverquery-list-drivers-table-format

## Command

```cmd
driverquery.exe /fo table /si
```

## Description

This command uses the built-in Windows driverquery.exe to list all installed drivers in a formatted table, including digital signature information. It is useful for initial reconnaissance during privilege escalation to identify third-party drivers that may be vulnerable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /fo table | Specifies table format for output (alternatives: csv, list) | Yes |
| /si | Includes signature information for each driver | Yes |

## Examples

### Basic Usage

```cmd
driverquery.exe /fo table /si
```

### Redirect to File

```cmd
driverquery.exe /fo table /si > all_drivers.txt
```

## Expected Output

```
Module Name  Display Name           Driver Type   Link Date             Signer
============ ====================== ============= ====================== ========
1394ohci     1394 OHCI Compliant Ho Kernel        12/10/2006 4:44:38 PM Microsoft Windows
3ware        3ware                  Kernel        5/18/2015 6:28:03 PM Unknown
ACPI         Microsoft ACPI Driver  Kernel        12/9/1975 6:17:08 AM Microsoft Windows
<SNIP>
```

A table listing drivers with details; look for 'Unknown' or non-Microsoft signers indicating potential targets.

## Related

- [[procedures/windows-privilege-escalation-evaluating-vulnerable-drivers]]
- [[tools/OffensiveCSharp-DriverQuery]]
