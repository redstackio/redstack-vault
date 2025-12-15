---
data: 'socat -u FILE:poc TCP-LISTEN:12345,reuseaddr,fork'
tags:
  - server-setup
  - mqtt
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.659Z'
id: a8a42294-279d-42d2-bc18-f4be444b6d7d
verified: false
validated: true
submitted: true
---
# socat-mqtt-server-setup

## Command

```bash
socat -u FILE:poc TCP-LISTEN:12345,reuseaddr,fork
```

## Description

This command creates a TCP listener on port 12345 that serves content from the 'poc' file unidirectionally to connecting clients, forking a new process per connection to handle the malicious MQTT response for DoS reproduction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Unidirectional mode (data from FILE to TCP) | Yes |
| `FILE:poc` | Source file containing the 5-byte MQTT payload | Yes |
| `TCP-LISTEN:12345` | Listen on TCP port 12345 | Yes |
| `reuseaddr` | Allow address reuse for quick restarts | No |
| `fork` | Fork new process for each incoming connection | Yes |

## Examples

### Basic Usage

```bash
socat -u FILE:poc TCP-LISTEN:12345,reuseaddr,fork
```

### Advanced Usage

```bash
socat -u FILE:poc TCP-LISTEN:12345,reuseaddr,fork,verbose
```

## Expected Output

The command runs silently in the foreground, serving the poc file to clients and maintaining the listener. Interrupt with Ctrl+C to stop. Successful connections log minimally unless verbose is added.

## Related

- [[commands/curl-mqtt-dos-trigger]]
- [[procedures/Set-Up-Malicious-MQTT-Server-with-socat]]
