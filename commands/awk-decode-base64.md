---
data: >-
  curl -s https://app.bountypay.h1ctf.com/bp_web_trace.log | awk -F ':' '{print
  $2}' | while read line; do echo "$line" | base64 --decode && echo "\n"; done
tags:
  - decoding
type: command
output: >-
  Decoded JSON payloads revealing credentials like
  {"username":"brian.oliver","password":"V7h0inzX"}
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:05.996Z'
id: e439cd64-d834-4652-99ef-d72883e13399
verified: false
validated: true
submitted: true
---
# awk-decode-base64

## Command

```bash
curl -s https://app.bountypay.h1ctf.com/bp_web_trace.log | awk -F ':' '{print $2}' | while read line; do echo "$line" | base64 --decode && echo "\n"; done
```

## Description

Parses and decodes base64-encoded log entries.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-F ':'` | Field separator | Yes |
| `-s` | Silent curl | No |

## Examples

### Basic Usage

```bash
cat log | awk ... | base64 --decode
```

## Expected Output

Decoded payloads.

## Related

- Standard awk and base64
