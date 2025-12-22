---
id: cmd-mkdir-tools
data: 'mkdir C:\tools'
tags:
  - directory-creation
type: command
output: 'Directory C:\tools created successfully.'
executor: powershell
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.955Z'
verified: false
validated: true
submitted: true
---
# mkdir-tools-directory

## Command

```powershell
mkdir C:\tools
```

## Description

Creates the custom installation directory C:\tools on Windows, which will inherit permissive permissions from the drive root, setting up for Node.js installation exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `C:\tools` | Target path for the directory | Yes |

## Examples

### Basic Usage

```powershell
mkdir C:\tools
```

### Advanced Usage

```powershell
mkdir C:\tools -Force
```

## Expected Output

If successful: No output or 'Directory created'. If exists: Warning that it already exists.

## Related

- [[procedures/Install-Node.js-to-Custom-Writable-Directory]]
