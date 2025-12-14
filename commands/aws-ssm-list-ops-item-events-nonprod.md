---
id: cmd-uuid-006
data: 'aws ssm list-ops-item-events --endpoint-url https://████'
tags:
  - aws
  - ssm
  - events
type: command
output: >-
  Varies: {"Summaries": []} for permitted, AccessDeniedException for denied; no
  CloudTrail log
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.853Z'
verified: false
validated: true
submitted: true
---
# aws-ssm-list-ops-item-events-nonprod

## Command

```bash
aws ssm list-ops-item-events --endpoint-url https://████
```

## Description

Lists SSM OpsItem events on non-production endpoint to enumerate ssm:ListOpsItemEvents permission without logging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --endpoint-url | Non-production URL (https://████) | Yes |

## Examples

### Basic Usage

```bash
aws ssm list-ops-item-events --endpoint-url https://████
```

### Advanced Usage

```bash
aws ssm list-ops-item-events --endpoint-url https://████ --ops-item-id opsitem:123
```

## Expected Output

{"Summaries": []} or AccessDenied; no log.

## Related

- [[procedures/Test-Additional-SSM-Actions-for-Silent-Enumeration]]
