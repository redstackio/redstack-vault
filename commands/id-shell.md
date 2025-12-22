---
data: id
tags:
  - recon
type: command
output: uid=1000(airflow) gid=1000(airflow) groups=1000(airflow)
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.971Z'
id: ec314cf8-7dfc-447d-a28b-efcd8ce98b8b
verified: false
validated: true
submitted: true
---
# id-shell

## Command

```bash
id
```

## Description

Displays current user and group IDs, useful for RCE PoC to confirm execution context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```bash
id
```

## Expected Output

uid=1000(airflow) gid=1000(airflow) groups=1000(airflow)

## Related

- [[commands/env-shell]]
