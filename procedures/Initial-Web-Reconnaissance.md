---
tags:
  - reconnaissance
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: de67ecb7-76c6-47b4-a759-d35210cbcd9c
created_at: '2025-12-14T17:29:56.722Z'
updated_at: '2025-12-14T17:29:56.722Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Initial-Web-Reconnaissance

## Summary

This procedure involves visiting the target web domain to confirm accessibility and initiate passive reconnaissance, setting the stage for deeper scanning without executing any intrusive actions.

## Description

In web-based attacks, initial reconnaissance confirms the target's online presence and responsiveness. Here, accessing the main domain (e.g., https://h2f54.n1.ips.mtn.co.ug) verifies the web server is operational, often revealing basic site structure or errors that hint at technologies in use. This step requires no special tools beyond a browser and assumes public-facing access. Expected outcomes include confirmation of HTTP/HTTPS service and any immediate visible misconfigurations.

## Requirements

1. Internet access to the target domain
2. Standard web browser (e.g., Chrome, Firefox)
3. No authentication or special permissions needed

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to log unusual access patterns
- Monitor server logs for repeated requests from unknown IPs
- Use rate limiting on public endpoints to deter scanning

## Objectives

1. Verify target domain responsiveness
2. Observe initial site behavior for tech stack hints
3. Establish baseline for subsequent active scanning

## Instructions

### Step 1: Navigate to Target Domain

**Context**: Use a browser to directly access the root URL, noting any redirects, errors, or content that indicates the platform.

No specific command required; manually enter the URL in the browser address bar.

> Successful access shows the homepage loading, potentially revealing PHP or Windows indicators in headers or source code.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[web]]
