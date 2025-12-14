---
data: >-
  curl -s -w "%{time_total}s" "https://betterscience.org/plugin/tag/peerj" >
  /dev/null
tags:
  - recon
  - baseline
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.898Z'
id: a998f930-031c-486e-9e96-b2b49cac4b88
verified: false
validated: true
submitted: true
---
# curl-baseline-tag-request

## Command

```bash
curl -s -w "%{time_total}s" "https://betterscience.org/plugin/tag/peerj" > /dev/null
```

## Description

Sends a GET request to the tag endpoint with a legitimate tag to measure baseline response time for SQLi detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, no progress meter | Yes |
| `-w "%{time_total}s"` | Print total time in seconds | Yes |
| URL | Target endpoint with valid tag | Yes |
| `> /dev/null` | Suppress output body | Yes |

## Examples

### Basic Usage

```bash
curl -s -w "%{time_total}s" "https://betterscience.org/plugin/tag/peerj" > /dev/null
```

### Advanced Usage

Add headers for realism:

```bash
curl -s -w "%{time_total}s" -H "User-Agent: Mozilla/5.0..." "https://betterscience.org/plugin/tag/peerj" > /dev/null
```

## Expected Output

A single number representing response time, e.g., 0.28s.

## Related

- [[commands/curl-sqli-payload-sleep-3]]
- [[procedures/Establish-Baseline-Response-Time-for-Tag-Endpoint]]
