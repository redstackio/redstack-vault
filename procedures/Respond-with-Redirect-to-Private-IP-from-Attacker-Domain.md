---
id: proc-respond-redirect-private-ip-187520
tags:
  - ssrf
  - redirect
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/serve-redirect-response]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:30.703Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Respond-with-Redirect-to-Private-IP-from-Attacker-Domain

## Summary

This procedure involves responding to the WordPress scrape with a 302 redirect to a private IP:port, bypassing built-in filters that block direct private access, and optionally injecting basic auth.

## Description

WordPress's Press This follows HTTP redirects without validating the Location header, allowing an external host (attacker.com) to redirect to internal endpoints like 192.168.0.1:12345. Filters only apply to the initial u= URL, not redirects. Basic auth can be embedded (e.g., admin:admin@) to inject credentials. This enables SSRF to any internal service. Expected outcome: WordPress sends request to private endpoint.

## Requirements

1. Control of response on attacker domain
2. Knowledge of target private IPs/ports and credentials
3. HTTP server capable of custom 302 responses

## Defense

Defensive measures and detection strategies:

- Implement redirect validation to block private IPs in Location headers
- Disable redirect following in scraping functions
- Monitor for unexpected internal requests from web servers

## Objectives

1. Hijack scrape response to redirect internally
2. Bypass IP/port whitelists (e.g., only 80/443/8080 allowed initially)
3. Inject auth for service compromise

## Instructions

### Step 1: Set Up Redirect Server

**Context**: Configure server to return 302 with private Location.

**Command** ([[commands/serve-redirect-response]]):
```bash
echo -e "HTTP/1.1 302 Found\r\nLocation: http://192.168.0.1:12345\r\nContent-Length: 0\r\n\r\n" | nc -l -p 80
```

> Responds to incoming scrape with basic redirect. Expected output: Client (WordPress) receives 302 and follows.

### Step 2: Include Basic Auth in Redirect

**Context**: Enhance redirect with credentials for auth injection.

**Command** ([[commands/serve-auth-redirect]]):
```bash
echo -e "HTTP/1.1 302 Found\r\nLocation: http://admin:admin@192.168.0.1:12345\r\nContent-Length: 0\r\n\r\n" | nc -l -p 80
```

> Embeds basic auth; WordPress will forward as Authorization header. Expected output: Internal request includes Basic YWRtaW46YWRtaW4=.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/serve-redirect-response]]
- [[commands/serve-auth-redirect]]

## Tools Used

- None

## Tags

- [[ssrf]]
- [[redirect]]
