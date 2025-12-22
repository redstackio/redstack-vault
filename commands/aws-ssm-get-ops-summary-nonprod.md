---
id: cmd-uuid-004
data: aws ssm get-ops-summary --endpoint-url ███
tags:
  - aws
  - ssm
  - enumeration
type: command
output: >-
  Varies by privileges: empty Entities array for permitted,
  AccessDeniedException for denied; no CloudTrail log
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.856Z'
verified: false
validated: true
submitted: true
---
# aws-ssm-get-ops-summary-nonprod

## Command

```bash
aws ssm get-ops-summary --endpoint-url ███
```

## Description

Retrieves SSM OpsSummary on non-production endpoint (███) to test ssm:GetOpsSummary permission silently.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --endpoint-url | Non-production URL (███) | Yes |

## Examples

### Basic Usage

```bash
aws ssm get-ops-summary --endpoint-url ███
```

### Advanced Usage

```bash
aws ssm get-ops-summary --endpoint-url https://███ --filters Key=ResourceId,Values=opsitem:123
```

## Expected Output

{"Entities": []} for allowed; AccessDeniedException for denied; no log.

## Related

- [[commands/export-aws-profile-noperm]]
- [[procedures/Test-Additional-SSM-Actions-for-Silent-Enumeration]]
