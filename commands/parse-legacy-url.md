---
data: >-
  const url = require('url'); const parsed = url.parse(poc_url);
  console.log(parsed.hostname);
tags:
  - legacy-parsing
  - crlf-injection
type: command
output: test1.com
executor: node
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.492Z'
id: 12301509-ced3-499b-94db-6b508c169d36
verified: false
validated: true
submitted: true
---
# parse-legacy-url

## Command

```javascript
const url = require('url');
const parsed = url.parse(poc_url);
console.log(parsed.hostname);
```

## Description

Requires Node.js url module and parses a given URL string using the legacy parse function, extracting the hostname which terminates at CRLF. Ideal for testing whitelist bypass in vulnerable applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Built-in module | Yes |
| `poc_url` | Input URL string | Yes |
| `parsed.hostname` | Extracted hostname property | Yes |

## Examples

### Basic Usage

```javascript
const url = require('url');
const poc_url = 'http://test1.com\\r\\ntest2.com';
const parsed = url.parse(poc_url);
console.log(parsed.hostname); // test1.com
```

### Advanced Usage

```javascript
const url = require('url');
const parsed = url.parse(poc_url, true, true); // Strict parsing
console.log(parsed.hostname);
```

## Expected Output

Outputs 'test1.com' for the POC, demonstrating early termination due to CRLF.

## Related

- [[Related Procedure: Parse-URL-with-Legacy-url.parse-to-Extract-Hostname]]
