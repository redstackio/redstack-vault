---
id: 729a7c6c-b5e5-4c81-859f-313f0a917144
name: browser-enter-https-url
type: command
executor: browser
data: 'https://$_TARGET_URL'
output: null
created_at: '2023-04-06T03:56:17.451945+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Windows
  - Browser
tags:
  - protocol-handler
  - browser-escape
verified: true
validated: true
---

# browser-enter-https-url

## Command

In the browser address bar, enter:

```text
https://$_TARGET_URL
```

## Description

This command uses the HTTPS protocol to securely access resources, potentially evading unencrypted traffic filters in restricted browsers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The secure target website or IP (e.g., example.com) | Yes |

## Examples

### Basic Usage

```text
https://example.com
```

### Advanced Usage

```text
https://example.com/api
```

## Expected Output

Secure page loads with HTTPS indicator. Success: Content displays without certificate errors; failure: Connection refused or block.

## Related

- [[procedures/Browser-Escape-via-Unassociated-Protocols]]
