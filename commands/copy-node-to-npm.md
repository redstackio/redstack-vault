---
id: cmd-copy-node-npm
data: 'copy C:\tools\node.exe C:\tools\npm.exe'
tags:
  - file-copy
  - hijacking
type: command
output: 1 file(s) copied.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.951Z'
verified: false
validated: true
submitted: true
---
# copy-node-to-npm

## Command

```cmd
copy C:\tools\node.exe C:\tools\npm.exe
```

## Description

Copies node.exe to npm.exe in the Node.js installation directory as a demonstration of placing a malicious executable to hijack the npm command via PATH precedence on Windows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `C:\tools\node.exe` | Source file path | Yes |
| `C:\tools\npm.exe` | Destination file path | Yes |

## Examples

### Basic Usage

```cmd
copy C:\tools\node.exe C:\tools\npm.exe
```

### Advanced Usage

```cmd
copy /Y malicious.exe C:\tools\npm.exe
```

## Expected Output

'1 file(s) copied' if successful; error if source missing or no write access.

## Related

- [[procedures/Hijack-NPM-Command-via-PATH-Precedence]]
