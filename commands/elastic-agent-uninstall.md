---
id: d38028a2-71a5-4654-b1e5-b289331bd981
name: elastic-agent-uninstall
type: command
executor: powershell
data: 'cd "C:\Program Files\Elastic\Agent"; .\elastic-agent.exe uninstall'
output: null
created_at: '2023-04-06T03:56:27.632701+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - antivirus-removal
  - defense-evasion
verified: true
validated: true
---

# elastic-agent-uninstall

## Command

```powershell
cd "C:\Program Files\Elastic\Agent"; .\elastic-agent.exe uninstall
```

## Description

Uninstalls the Elastic Agent from a Windows system by changing to its installation directory and running the built-in uninstaller. This removes endpoint monitoring capabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses default installation path; customize cd if non-standard | No |

## Examples

### Basic Usage

```powershell
cd "C:\Program Files\Elastic\Agent"; .\elastic-agent.exe uninstall
```

### With Confirmation

When prompted, enter 'Y' to confirm uninstallation.

## Expected Output

```
Elastic Agent will be uninstalled from your system at C:\Program Files\Elastic\Agent. Do you want to continue? [Y/n]: Y
Elastic Agent has been uninstalled.
```

Success is confirmed by the agent services stopping and files being removed from the directory.

## Related

- [[procedures/disable-elastic-agent-and-cortex-xdr-on-windows]]
