---
type: command
executor: powershell
data: 'Certify.exe writefile /ca:$_CA_NAME /readonly'
output: null
platforms:
  - Windows
tags:
  - adcs
  - enumeration
verified: true
validated: true
---

# certify-get-cdp-list

## Command

```powershell
Certify.exe writefile /ca:$_CA_NAME /readonly
```

## Description

Retrieves the current Certificate Distribution Point (CDP) list to identify writable locations for shell deployment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /ca:$_CA_NAME | Target CA (e.g., SERVER\\ca-name) | Yes |
| /readonly | Read-only mode to list CDPs | Yes |

## Examples

### Basic Usage

```powershell
Certify.exe writefile /ca:SERVER\ca-name /readonly
```

## Expected Output

List of CDPs: "CDP1: http://server/certsrv/certnew.p7b, Writable: Yes, Path: \\server\share"

## Related

- [[procedures/Vulnerable-Certificate-Authority-Access-Control]]
