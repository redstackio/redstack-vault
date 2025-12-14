---
id: cmd-mkdir-path
data: 'mkdir "C:\\Program Files\\Java\\jre1.8.0_xxx\\bin\\server\\amd64"'
tags:
  - directory-creation
type: command
output: null
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.106Z'
verified: false
validated: true
submitted: true
---
# mkdir-create-path

## Command

```cmd
mkdir "C:\Program Files\Java\jre1.8.0_xxx\bin\server\amd64"
```

## Description

Creates a nested directory structure on Windows C: drive to mimic a non-existent DLL load path for hijacking purposes, such as in Burp Suite exploitation. Handles spaces in paths with quotes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Path | Full quoted path to create | Yes |

## Examples

### Basic Usage

```cmd
mkdir "C:\Program Files\Test"
```

### Advanced Usage

```cmd
mkdir "C:\Program Files\Java\jre1.8.0_xxx\bin\server\amd64"
```

## Expected Output

A new directory or tree is created; output like "The directory ... was created successfully" if new, or nothing if exists.

## Related

- [[Related Procedure: Create-Malicious-Directory-Structure]]
