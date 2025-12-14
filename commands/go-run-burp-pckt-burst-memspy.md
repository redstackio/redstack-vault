---
data: go run burp-pckt-burst-memspy.go
tags:
  - go
  - server
  - poc
type: command
output: null
executor: bash
platforms:
  - Linux
  - Desktop
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.410Z'
id: 5e28b9b9-9749-4379-b783-e05d4cd024ae
verified: false
validated: true
submitted: true
---
# go-run-burp-pckt-burst-memspy

## Command

```bash
go run burp-pckt-burst-memspy.go
```

## Description

Compiles and starts a custom Go HTTP server that holds incoming connections to /memspy until a limit (e.g., 20) is reached, then bursts malformed responses to trigger races in Burp Suite's JSBeautifier.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `burp-pckt-burst-memspy.go` | Source file with server logic, connLimit, and random body generation | Yes |

## Examples

### Basic Usage

```bash
go run burp-pckt-burst-memspy.go
```

### Advanced Usage

```bash
go build burp-pckt-burst-memspy.go && ./burp-pckt-burst-memspy -port=8000 -limit=50
```

(Assumes flags added to source for customization.)

## Expected Output

Server logs connection counts in hex (e.g., "Listening on 127.0.0.1:8000\n0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X") where 'X' indicates burst and response flush.

## Related

- [[procedures/Build-and-Run-Custom-Go-HTTP-Server-for-Request-Bursting]]
