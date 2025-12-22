---
id: 7c3014e4-49eb-41f5-838a-a3a747764401
name: mpcmdrun-remove-definitions
type: command
executor: cmd
data: '"C:\Program Files\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All'
output: |-
  Removing definitions...
  Definitions removed successfully.
created_at: '2020-07-14T18:21:25.398243+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - antivirus-bypass
verified: true
validated: true
---

# mpcmdrun-remove-definitions

## Command

```cmd
"C:\Program Files\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All
```

## Description

This command uses the Windows Defender command-line tool to remove all virus and security definitions, impairing the antivirus's ability to detect threats. Ideal when PowerShell is blocked; requires elevated Command Prompt.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -RemoveDefinitions | Initiates removal of Defender definitions | Yes |
| -All | Removes all definition types (AV, ASB, etc.) | Yes |

## Examples

### Basic Usage

```cmd
"C:\Program Files\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All
```

### Advanced Usage

```cmd
"C:\Program Files\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All -MM
```

## Expected Output

Removing definitions...
Definitions removed successfully.

The process may take several minutes; success is confirmed by a completion message. Check the MpCmdRun.log for details.

## Related

- [[procedures/Disable-Windows-Defender]]
