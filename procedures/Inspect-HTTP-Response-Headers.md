---
id: proc-inspect-http-headers
tags:
  - reconnaissance
  - web
  - headers
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-fetch-headers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:15:26.937Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Inspect-HTTP-Response-Headers

## Summary

This procedure retrieves and examines HTTP response headers from a target web server to identify security configurations, such as the presence of protective headers. It is commonly used in reconnaissance to uncover misconfigurations that could enable attacks like reflected XSS.

## Description

In web security assessments, inspecting HTTP headers reveals server details and security settings. The X-XSS-Protection header, for instance, instructs browsers to enable or block reflective XSS attempts. Absence of this header, as seen on https://doc.owncloud.org/, leaves sites vulnerable to script injection without browser intervention. This procedure targets public web endpoints and requires no authentication, making it suitable for initial vulnerability scouting on platforms like ownCloud documentation sites hosted on Nginx, Apache, or IIS.

## Requirements

1. Network access to the target URL (e.g., https://doc.owncloud.org/)
2. curl installed or browser with developer tools
3. Basic command-line knowledge

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor header inspection requests
- Log unusual curl or dev tools traffic patterns
- Enforce security headers via server configuration (e.g., add X-XSS-Protection: 1; mode=block in Nginx/Apache)

## Objectives

1. Retrieve all HTTP response headers from the target
2. Identify potential security weaknesses in header configuration
3. Document findings for further exploitation assessment

## Instructions

### Step 1: Fetch Headers Using curl

**Context**: Use curl to send a HEAD request and capture response headers without downloading the full body, focusing on metadata like security headers.

**Command** ([[commands/curl-fetch-headers]]):
```bash
curl -I https://doc.owncloud.org/
```

> This command outputs headers such as HTTP/1.1 200 OK, Server: nginx, Content-Type: text/html, etc. Look for security-related headers; absence indicates misconfiguration.

### Step 2: Analyze Output for Security Headers

**Context**: Manually or scripturally review the headers for key security entries like X-XSS-Protection, Content-Security-Policy, or Strict-Transport-Security.

**Command** ([[commands/curl-fetch-headers]] with grep):
```bash
curl -s -I https://doc.owncloud.org/ | grep -i xss
```

> Expected output: Empty if missing. Success confirms vulnerability to XSS without browser blocking.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-headers]]

## Tools Used


## Tags

- reconnaissance
- web
- headers
