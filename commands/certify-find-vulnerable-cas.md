---
type: command
executor: powershell
data: Certify.exe find /vulnerable
output: null
platforms:
  - Windows
tags:
  - adcs
  - enumeration
verified: true
validated: true
---

# certify-find-vulnerable-cas

## Command

```powershell
Certify.exe find /vulnerable
```

## Description

Scans Active Directory for vulnerable Certificate Authorities where low-privileged users have ManageCA or Manage Certificates permissions, identifying ESC7 exploitation opportunities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /vulnerable | Flag to filter for vulnerable CAs only | Yes |

## Examples

### Basic Usage

```powershell
Certify.exe find /vulnerable
```

## Expected Output

JSON output listing vulnerable CAs, e.g.:

{
  "CAs": [
    {
      "Name": "SERVER\\ca-name",
      "Permissions": ["ManageCA"],
      "Vulnerable": true
    }
  ]
}

## Related

- [[procedures/Vulnerable-Certificate-Authority-Access-Control]]
