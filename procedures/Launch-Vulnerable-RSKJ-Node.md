---
id: proc-uuid-2
tags:
  - execution
  - java
  - rskj-server
type: procedure
tools:
  - '[[tools/Java]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/start-rskj-server]]'
verified: false
platforms:
  - Java
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:56.340Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Launch-Vulnerable-RSKJ-Node

## Summary

This procedure starts the RSKJ node server using the vulnerable JAR file, exposing the UDPv6 listener on port 5050 where the RLP decoding vulnerability can be exploited, simulating a production-like environment for the denial-of-service attack.

## Description

The RSKJ server is a Java-based Rootstock node that listens on UDPv6 port 5050 for peer communications. Launching it with specific flags enables CORS and WebSocket RPC, but the core vulnerability lies in the RLP.java decode2 function (lines 432, 440, 405, 403, 490), where bytesToLength can return -5, causing length=0 and an infinite loop. This step requires Java runtime and the JAR file; expected outcome is the server running and bound to the port, vulnerable to crafted packets. Target environment is Linux with Java 8+.

## Requirements

1. Downloaded rskj-core-5.0.0-FINGERROOT-all.jar
2. Java runtime environment installed
3. Linux host with sufficient resources (at least 1GB RAM for crash simulation)

## Defense

Defensive measures and detection strategies:

- Run servers in containers with resource limits to prevent OOM crashes
- Monitor Java process resource usage and UDP traffic spikes
- Deploy input validation for RLP decoding in custom patches

## Objectives

1. Expose the vulnerable UDPv6 endpoint for exploitation
2. Confirm server is operational and listening on port 5050
3. Prepare for incoming malicious UDP packets

## Instructions

### Step 1: Execute Server Launch Command

**Context**: Use the Java command to start the RSKJ node with the vulnerable JAR and required flags.

**Command** ([[commands/start-rskj-server]]):
```bash
java -classpath rskj-core-5.0.0-FINGERROOT-all.jar -Drpc.providers.web.cors=* -Drpc.providers.web.ws.enabled=true co.rsk.Start
```

> This launches the main class co.rsk.Start, enabling CORS (*) and WebSocket RPC (true). Expected output: Console logs showing node startup and "Listening on UDPv6 port 5050".

### Step 2: Verify Port Binding

**Context**: Confirm the UDPv6 listener is active.

Use netstat to check:

```bash
netstat -ulnp | grep 5050
```

> Expected output: UDP listener on :::5050 (IPv6).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/start-rskj-server]]

## Tools Used

- [[tools/Java]]

## Tags

- [[Execution]]
- [[tools/Java]]
- [[rskj-server]]
