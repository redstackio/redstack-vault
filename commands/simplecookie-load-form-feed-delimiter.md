---
id: cmd-simplecookie-form-feed
data: |-
  from http import cookies
  C = cookies.SimpleCookie()
  C.load('__utmz=blah\x0ccsrftoken=x')
  print(C)
tags:
  - cookie-parsing
  - python
type: command
output: '<SimpleCookie: __utmz=''blah''; csrftoken=''x''>'
executor: python
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.496Z'
verified: false
validated: true
submitted: true
---
# simplecookie-load-form-feed-delimiter

## Command

```python
from http import cookies
C = cookies.SimpleCookie()
C.load('__utmz=blah\x0ccsrftoken=x')
print(C)
```

## Description

Uses form feed (\x0c) as delimiter to split cookie for injection simulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| load string | With \x0c | Yes |

## Examples

### Basic Usage

```python
from http import cookies
C = cookies.SimpleCookie()
C.load('__utmz=blah\x0ccsrftoken=x')
print(C)
```

## Expected Output

<SimpleCookie: __utmz='blah'; csrftoken='x'>

## Related

- [[commands/simplecookie-load-vertical-tab-delimiter]]
