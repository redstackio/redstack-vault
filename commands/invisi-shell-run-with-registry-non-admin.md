---
id: 96f63e94-83ea-4f98-8f30-038abef95d7a
name: invisi-shell-run-with-registry-non-admin
type: command
executor: command_prompt
data: RunWithRegistryNonAdmin.bat
output: null
created_at: '2023-01-12T04:43:16.722147+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - powershell
verified: true
validated: true
---

# invisi-shell-run-with-registry-non-admin

## Command

```command_prompt
RunWithRegistryNonAdmin.bat
```

## Description

This command runs the Invisi-Shell non-administrative launcher batch file from a CMD prompt. It modifies the registry to load the Invisi-Shell DLL, bypassing PowerShell security features without requiring elevation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; assumes batch file is in the working directory. | N/A |

## Examples

### Basic Usage

```command_prompt
RunWithRegistryNonAdmin.bat
```

### Usage in Script

```command_prompt
cd C:\temp\invisi-shell\Invisi-Shell
RunWithRegistryNonAdmin.bat
powershell
```

## Expected Output

Silent execution with no output on success. The prompt returns, and the bypass is active for subsequent PowerShell launches. Check registry keys under HKCU\Software\Microsoft\Windows\CurrentVersion\Run for modifications if needed.

## Related

- [[procedures/Bypass-PowerShell-Logging-with-Invisi-Shell]]
- [[tools/Invisi-Shell]]
