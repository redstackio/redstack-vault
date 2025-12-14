---
id: cmd-nc-listen-3001
data: netcat -l -p 3001 -v
tags:
  - network
  - listener
type: command
output: |-
  Listening on [0.0.0.0] (family 0, port 3001)
  Connection from [IP] port 3001 [tcp/*] accepted
  GET /?evil=var HTTP/1.0
  Host: [target]
  Accept-Encoding: gzip
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.490Z'
verified: false
validated: true
submitted: true
---
# netcat-listen-on-port

## Command

```bash
netcat -l -p 3001 -v
```

## Description

This command uses netcat to listen for incoming TCP connections on port 3001 in verbose mode, useful for capturing SSRF-triggered HTTP requests from servers like Shopify during vulnerability testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Listen mode for incoming connections | Yes |
| `-p 3001` | Specify the port to listen on | Yes |
| `-v` | Verbose output to display connection details | Yes |

## Examples

### Basic Usage

```bash
netcat -l -p 3001 -v
```

### Advanced Usage

```bash
netcat -l -p 8080 -v -e /bin/bash
```
(For shell access, but not used here.)

## Expected Output

Description of what output to expect when the command runs successfully: Initial listen confirmation, followed by connection logs and raw HTTP request data upon incoming traffic.

## Related

- [[Related Procedure|procedures/Set-Up-Netcat-Listener-for-SSRF]]
