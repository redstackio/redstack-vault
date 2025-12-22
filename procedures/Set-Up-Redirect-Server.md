---
tags:
  - redirect
  - server-setup
type: procedure
tools:
  - '[[tools/socat]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/socat-redirect-server]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 6cf1ddf4-7ea9-4552-9b2d-1fcf1afe5cdf
created_at: '2025-12-13T09:01:17.568Z'
updated_at: '2025-12-13T09:01:17.568Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set Up Redirect Server

## Summary

This procedure sets up a redirect server using socat to handle incoming connections on port 443 and redirect them to a malicious endpoint on port 8443, facilitating the exploitation of redirect vulnerabilities.

## Description

In the context of exploiting HTTP Request Smuggling for arbitrary redirects, this server acts as an intermediary that receives connections from manipulated Host headers and forces browsers to connect to a controlled malicious site. It requires control over a domain and uses chunked encoding exploits to trigger the redirects. The target environment is a web application vulnerable to request smuggling on specific paths like /sf.

## Requirements

1. Access to a server with socat installed
2. Control over a domain (e.g., pqp.mx) with ports 443 and 8443 open
3. Network accessibility from the target to the attacker's domain

## Defense

Defensive measures and detection strategies:

- Monitor for unusual redirect patterns in web server logs
- Implement strict request parsing and validation of Transfer-Encoding headers

## Objectives

1. Establish a listener for smuggled redirect requests
2. Force incoming connections to a malicious HTTPS endpoint
3. Confirm server readiness for exploitation

## Instructions

### Step 1: Launch Socat Listener

**Context**: This step initializes the TCP listener to respond with a 302 redirect.

**Command** ([[commands/socat-redirect-server]]):
```bash
socat -v -d -d TCP-LISTEN:443,crlf,reuseaddr,fork 'SYSTEM:/bin/echo "HTTP/1.1 302 Found";/bin/echo "Content-Length: 0";/bin/echo "Location: https://pqp.mx:8443";/bin/echo;/bin/echo'
```

> This command sets up verbose listening on port 443 and sends a redirect response to any incoming connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/socat-redirect-server]]

## Tools Used

- [[tools/socat]]

## Tags

- [[redirect]]
- [[server-setup]]
