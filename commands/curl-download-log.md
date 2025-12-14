---
data: 'curl https://app.bountypay.h1ctf.com/bp_web_trace.log -o bp_web_trace.log'
tags:
  - download
type: command
output: Raw log content with base64-encoded entries
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.000Z'
id: c1464324-4ce7-4c74-a9b2-d4328fc43eaf
verified: false
validated: true
submitted: true
---
# curl-download-log

## Command

```bash
curl https://app.bountypay.h1ctf.com/bp_web_trace.log -o bp_web_trace.log
```

## Description

Downloads a remote log file for offline analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-o` | Output file | No |

## Examples

### Basic Usage

```bash
curl url -o file.log
```

## Expected Output

Saved log file.

## Related

- Standard curl usage
