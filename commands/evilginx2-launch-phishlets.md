---
id: 1d17a65b-29c9-463c-a57d-2f3514b88e4b
name: evilginx2-launch-phishlets
type: command
executor: powershell
data: 'evilginx2 -p C:\Tools\evilginx2\phishlets'
output: null
created_at: '2023-05-24T03:35:02.203970+00:00'
updated_at: '2023-05-24T03:35:02.314062+00:00'
platforms:
  - Windows
tags:
  - phishing
  - evilginx2
verified: true
validated: true
---

# evilginx2-launch-phishlets

## Command

```powershell
evilginx2 -p C:\Tools\evilginx2\phishlets
```

## Description

Launches the Evilginx2 interactive shell, specifying the directory containing phishlet templates for services like O365/Azure. Use this to initialize the framework before configuring phishing attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p | Path to the phishlets directory | Yes |
| C:\Tools\evilginx2\phishlets | Example path; adjust to your installation | Yes |

## Examples

### Basic Usage

```powershell
evilginx2 -p C:\Tools\evilginx2\phishlets
```

### Advanced Usage

If phishlets are in a different location:

```powershell
evilginx2 -p /opt/evilginx2/phishlets
```

## Expected Output

The Evilginx2 console starts with a prompt like ": " indicating the interactive shell is ready. No errors should appear if the path is valid.

## Related

- [[procedures/Azure-Phishing-with-Evilginx2]]
- [[tools/Evilginx2]]
