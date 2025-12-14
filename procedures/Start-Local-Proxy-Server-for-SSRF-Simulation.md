---
id: proc-uuid-002
tags:
  - proxy
  - ssrf
  - simulation
type: procedure
tools:
  - '[[tools/proxy-py]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T03:53:38.556Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Start-Local-Proxy-Server-for-SSRF-Simulation

## Summary

This procedure launches a simple HTTP server on a local port to simulate an internal service, capturing SSRF requests during GitLab exploitation and returning 200 OK to confirm hits.

## Description

To observe SSRF in the GitLab attack, a local proxy listens on port 8500 (Consul's port) and logs incoming requests from the injected git proxy. This reveals leaked status codes and bodies. Run on the attacker's machine with port access; no credentials needed beyond local privileges.

## Requirements

1. Python environment for proxy.py
2. Port 8500 available on localhost
3. Firewall allowing inbound on 8500

## Defense

Defensive measures and detection strategies:

- Block unexpected local listeners on internal ports
- Monitor for unauthorized processes binding to service ports like 8500
- Use host-based firewalls to restrict localhost bindings

## Objectives

1. Bind to port 8500 for request capture
2. Return 200 OK to simulate successful internal access
3. Log SSRF payloads for analysis

## Instructions

### Step 1: Launch Proxy Server

**Context**: Start the Python-based proxy to listen on 8500, handling GET requests with a 200 response.

**Command** (Run proxy.py):
```bash
python3 proxy.py 8500
```

> The script should output 'Listening on 127.0.0.1:8500'. Test with curl localhost:8500/v1/config to confirm 200.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/proxy-py]]

## Tags

- proxy
- ssrf
