---
id: proc-lactate-start-001
name: Start-Vulnerable-Lactate-Server
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.022Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - server-start
  - web-server
  - vulnerable-setup
commands:
  - '[[commands/lactate-start-server]]'
platforms:
  - Linux
  - Web
tools:
  - '[[tools/lactate]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Start-Vulnerable-Lactate-Server

## Summary

This procedure launches the lactate static web server on port 8081, serving files from the current directory (/root), exposing the path traversal vulnerability for exploitation.

## Description

The lactate server (v0.13.12) is a lightweight Node.js tool for serving static files but fails to sanitize user-supplied paths, allowing directory traversal. This step assumes prior installation and directory setup. The server runs in the foreground, listening for HTTP requests on the specified port.

## Requirements

1. Lactate installed globally
2. Current directory set to web root (e.g., /root)
3. Port 8081 free and firewall permitting inbound traffic

## Defense

Defensive measures and detection strategies:

- Input validation on path parameters in custom servers
- Use WAF rules to block '../' patterns in URLs
- Network monitoring for unusual port bindings (e.g., via netstat or fail2ban)

## Objectives

1. Bind the server to port 8081
2. Confirm it's serving from /root
3. Verify accessibility without errors

## Instructions

### Step 1: Launch the Server

**Context**: Start the server to expose the vulnerable endpoint for path traversal testing.

**Command** ([[commands/lactate-start-server]]):
```bash
lactate -p 8081
```

> The -p flag specifies the port; expected output includes "Server listening on port 8081" and remains running until interrupted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/lactate-start-server]]

## Tools Used

- [[tools/lactate]]

## Tags

- server-start
- web-server
- vulnerable-setup
