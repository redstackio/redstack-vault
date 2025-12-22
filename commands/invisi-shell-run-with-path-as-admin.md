---
id: a22ad289-c4c4-4f30-8967-235d4ea25391
name: invisi-shell-run-with-path-as-admin
type: command
executor: command_prompt
data: RunWithPathAsAdmin.bat
output: null
created_at: '2023-01-12T04:43:16.722826+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - powershell
verified: true
validated: true
---

# invisi-shell-run-with-path-as-admin

## Command

```command_prompt
RunWithPathAsAdmin.bat
```

## Description

This command executes the Invisi-Shell administrative launcher batch file from a CMD prompt with elevated privileges. It loads the Invisi-Shell DLL into the current process path, disabling PowerShell logging and AMSI for the session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The batch file has no command-line parameters; it runs with default settings assuming it's in the current directory. | N/A |

## Examples

### Basic Usage

```command_prompt
RunWithPathAsAdmin.bat
```

### Usage in Script

```command_prompt
cd C:\temp\invisi-shell\Invisi-Shell
RunWithPathAsAdmin.bat
powershell
```

## Expected Output

The command runs silently with no console output if successful. The CMD prompt returns immediately. Verify by launching PowerShell and checking for absent logs in Event Viewer.

## Related

- [[procedures/Bypass-PowerShell-Logging-with-Invisi-Shell]]
- [[tools/Invisi-Shell]]
