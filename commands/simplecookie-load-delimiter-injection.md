---
id: cmd-simplecookie-delimiter
data: |-
  from http import cookies
  C = cookies.SimpleCookie()
  C.load('__utmz=blah]csrftoken=x')
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
updated_at: '2025-12-14T17:27:57.504Z'
verified: false
validated: true
submitted: true
---
# simplecookie-load-delimiter-injection

## Command

```python
from http import cookies
C = cookies.SimpleCookie()
C.load('__utmz=blah]csrftoken=x')
print(C)
```

## Description

Demonstrates Python's SimpleCookie parsing flaw by loading a malformed string with ']' as delimiter, splitting into two cookies for CSRF injection testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| load string | Malformed cookie like '__utmz=blah]csrftoken=x' | Yes |
| delimiter | Character like ']' to separate pairs | Yes |

## Examples

### Basic Usage

```python
from http import cookies
C = cookies.SimpleCookie()
C.load('__utmz=blah]csrftoken=x')
print(C)
```

### Advanced Usage

Test multiple: Chain with other loads.

## Expected Output

<SimpleCookie: __utmz='blah'; csrftoken='x'>

## Related

- [[commands/simplecookie-load-tab-delimiter]]
- [[procedures/Exploit-Cookie-Parsing-Flaw-with-Forged-Token]]
