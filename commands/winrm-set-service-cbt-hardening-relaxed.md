---
type: command
executor: powershell
data: 'winrm set winrm/config/service/auth @{CbtHardeningLevel="relaxed"}'
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - winrm
  - security
verified: true
validated: true
---

# winrm-set-service-cbt-hardening-relaxed

## Command

```powershell
winrm set winrm/config/service/auth @{CbtHardeningLevel="relaxed"}
```

## Description

Sets Channel Binding Token (CBT) hardening to 'relaxed' mode, accepting connections without strict token validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @{CbtHardeningLevel="relaxed"} | Options: Strict, Relaxed, None | Yes |

## Examples

### Basic Usage

```powershell
winrm set winrm/config/service/auth @{CbtHardeningLevel="relaxed"}
```

### Alternative: None

```powershell
winrm set winrm/config/service/auth @{CbtHardeningLevel="none"}
```

## Expected Output

CbtHardeningLevel = relaxed

## Related

- [[procedures/windows-remoting-via-winrm]]
- [[commands/winrm-get-service-config]]
