---
id: cmd-curl-who-cron-verbose-001
data: 'time curl -v https://hack.whocoronavirus.org/internal/cron/refreshCaseStats'
tags:
  - testing
  - http
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.949Z'
verified: false
validated: true
submitted: true
---
# curl-test-internal-cron-access-verbose

## Command

```bash
time curl -v https://hack.whocoronavirus.org/internal/cron/refreshCaseStats
```

## Description

This command tests public access to the internal cron endpoint in the WHO COVID-19 App, measuring execution time and displaying verbose HTTP details to confirm unauthorized access and resource intensity.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output including request/response headers | Yes |
| `https://hack.whocoronavirus.org/internal/cron/refreshCaseStats` | Target endpoint URL | Yes |
| `time` | Prefix to measure real execution time | Yes |

## Examples

### Basic Usage

```bash
time curl -v https://hack.whocoronavirus.org/internal/cron/refreshCaseStats
```

### Advanced Usage

To silent output except timing: ```bash
time curl -s -v -o /dev/null https://hack.whocoronavirus.org/internal/cron/refreshCaseStats 2>&1
```

## Expected Output

Verbose headers followed by a 200 OK response body (empty or stats confirmation), with total execution time of approximately 20 seconds, indicating backend processing load.

## Related

- [[commands/curl-verify-cron-access-restricted]]
