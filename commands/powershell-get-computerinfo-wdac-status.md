---
type: command
executor: powershell
data: Get-ComputerInfo
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - discovery
  - system-information
verified: true
validated: true
---

# powershell-get-computerinfo-wdac-status

## Command

```powershell
Get-ComputerInfo
```

## Description

This PowerShell cmdlet retrieves detailed information about the local computer, including hardware, OS, and security configurations like Windows Defender Application Control (WDAC) enforcement status. Use it during reconnaissance to assess defense mechanisms without installing tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The command runs without parameters to output all available info. For targeted output, pipe to Select-Object (e.g., Get-ComputerInfo | Select-Object DeviceGuard*). | No |

## Examples

### Basic Usage

```powershell
Get-ComputerInfo
```

### Advanced Usage

```powershell
Get-ComputerInfo | Select-Object -Property DeviceGuardCodeIntegrityPolicyEnforcementStatus, DeviceGuardUserModeCodeIntegrityPolicyEnforcementStatus
```

## Expected Output

The command produces a large object with sections on OS, BIOS, and security. Key WDAC indicators appear under DeviceGuard:

```
DeviceGuardCodeIntegrityPolicyEnforcementStatus         : EnforcementMode
DeviceGuardUserModeCodeIntegrityPolicyEnforcementStatus : EnforcementMode
```

Look for 'EnforcementMode' (active blocking), 'AuditMode' (logging only), or 'NotConfigured' (disabled). Full output may include hundreds of properties; use filtering for efficiency.

## Related

- [[procedures/Check-WDAC-Enforcement-Mode]]
