---
id: cmd-001
data: nc -l -p 666
tags:
  - network
  - listen
  - capture
type: command
output: >-
  Incoming HTTP request: GET / HTTP/1.1\r\nHost:
  159.203.190.123:666\r\nAuthorization: Basic YWRtaW46YWRtaW4=\r\nUser-Agent:
  Photon/1.0\r\nAccept: */*
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.038Z'
verified: false
validated: true
submitted: true
---
# nc-listen-on-port

## Command

```bash
nc -l -p 666
```

## Description

This command uses Netcat (nc) to listen for incoming TCP connections on a specified port, useful for capturing SSRF requests or debugging network interactions in security testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Listen mode for incoming connections | Yes |
| `-p 666` | Specify the port to listen on (e.g., 666 for non-standard testing) | Yes |

## Examples

### Basic Usage

```bash
nc -l -p 666
```

### Advanced Usage

```bash
nc -l -p 8080 -v
```

(Adds verbose output with -v flag.)

## Expected Output

When a connection is made, it displays raw input like HTTP requests, e.g., GET / HTTP/1.1 followed by headers such as Host, Authorization, and User-Agent.

## Related

- [[Related Procedure: Capture-SSRF-Request-with-Netcat]]
