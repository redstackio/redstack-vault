---
id: c5h6i7j8-k9l0-1235-gh23-456789012345
data: python manage.py poc
tags:
  - django
  - poc
  - sqli
type: command
output: >-
  Sample users created; simulates payload; generates injected SQL; returns all
  users including admin; prints 'SUCCESS: The filter was bypassed'
executor: bash
platforms:
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.946Z'
verified: false
validated: true
submitted: true
---
# python-manage-py-poc

## Command

```bash
python manage.py poc
```

## Description

Executes the custom POC management command to demonstrate the SQL injection vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs default POC | No |

## Examples

### Basic Usage

```bash
python manage.py poc
```

### Advanced Usage

Not applicable; custom command.

## Expected Output

Users created, injected SQL printed (e.g., SELECT ... WHERE (NOT ... ) OR 1=1 OR (...)), all users listed, success message.

## Related

- [[commands/python-manage-py-migrate]]
- [[procedures/Run-Migrations-and-Execute-POC]]
