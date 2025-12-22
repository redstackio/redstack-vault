---
id: cmd-mitmproxy-capture
data: mitmproxy --mode transparent --listen-port 8080
tags:
  - network
  - proxy
  - interception
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.495Z'
verified: false
validated: true
submitted: true
---
# mitmproxy-capture

## Command

```bash
mitmproxy --mode transparent --listen-port 8080
```

## Description

Starts mitmproxy in transparent mode to capture and intercept network traffic on port 8080, useful for analyzing HTTP requests from mobile apps without explicit browser configuration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--mode transparent` | Enables transparent proxying for seamless traffic routing | Yes |
| `--listen-port 8080` | Specifies the port for listening to incoming traffic | Yes |

## Examples

### Basic Usage

```bash
mitmproxy --mode transparent --listen-port 8080
```

### Advanced Usage

```bash
mitmproxy --mode transparent --listen-port 8080 --set confdir=~/.mitmproxy
```

## Expected Output

Interactive console opens showing real-time traffic flows; press 'f' to filter, 'q' to quit. Captured requests display headers, body, and metadata.

## Related

- [[Related Procedure]]
