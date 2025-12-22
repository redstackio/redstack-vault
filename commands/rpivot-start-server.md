---
id: 3a6bbbb9-80fb-4573-ba0e-69c7c767463f
type: command
executor: bash
data: python server.py --proxy-port 1080 --server-port 9443 --server-ip 0.0.0.0
output: null
created_at: '2023-04-06T03:56:22.866741+00:00'
updated_at: '2023-04-10T20:25:21.419917+00:00'
platforms:
  - Linux
  - Windows
tags:
  - pivoting
  - proxy
verified: true
validated: true
---

# rpivot-start-server

## Command

```bash
python server.py --proxy-port 1080 --server-port 9443 --server-ip 0.0.0.0
```

## Description

Starts the Rpivot proxy server on the attacker's machine, listening for client connections and forwarding traffic via SOCKS proxy. Use this to establish the pivoting endpoint before connecting clients.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --proxy-port 1080 | Local SOCKS proxy port for incoming requests | Yes |
| --server-port 9443 | Port for client-server communication | Yes |
| --server-ip 0.0.0.0 | IP to bind the server (0.0.0.0 for all interfaces) | Yes |

## Examples

### Basic Usage

```bash
python server.py --proxy-port 1080 --server-port 9443 --server-ip 0.0.0.0
```

### Advanced Usage

To change ports:
```bash
python server.py --proxy-port 1085 --server-port 9445 --server-ip 0.0.0.0
```

## Expected Output

Server logs indicating successful binding:
```
Server listening on 0.0.0.0:9443 for clients
Proxy listening on 0.0.0.0:1080
Waiting for connections...
```
No errors in binding ports; ready for client connections.

## Related

- [[procedures/Rpivot-Network-Pivoting]]
- [[commands/rpivot-start-client]]
