---
id: cmd-curl-who-cron-restricted-001
data: 'time curl -i https://hack.whocoronavirus.org/internal/cron/refreshCaseStats'
tags:
  - testing
  - http
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.946Z'
verified: false
validated: true
submitted: true
---
# curl-verify-cron-access-restricted

## Command

```bash
time curl -i https://hack.whocoronavirus.org/internal/cron/refreshCaseStats
```

## Description

This command verifies that access to the internal cron endpoint has been restricted post-remediation, including response headers and timing to confirm quick denial.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include HTTP response headers in output | Yes |
| `https://hack.whocoronavirus.org/internal/cron/refreshCaseStats` | Target endpoint URL | Yes |
| `time` | Prefix to measure real execution time | Yes |

## Examples

### Basic Usage

```bash
time curl -i https://hack.whocoronavirus.org/internal/cron/refreshCaseStats
```

### Advanced Usage

With follow redirects: ```bash
time curl -i -L https://hack.whocoronavirus.org/internal/cron/refreshCaseStats
```

## Expected Output

HTTP/2 401 Unauthorized header with body message 'Cron access only', completing in under 1 second.

## Related

- [[commands/curl-test-internal-cron-access-verbose]]
