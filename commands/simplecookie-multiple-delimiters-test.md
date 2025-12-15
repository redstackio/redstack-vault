---
id: cmd-simplecookie-multiple
data: |-
  from http import cookies
  C = cookies.SimpleCookie()
  C.load('__utmz=blah csrftoken=x')
  C.load('__utmz=blah\x09csrftoken=x')
  C.load('__utmz=blah\x0bcsrftoken=x')
  C.load('__utmz=blah\x0ccsrftoken=x')
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
updated_at: '2025-12-14T17:27:57.493Z'
verified: false
validated: true
submitted: true
---
# simplecookie-multiple-delimiters-test

## Command

```python
from http import cookies
C = cookies.SimpleCookie()
C.load('__utmz=blah csrftoken=x')
C.load('__utmz=blah\x09csrftoken=x')
C.load('__utmz=blah\x0bcsrftoken=x')
C.load('__utmz=blah\x0ccsrftoken=x')
print(C)
```

## Description

Tests multiple whitespace and control delimiters in SimpleCookie to confirm vulnerability persistence for Firefox exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| multiple loads | Strings with space, \x09, \x0b, \x0c | Yes |

## Examples

### Basic Usage

```python
from http import cookies
C = cookies.SimpleCookie()
C.load('__utmz=blah csrftoken=x')
C.load('__utmz=blah\x09csrftoken=x')
C.load('__utmz=blah\x0bcsrftoken=x')
C.load('__utmz=blah\x0ccsrftoken=x')
print(C)
```

## Expected Output

<SimpleCookie: __utmz='blah'; csrftoken='x'>

## Related

- [[commands/simplecookie-load-tab-delimiter]]
- [[procedures/Firefox-Whitespace-Bypass-for-Cookie-Injection]]
