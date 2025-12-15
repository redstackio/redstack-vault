---
id: cmd-uuid-002
data: 'curl -w "Total time: %{time_total}s\n" -o /dev/null -s http://owncloud.com/'
tags:
  - testing
type: command
output: 'Total time: 0.001s'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.978Z'
verified: false
validated: true
submitted: true
---
# curl-normal-get

## Command

```bash
curl -w "Total time: %{time_total}s\n" -o /dev/null -s http://owncloud.com/
```

## Description

Performs a timed normal GET request to baseline server response time.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -w | Write timing info | Yes |
| -o /dev/null | Discard body | Yes |
| -s | Silent mode | Yes |
| http://owncloud.com/ | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -w "%{time_total}" -s -o /dev/null http://example.com/
```

### Advanced Usage

```bash
curl -w "Time: %{time_total}s" -H "User-Agent: Test" http://example.com/
```

## Expected Output

"Total time: 0.001s" indicating normal latency.

## Related

- [[Related Procedure]]
