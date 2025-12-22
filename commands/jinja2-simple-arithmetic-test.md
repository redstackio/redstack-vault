---
data: '{{3*3}}'
tags:
  - ssti-test
type: command
output: '9'
executor: python
platforms:
  - Python
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.008Z'
id: 383511c6-7249-4df2-b637-6ca5a4cbd51f
verified: false
validated: true
submitted: true
---
# jinja2-simple-arithmetic-test

## Command

```python
{{3*3}}
```

## Description

Basic Jinja2 template expression to test SSTI by performing arithmetic; evaluates to 9 if templating is active.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Simple expression | Yes |

## Examples

### Basic Usage

```python
{{3*3}}
```

### Advanced Usage

N/A for this test.

## Expected Output

'9' rendered in template context.

## Related

- [[Related Procedure]]
