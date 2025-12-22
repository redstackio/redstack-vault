---
id: proc-discover-dom-xss-endpoint
tags:
  - reconnaissance
  - web-enumeration
  - dom-xss
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-13T23:52:21.041Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover-Vulnerable-Endpoint-for-DOM-XSS

## Summary

This procedure involves identifying public endpoints on a web application, specifically locating the attach.html file on iqcard.informatica.com that is vulnerable to DOM-based XSS due to its directory structure under /pub/fujitsu/fm3v2/player/.

## Description

In web vulnerability assessments, discovering exposed paths is crucial for identifying potential injection points. Here, the endpoint iqcard.informatica.com/pub/fujitsu/fm3v2/player/attach.html was found through manual exploration or directory traversal, revealing JavaScript that processes URL parameters insecurely. This step sets the stage for deeper analysis and exploitation, applicable in reconnaissance phases of penetration testing against public web apps.

## Requirements

1. Internet access to the target domain (iqcard.informatica.com)
2. Web browser for manual navigation
3. Basic knowledge of URL structures and directory enumeration

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor unusual path access
- Use directory listing protections and robots.txt to obscure internal paths
- Regularly scan for exposed endpoints with tools like OWASP ZAP

## Objectives

1. Locate the specific vulnerable attach.html endpoint
2. Confirm public accessibility without authentication
3. Prepare for source code inspection

## Instructions

### Step 1: Enumerate Public Directories

**Context**: Start by navigating to the base domain and exploring common public paths like /pub/ to identify legacy or exposed directories.

No specific command; use browser to visit https://iqcard.informatica.com/pub/ and drill down to /fujitsu/fm3v2/player/attach.html.

> Manually append paths in the browser URL bar and check for 200 OK responses.

### Step 2: Verify Endpoint Accessibility

**Context**: Ensure the attach.html loads without errors, indicating it's a valid and potentially exploitable resource.

Load the full URL: https://iqcard.informatica.com/pub/fujitsu/fm3v2/player/attach.html.

> Expected output: Page renders with minimal content, likely a blank or player-related HTML file.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[web-enumeration]]
- [[dom-xss]]
