---
data: 'msiexec /fa C:\Windows\Installer\installer_name.msi'
tags:
  - execution
  - msi
type: command
executor: cmd
platforms:
  - Windows
id: 33a8dd75-9a35-4c01-b4f4-289eb37e623f
created_at: '2025-12-14T17:29:44.270Z'
updated_at: '2025-12-14T17:29:44.270Z'
verified: false
validated: true
submitted: true
---
# msiexec /fa MSI Repair

## Command

```cmd
msiexec /fa C:\Windows\Installer\installer_name.msi
```

## Description

This command uses the Windows Installer (msiexec.exe) to force a repair (/fa) on the specified MSI package, reinstalling all components and creating temporary files like schedule.dll in %TEMP% for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /fa | Reinstalls all features (force all actions: repair) | Yes |
| C:\Windows\Installer\installer_name.msi | Path to the target MSI file (replace with actual GUID-based name) | Yes |

## Examples

### Basic Usage

```cmd
msiexec /fa C:\Windows\Installer\{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}.msi
```

### Advanced Usage

```cmd
msiexec /fa "{MSI_PATH}" /quiet
```

> The /quiet suppresses UI, but for exploitation, interactive mode is needed to handle UAC.

## Expected Output

The command launches MsiExec.exe; after a few seconds, a temporary folder appears in %TEMP% containing schedule.dll. The process may prompt UAC and complete with elevated DLL loading.

## Related

- [[Related Procedure: Initiate MSI Repair Process]]
