---
data: hostname -f
tags:
  - verification
type: command
executor: bash
platforms:
  - Linux
id: eb5a7884-9aca-41bb-b770-e3787e91766b
created_at: '2025-12-11T03:48:05.986Z'
updated_at: '2025-12-11T03:48:05.986Z'
verified: false
validated: true
submitted: true
---
# hostname-f

## Command

```bash
hostname -f
```

## Description

Displays the full hostname.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Full hostname | Yes |

## Examples

### Basic Usage

```bash
hostname -f
```

## Expected Output

gitlab-sidekiq-imports-v2-5b46b76b94-9zkwr

## Related

- [[procedures/Bypass-Feature-Flag-and-Verify-RCE]]
