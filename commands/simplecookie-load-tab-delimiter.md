---
id: cmd-simplecookie-tab
data: |-
  from http import cookies
  C = cookies.SimpleCookie()
  C.load('__utmz=blah\x09csrftoken=x')
  print(C)
tags:
  - cookie-parsing
  - firefox
  - python
type: command
output: '<SimpleCookie: __utmz=''blah''; csrftoken=''x''>'
executor: python
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.501Z'
verified: false
validated: true
submitted: true
---
# simplecookie-load-tab-delimiter

## Command

```python
from http import cookies
C = cookies.SimpleCookie()
C.load('__utmz=blah\x09csrftoken=x')
print(C)
```

## Description

Tests tab (\x09) as delimiter in SimpleCookie for Firefox-compatible whitespace injection in __utmz cookie.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| load string | String with \x09 separator | Yes |

## Examples

### Basic Usage

```python
from http import cookies
C = cookies.SimpleCookie()
C.load('__utmz=blah\x09csrftoken=x')
print(C)
```

## Expected Output

<SimpleCookie: __utmz='blah'; csrftoken='x'>

## Related

- [[commands/simplecookie-load-delimiter-injection]]
- [[procedures/Firefox-Whitespace-Bypass-for-Cookie-Injection]]
