---
type: command
executor: cmd
data: winrm quickconfig
output: null
platforms:
  - Windows
tags:
  - winrm
  - remote-management
verified: true
validated: true
---

# winrm-quickconfig-enable

## Command

```cmd
winrm quickconfig
```

## Description

Enables the WinRM service for remote management on a Windows machine, configures the HTTP listener, and sets the firewall rule. Use this on the target to prepare for remote access sessions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; interactive prompt for confirmation | No |

## Examples

### Basic Usage

```cmd
winrm quickconfig
```

Respond 'y' to prompts. For non-interactive: winrm quickconfig -quiet -force.

### Advanced Usage

Enable HTTPS listener separately: winrm create winrm/config/Listener?Address=*+Transport=HTTPS @{Hostname="hostname";CertificateThumbprint="thumbprint"}

## Expected Output

WinRM is not set up to allow remote access to this machine for management.
The following changes must be made:

Create a WinRM listener on HTTP://* to accept WS-Man requests to any IP on this machine.
Enable the WinRM firewall exception.

Make these changes [y/n]? y

WinRM has been updated for remote management.

Created a WinRM listener on HTTP://* to accept WS-Man requests to any IP on this
machine.

WZCSVC Service is not running. The service may not function properly.

WinRM firewall exception enabled.

## Related

- [[procedures/windows-winrm-credential-access]]
- [[tools/Evil-WinRM]]
