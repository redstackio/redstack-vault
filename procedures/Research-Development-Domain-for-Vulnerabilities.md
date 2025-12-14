---
id: proc-uuid-001
tags:
  - recon
  - domain-research
  - info-disclosure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-directory-list]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:25:12.587Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Research-Development-Domain-for-Vulnerabilities

## Summary

This procedure involves initial reconnaissance of a development domain to identify potential misconfigurations or exposed resources, such as open directories on servers like cards-dev.twitter.com.

## Description

In attack scenarios targeting development environments, researchers often start by exploring public domains for overlooked endpoints. This procedure simulates manual browsing to uncover issues like exposed directories containing sensitive data. The target is a web server on HTTPS (port 443), and success leads to identifying paths like /keys/ for further exploitation. Prerequisites include internet access and a web browser; no special privileges are needed.

## Requirements

1. Internet connectivity to resolve and access the target domain (e.g., cards-dev.twitter.com)
2. Web browser (e.g., Chrome, Firefox) or command-line tool like curl
3. Basic understanding of HTTP endpoints and common misconfigurations

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor anomalous browsing patterns
- Regularly audit development servers for exposed directories using tools like OWASP ZAP
- Use robots.txt and directory indexing restrictions (e.g., Options -Indexes in Apache)

## Objectives

1. Map the attack surface of the development domain
2. Identify publicly accessible paths without authentication
3. Uncover potential information disclosure opportunities

## Instructions

### Step 1: Resolve and Access Domain Root

**Context**: Start by verifying the domain is live and exploring the root path for clues.

**Command** ([[commands/curl-directory-list]]):
```bash
curl -k https://cards-dev.twitter.com/
```

> This command fetches the root page, revealing any visible links or errors indicating development status. Expected output: HTML content or a default page confirming the server is active.

### Step 2: Probe Common Sensitive Paths

**Context**: Manually or programmatically test paths like /admin, /keys, or /config for exposure.

**Command** ([[commands/curl-directory-list]]):
```bash
curl -k https://cards-dev.twitter.com/keys/
```

> Look for directory listings or file downloads in the response. Expected output: Redirect to file download or 200 OK with JSON content.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/curl-directory-list]]

## Tools Used


## Tags

- recon
- domain-research
