---
data: >-
  curl "https://www.xvcams.com/?tpl=index2&model=json&_=$(date +%s)" -H
  "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
tags:
  - recon
  - json
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.740Z'
id: a65f796d-b1b6-48e9-a29e-3c53f12d48f2
verified: false
validated: true
submitted: true
---
---

# curl-access-model-json-endpoint

## Command

```bash
curl "https://www.xvcams.com/?tpl=index2&model=json&_=$(date +%s)" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

## Description

Fetches JSON model data from root endpoint. Use to supplement PII collection; timestamp avoids caching.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `tpl=index2` | Template selector | Yes |
| `model=json` | JSON output mode | Yes |
| `_=$(date +%s)` | Cache-buster timestamp | Yes |
| `-H "User-Agent: ..."` | Header for realism | No |

## Examples

### Basic Usage

```bash
curl "https://www.xvcams.com/?tpl=index2&model=json&_=1496352433890"
```

### Advanced Usage

```bash
curl "https://www.xvcams.com/?tpl=index2&model=json&_= $(date +%s)" | jq 'keys'
```

## Expected Output

JSON object with model info, e.g., {"models": [{...}]}. Parse for IDs.

## Related

- [[Related Procedure]]
