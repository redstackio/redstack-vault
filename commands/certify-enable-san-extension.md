---
type: command
executor: powershell
data: Certify.exe setconfig /enablesan /restart
output: null
platforms:
  - Windows
tags:
  - adcs
  - configuration
verified: true
validated: true
---

# certify-enable-san-extension

## Command

```powershell
Certify.exe setconfig /enablesan /restart
```

## Description

Enables the Subject Alternative Name (SAN) extension for all certificate templates under the target CA and restarts the certificate service to apply changes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /enablesan | Enables SAN extension in templates | Yes |
| /restart | Restarts certsvc service | Yes |

## Examples

### Basic Usage

```powershell
Certify.exe setconfig /enablesan /restart
```

## Expected Output

Success message: "Configuration updated successfully. Service restarted."

## Related

- [[procedures/Vulnerable-Certificate-Authority-Access-Control]]
