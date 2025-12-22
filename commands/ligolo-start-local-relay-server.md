---
id: e2191479-67e9-433d-8370-17fc904182f7
name: ligolo-start-local-relay-server
type: command
executor: bash
data: ./bin/localrelay_linux_amd64
output: null
created_at: '2023-04-06T03:56:22.820206+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ligolo
  - pivoting
verified: true
validated: true
---

# ligolo-start-local-relay-server

## Command

```bash
./bin/localrelay_linux_amd64
```

## Description

Starts the Ligolo local relay server on a Linux-based attack machine, listening for connections from Ligolo agents on compromised hosts to enable network tunneling and pivoting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The binary runs with default settings, listening on port 5555. Use flags like `-selfcert` for custom certificates if needed. | No |

## Examples

### Basic Usage

```bash
./bin/localrelay_linux_amd64
```

Starts the relay with default configuration.

### Advanced Usage

```bash
./bin/localrelay_linux_amd64 -selfcert -addr 0.0.0.0:5555
```

Binds to all interfaces with self-signed certificates for secure connections.

## Expected Output

The command outputs a message confirming the server startup, such as:

```
[INFO] Local relay server started on 0.0.0.0:5555
[INFO] Waiting for agent connections...
```

Subsequent agent connections will log session details.

## Related

- [[procedures/Ligolo-Local-Relay-Setup]]
- [[tools/Ligolo]]
