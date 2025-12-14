---
id: cmd-copy-calc-dll-001
data: 'copy calc.dll c:\stage'
tags:
  - file-copy
type: command
output: 1 file(s) copied.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.942Z'
verified: false
validated: true
submitted: true
---
# copy-calc-dll-to-stage

## Command

```cmd
copy calc.dll c:\stage
```

## Description

Copies the compiled malicious DLL to the staging directory for OpenSSL config loading in curl attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `calc.dll` | Source file | Yes |
| `c:\stage` | Destination directory | Yes |

## Examples

### Basic Usage

```cmd
copy calc.dll c:\stage
```

## Expected Output

File copied successfully.

## Related

- [[commands/compile-calc-dll]]
