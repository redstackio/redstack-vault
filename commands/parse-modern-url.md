---
data: const modernUrl = new URL(poc_url); console.log(modernUrl.hostname);
tags:
  - modern-parsing
  - crlf-injection
type: command
output: test1.com\r\ntest2.com
executor: node
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.485Z'
id: f61a5328-9d4f-408d-ad95-ca5bb8b8b361
verified: false
validated: true
submitted: true
---
# parse-modern-url

## Command

```javascript
const modernUrl = new URL(poc_url);
console.log(modernUrl.hostname);
```

## Description

Uses the modern WHATWG URL constructor in Node.js to parse a URL string, handling CRLF without termination and including it in the hostname. Use for comparison to highlight legacy vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `URL` | Built-in constructor | Yes |
| `poc_url` | Input URL string | Yes |
| `modernUrl.hostname` | Full hostname property | Yes |

## Examples

### Basic Usage

```javascript
const poc_url = 'http://test1.com\\r\\ntest2.com';
const modernUrl = new URL(poc_url);
console.log(modernUrl.hostname); // test1.com\r\ntest2.com
```

### Advanced Usage

```javascript
const modernUrl = new URL(poc_url, 'http://base.com'); // With base URL
console.log(modernUrl.hostname);
```

## Expected Output

Outputs the full hostname 'test1.com\r\ntest2.com', showing no CRLF termination.

## Related

- [[Related Procedure: Compare-with-Modern-URL-Constructor-Parsing]]
