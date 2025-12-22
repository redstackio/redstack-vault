---
data: pull_number = 76793
tags:
  - python
  - variable
type: command
executor: python
platforms:
  - Web
  - GitHub Enterprise
id: a28f4282-add5-47b8-84a9-d99ff2305249
created_at: '2025-12-11T06:10:25.256Z'
updated_at: '2025-12-11T06:10:25.256Z'
verified: false
validated: true
submitted: true
---
# python-set-pull-number

## Command

```python
pull_number = 76793
```

## Description

Sets a variable for the pull request number in Python, used to construct API URLs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pull_number | Integer value representing the pull request ID | Yes |

## Examples

### Basic Usage

```python
pull_number = 76793
```

## Expected Output

No output; variable is set.

## Related

- [[commands/python-construct-pull-url]]
- [[procedures/Extract-and-Validate-Leaked-GitHub-Token]]
