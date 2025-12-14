---
id: cmd-copy-to-c-root
data: 'copy program.exe C:\'
tags:
  - file-copy
  - exploitation
type: command
output: 1 file(s) copied.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.486Z'
verified: false
validated: true
submitted: true
---
# copy-file-to-root

## Command

```cmd
copy program.exe C:\
```

## Description

Copies a file named 'program.exe' from the current directory to the C:\ root, enabling path hijacking exploits where processes search for executables in unexpected locations like the system root.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| source | Path to source file (e.g., program.exe) | Yes |
| destination | Target directory (e.g., C:\) | Yes |

## Examples

### Basic Usage

```cmd
copy program.exe C:\
```

### Advanced Usage

```cmd
copy /Y malicious.exe C:\program.exe
```

## Expected Output

'1 file(s) copied.' if successful; error if permissions denied or file not found.

## Related

- [[Related Procedure: Place-Malicious-EXE-in-Root-Directory]]
