---
id: cmd-inspect-form-field-2024
data: |-
  import inspect
  from django.forms import GenericIPAddressField
  field = GenericIPAddressField()
  print(inspect.getsource(field.clean))
tags:
  - recon
  - source-analysis
type: command
output: null
executor: python
platforms:
  - Python
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.836Z'
verified: false
validated: true
submitted: true
---
# inspect-form-field

## Command

```python
import inspect
from django.forms import GenericIPAddressField
field = GenericIPAddressField()
print(inspect.getsource(field.clean))
```

## Description

Inspects the clean method of Django's GenericIPAddressField to confirm it invokes vulnerable IPv6 functions without length validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Direct execution | N/A |

## Examples

### Basic Usage

```python
from django.forms import GenericIPAddressField
print(GenericIPAddressField.__doc__)
```

## Expected Output

Source code revealing calls to clean_ipv6_address, e.g., if protocol == 'IPv6': return clean_ipv6_address(value).

## Related

- [[Related Procedure: Identify Vulnerable IPv6 Validation in Django]]
