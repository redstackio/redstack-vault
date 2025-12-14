---
data: 'curl -m3 mqtt://localhost:12345'
tags:
  - dos
  - curl
  - mitigation
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.638Z'
id: 0d8ab77f-66aa-4d33-8e77-45c95af39abb
verified: false
validated: true
submitted: true
---
# curl-mqtt-with-timeout

## Command

```bash
curl -m3 mqtt://localhost:12345
```

## Description

This command tests the MQTT DoS trigger with a 3-second timeout to demonstrate mitigation and prevent indefinite hanging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-m3` | Maximum time of 3 seconds for the operation | Yes |
| `mqtt://localhost:12345` | MQTT URL to the server | Yes |

## Examples

### Basic Usage

```bash
curl -m3 mqtt://localhost:12345
```

### Advanced Usage

```bash
curl -m3 -v mqtt://localhost:12345
```

## Expected Output

curl attempts the connection, enters the loop briefly, then times out after 3 seconds with a message like 'curl: (28) Operation timed out'.

## Related

- [[commands/curl-mqtt-dos-trigger]]
- [[procedures/Trigger-curl-DoS-with-MQTT-URL]]
