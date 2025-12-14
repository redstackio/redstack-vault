---
id: cmd-jobs-check-001
data: jobs
tags:
  - monitoring
  - bash
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.925Z'
verified: false
validated: true
submitted: true
---
# jobs-check-pending

## Command

```bash
jobs
```

## Description

Lists active background jobs (e.g., pending curl processes) to verify if DoS requests are still running after initiation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Built-in bash command | No |

## Examples

### Basic Usage

```bash
jobs
```

### Advanced Usage

jobs -l for PID details

## Expected Output

[1] Running time curl -s https://... & (list of jobs)

## Related

- [[commands/curl-slow-dos-launch]]
- [[procedures/Verify-and-Monitor-DoS-Impact]]
