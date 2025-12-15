---
data: 'const poc_url = ''http://test1.com\\r\\ntest2.com'';'
tags:
  - url-crafting
  - crlf-injection
type: command
output: 'POC URL string defined: ''http://test1.com\r\ntest2.com'''
executor: node
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.493Z'
id: b4161189-350f-4e77-adcc-31a17005269f
verified: false
validated: true
submitted: true
---
# define-poc-url

## Command

```javascript
const poc_url = 'http://test1.com\\r\\ntest2.com';
```

## Description

Defines a JavaScript string variable for a POC URL with CRLF injection, using double backslashes to escape newlines in the string literal. Use this in Node.js scripts to prepare malicious input for URL parsing tests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `poc_url` | Variable name for the URL string | Yes |
| `\\r\\n` | Escaped CRLF sequence | Yes |

## Examples

### Basic Usage

```javascript
const poc_url = 'http://test1.com\\r\\ntest2.com';
console.log(poc_url);
```

### Advanced Usage

```javascript
const poc_url = `http://whitelisted.com\\r\\nmalicious.com/path`;
// Use template literals for complex URLs
```

## Expected Output

The variable poc_url is set to the string 'http://test1.com\r\ntest2.com', printable via console.log without syntax errors.

## Related

- [[Related Procedure: Craft-CRLF-Injection-URL-for-Node.js]]
