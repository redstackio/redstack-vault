---
data: >-
  payload["Authorization"] = "token " +
  "9db9ca3440e535d90408a32a9c03d415979da910"
tags:
  - python
  - variable
  - auth
type: command
executor: python
platforms:
  - Web
  - GitHub Enterprise
id: 9ee128cf-5db3-4a52-934e-e73e517b338f
created_at: '2025-12-11T06:10:25.180Z'
updated_at: '2025-12-11T06:10:25.180Z'
verified: false
validated: true
submitted: true
---
# python-add-authorization-header

## Command

```python
payload["Authorization"] = "token " + "9db9ca3440e535d90408a32a9c03d415979da910"
```

## Description

Adds the Authorization header with a token to the payload dictionary in Python.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Authorization | Bearer token for authentication | Yes |

## Examples

### Basic Usage

```python
payload["Authorization"] = "token 9db9ca3440e535d90408a32a9c03d415979da910"
```

## Expected Output

No output; header is added to dictionary.

## Related

- [[commands/python-print-payload]]
- [[procedures/Extract-and-Validate-Leaked-GitHub-Token]]
