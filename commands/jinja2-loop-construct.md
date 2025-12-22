---
id: cf9b7424-c851-4b65-b7c4-48a6164d66ba
name: jinja2-loop-construct
type: command
executor: bash
data: '{%for c in [1,2,3] %}{{c,c,c}}{% endfor %}'
output: null
created_at: '2025-12-11T03:47:39.245Z'
updated_at: '2025-12-11T03:47:39.245Z'
platforms:
  - Web
tags:
  - ssti
  - jinja2
verified: false
validated: true
submitted: true
---

# jinja2-loop-construct

## Command

```bash
{%for c in [1,2,3] %}{{c,c,c}}{% endfor %}
```

## Description

Executes a loop over a list, printing each element three times to demonstrate control flow in Jinja2 templates.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| for c in [1,2,3] | Loop construct | Yes |
| {{c,c,c}} | Outputs the value of c three times | Yes |

## Examples

### Basic Usage

```bash
{%for c in [1,2,3] %}{{c,c,c}}{% endfor %}
```

## Expected Output

Something like '1,1,1 2,2,2 3,3,3'

## Related

- [[procedures/Explore-Advanced-SSTI-Payloads-for-Exploitation]]
