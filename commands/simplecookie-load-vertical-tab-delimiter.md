---
id: cmd-simplecookie-vertical-tab
data: |-
  from http import cookies
  C = cookies.SimpleCookie()
  C.load('__utmz=blah\x0bcsrftoken=x')
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
updated_at: '2025-12-14T17:27:57.498Z'
verified: false
validated: true
submitted: true
---
# simplecookie-load-vertical-tab-delimiter

## Command

```python
from http import cookies
C = cookies.SimpleCookie()
C.load('__utmz=blah\x0bcsrftoken=x')
print(C)
```

## Description

Parses cookie using vertical tab (\x0b) as delimiter for control character bypass testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| load string | With \x0b | Yes |

## Examples

### Basic Usage

```python
from http import cookies
C = cookies.SimpleCookie()
C.load('__utmz=blah\x0bcsrftoken=x')
print(C)
```

## Expected Output

<SimpleCookie: __utmz='blah'; csrftoken='x'>

## Related

- [[commands/simplecookie-load-tab-delimiter]]
