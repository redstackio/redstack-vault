---
id: 489a037c-fe87-4878-8706-7417ca525dd1
name: turn-off-password-protected-sharing
type: command
executor: powershell
data: >-
  netsh advfirewall firewall set rule group="File and Printer Sharing" new
  enable=Yes; # Then manually turn off in Advanced Sharing Settings
output: null
created_at: '2023-04-06T03:56:29.907602+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - configuration
  - sharing
verified: true
validated: true
---

# turn-off-password-protected-sharing

## Command

```powershell
netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=Yes
# Followed by manual adjustment in Network and Sharing Center to turn off password protected sharing
```

## Description

Enables file and printer sharing firewall rules and disables password protection to allow anonymous access to printer shares for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| group="File and Printer Sharing" | Targets the sharing rules group | Yes |
| new enable=Yes | Enables the rules | Yes |

## Examples

### Basic Usage

```powershell
netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=Yes
```

### Advanced Usage

Disable specific rule: `netsh advfirewall firewall set rule name="File and Printer Sharing" new enable=No`

## Expected Output

"Ok." confirming firewall rule change. Manually verify in Control Panel > Network and Sharing Center > Advanced sharing settings > All Networks > Turn off password protected sharing.

## Related

- [[procedures/Printer-Spooler-Service-Elevation-of-Privilege]]
