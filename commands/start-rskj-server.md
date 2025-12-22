---
id: cmd-uuid-1
data: >-
  java -classpath rskj-core-5.0.0-FINGERROOT-all.jar -Drpc.providers.web.cors=*
  -Drpc.providers.web.ws.enabled=true co.rsk.Start
tags:
  - execution
  - rskj
type: command
output: 'Server startup logs, including ''Listening on UDPv6 port 5050'''
executor: bash
platforms:
  - Linux
  - Java
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.325Z'
verified: false
validated: true
submitted: true
---
# start-rskj-server

## Command

```bash
java -classpath rskj-core-5.0.0-FINGERROOT-all.jar -Drpc.providers.web.cors=* -Drpc.providers.web.ws.enabled=true co.rsk.Start
```

## Description

This command launches the vulnerable RSKJ node server using Java, specifying the classpath to the JAR file and enabling CORS for all origins and WebSocket RPC, which opens the UDPv6 listener on port 5050 vulnerable to RLP DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-classpath` | Path to the rskj-core JAR file | Yes |
| `-Drpc.providers.web.cors=*` | Enables CORS for all domains | No (but used for full setup) |
| `-Drpc.providers.web.ws.enabled=true` | Activates WebSocket for RPC providers | No (but used for full setup) |
| `co.rsk.Start` | Main class to start the RSKJ application | Yes |

## Examples

### Basic Usage

```bash
java -classpath rskj-core-5.0.0-FINGERROOT-all.jar co.rsk.Start
```

### Advanced Usage

```bash
java -classpath rskj-core-5.0.0-FINGERROOT-all.jar -Drpc.providers.web.cors=* -Drpc.providers.web.ws.enabled=true -Xmx1g co.rsk.Start
```

## Expected Output

Console output includes initialization messages, configuration loading, and confirmation of network listeners: "Node started successfully. Listening on UDPv6 port 5050 for peer discovery and communications."

## Related

- [[procedures/Launch-Vulnerable-RSKJ-Node]]
- [[procedures/Obtain-Vulnerable-RSKJ-Software]]
