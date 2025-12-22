---
tags:
  - listener
  - setup
  - ssrf
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nc-listen]]'
platforms:
  - Linux
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 5bb8e8e7-c110-4eaf-8b0e-2736077128b0
created_at: '2025-12-14T04:39:09.926Z'
updated_at: '2025-12-14T04:39:09.926Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Set-Up-Attacker-Listener

## Summary

This procedure sets up a simple TCP listener on the attacker's server to capture incoming connections from a vulnerable target application during SSRF exploitation. It is a foundational step for receiving and logging server-side requests without requiring complex tools.

## Description

In an SSRF attack scenario, the attacker needs a reliable endpoint to receive forced requests from the target server. This procedure uses a basic netcat listener to bind to a port and display incoming data, allowing confirmation of the vulnerability. It assumes the attacker has control over a public-facing server and that the port is open (e.g., not blocked by firewalls). Expected outcomes include capturing HTTP requests that reveal the target's internal behavior.

## Requirements

1. Attacker-controlled server with public IP accessibility
2. Netcat installed (common on Linux/Unix systems)
3. Open outbound access from the target to the attacker's port (e.g., 8080)

## Defense

Defensive measures and detection strategies:

- Monitor for unusual outbound connections from web servers to unknown IPs
- Implement URL validation and whitelist external requests in application code
- Use web application firewalls (WAFs) to block fragment-based SSRF attempts

## Objectives

1. Establish a listening endpoint for SSRF payloads
2. Log incoming requests for analysis
3. Validate network reachability from the target

## Instructions

### Step 1: Start the Listener

**Context**: Bind netcat to a specific port to wait for connections from the target server.

**Command** ([[commands/nc-listen]]):
```bash
nc -lvp 8080
```

> This command starts netcat in listen mode (-l), verbose (-v), and prints port details (-p). Expected output includes a confirmation message, and it will hang waiting for input. Any incoming data (e.g., HTTP request) will be displayed in real-time.

### Step 2: Verify Listener Status

**Context**: Ensure the listener is active and testable before triggering the SSRF.

**Command** ([[commands/nc-listen]]):
```bash
nc -lvp 8080 &
```

> Run in background (&) for testing. Use telnet or curl from another terminal to test: `curl http://localhost:8080`. Success shows echoed request in netcat output.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/nc-listen]]

## Tools Used

- [[tools/netcat]]

## Tags

- [[listener]]
- [[ssrf]]
