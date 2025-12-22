---
id: c8620d3c-17b0-419a-905a-0140fb77d187
name: sharpaztoken-generate-device-keys
type: command
executor: bash
data: >-
  SharpAzToken.exe devicekeys --pfxpath $_PFX_PATH --refreshtoken (--prtcookie
  $_PRT_COOKIE or --username $_USERNAME --password $_PASSWORD)
output: null
created_at: '2023-05-24T07:40:26.709313+00:00'
updated_at: '2023-05-24T07:40:26.785466+00:00'
platforms:
  - Cloud
tags:
  - azure
  - prt
  - token-generation
verified: true
validated: true
---

# SharpAzToken Generate Device Keys

## Command

```bash
SharpAzToken.exe devicekeys --pfxpath $_PFX_PATH --refreshtoken (--prtcookie $_PRT_COOKIE or --username $_USERNAME --password $_PASSWORD)
```

## Description

This command generates a Primary Refresh Token (PRT) and session key from a device certificate PFX file, using either a PRT cookie or username/password for refresh. It is essential for obtaining persistent credentials in Azure AD after device enrollment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --pfxpath | Path to the input PFX device certificate file | Yes |
| --refreshtoken | Flag to generate refresh token | Yes |
| --prtcookie | PRT cookie extracted from a Windows session (alternative to username/password) | Conditional |
| --username | Azure username for credential-based refresh | Conditional |
| --password | Azure password for credential-based refresh | Conditional |

## Examples

### Basic Usage with PRT Cookie

```bash
SharpAzToken.exe devicekeys --pfxpath ./device.pfx --refreshtoken --prtcookie "cookie_value_here"
```

### Advanced Usage with Credentials

```bash
SharpAzToken.exe devicekeys --pfxpath $_PFX_PATH --refreshtoken --username $_USERNAME --password $_PASSWORD
```

## Expected Output

Successful execution outputs the PRT and session key, e.g.:

"PRT: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9...\nSession Key: [base64_key]"

These can be used in subsequent Azure API calls; validate by decoding the PRT JWT.

## Related

- [[procedures/Azure Device Management and Token Generation with SharpAzToken]]
- [[commands/sharpaztoken-join-mdm-device]]
