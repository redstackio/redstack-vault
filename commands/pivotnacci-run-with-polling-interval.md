---
id: 07e82521-66cd-4788-a34b-635f61d30d57
name: pivotnacci-run-with-polling-interval
type: command
executor: bash
data: pivotnacci $_AGENT_URL --polling-interval $_INTERVAL_MS
output: null
created_at: '2023-04-06T03:56:22.599866+00:00'
updated_at: '2023-04-10T20:25:18.048816+00:00'
platforms:
  - Linux
tags:
  - pivoting
  - socks-proxy
verified: true
validated: true
---

# pivotnacci-run-with-polling-interval

## Command

```bash
pivotnacci $_AGENT_URL --polling-interval $_INTERVAL_MS
```

## Description

This command launches Pivotnacci with a custom polling interval for the HTTP agent, allowing adjustment of how frequently the proxy checks for new connections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_AGENT_URL` | URL of the HTTP agent (e.g., https://domain.com/agent.php) | Yes |
| `--polling-interval` | Sets the polling frequency in milliseconds | Yes |
| `$_INTERVAL_MS` | Interval value (e.g., 2000 for 2 seconds) | Yes |

## Examples

### Basic Usage

```bash
pivotnacci https://domain.com/agent.php --polling-interval 2000
```

### Advanced Usage

```bash
pivotnacci https://domain.com/agent.php --polling-interval 5000 --password "s3cr3t"
```

## Expected Output

Output indicates startup:

SOCKS proxy listening on 127.0.0.1:1080
Polling interval set to 2000ms
Connected to agent.

## Related

- [[procedures/Web-SOCKS-Pivoting-with-Pivotnacci]]
