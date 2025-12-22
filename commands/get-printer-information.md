---
id: 2949ffae-667a-4a34-a3d4-bfa69c20c860
name: get-printer-information
type: command
executor: powershell
data: Get-Printer
output: null
created_at: '2023-04-06T03:56:29.907545+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - spooler
verified: true
validated: true
---

# get-printer-information

## Command

```powershell
Get-Printer
```

## Description

Retrieves a list of all printers installed on the system, including details like name, driver, and port, to verify spooler functionality before exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Lists all printers by default | No |

## Examples

### Basic Usage

```powershell
Get-Printer
```

### Advanced Usage

Filter by name: `Get-Printer | Where-Object {$_.Name -like "*Printer*"}`

## Expected Output

```
Name                           ComputerName    Type         DriverName             PortName
----                           ------------    ----         ----------             --------
Microsoft XPS Document Writer LOCAL            Local        Microsoft XPS Documen... PORTPROMPT:
Fax                            LOCAL            Local        Fax                    SHRFAX:
```

A table of printers confirms the spooler is active.

## Related

- [[procedures/Printer-Spooler-Service-Elevation-of-Privilege]]
