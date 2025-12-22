---
id: cmd-check-dangling
data: curl -I $URL
tags:
  - web
  - probe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.570Z'
verified: false
validated: true
submitted: true
---
# check-dangling-service

## Command

```bash
curl -I $URL
```

## Description

Probes a URL from a dangling DNS record to check if the service is active or decommissioned.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Head request only | Yes |
| `$URL` | Target URL (e.g., https://dangling.herokuapp.com) | Yes |

## Examples

### Basic Usage

```bash
curl -I https://dangling.herokuapp.com
```

### Advanced Usage

```bash
curl -I -m 10 https://dangling.herokuapp.com
```

## Expected Output

HTTP headers, e.g., 404 Not Found indicating dangling status.

## Related

- [[Related Procedure: Discover Dangling DNS Records]]
