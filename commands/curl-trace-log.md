---
data: 'curl -sk https://app.bountypay.h1ctf.com/bp_web_trace.log'
tags:
  - http-request
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:58.208Z'
id: 1b12fd5b-9a73-4153-b5de-aa886d4de54b
verified: false
validated: true
submitted: true
---
# curl-trace-log

## Command

```bash
curl -sk https://app.bountypay.h1ctf.com/bp_web_trace.log
```

## Description

Downloads the trace log file containing base64-encoded credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s | Silent mode | No |
| -k | Insecure SSL | No |

## Examples

### Basic Usage

```bash
curl -sk https://example.com/log.txt
```

## Expected Output

Base64 JSON logs with credentials.

## Related

- [[tools/Curl]]
- [[procedures/Credential-Leak-Analysis-and-Initial-Login]]
