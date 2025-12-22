---
data: print(payload)
tags:
  - python
  - output
type: command
executor: python
platforms:
  - Web
  - GitHub Enterprise
id: a03c5fe1-3d28-4192-96e3-d77a46dfd15c
created_at: '2025-12-11T06:10:25.170Z'
updated_at: '2025-12-11T06:10:25.170Z'
verified: false
validated: true
submitted: true
---
# python-print-payload

## Command

```python
print(payload)
```

## Description

Prints the contents of the payload dictionary to the console in Python.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters | N/A |

## Examples

### Basic Usage

```python
print(payload)
```

## Expected Output

The contents of the payload dictionary, e.g., {'Authorization': 'token 9db9ca3440e535d90408a32a9c03d415979da910'}.

## Related

- [[commands/python-add-authorization-header]]
- [[procedures/Extract-and-Validate-Leaked-GitHub-Token]]
