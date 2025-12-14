---
id: proc-inspect-headers-clickjacking
tags:
  - clickjacking
  - headers
  - web-security
  - vulnerability-scanning
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-inspect-headers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Client Configurations]]'
updated_at: '2025-12-14T17:28:04.970Z'
skill_level: beginner
impact_level: informational
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Client Configurations]]'
---
# Inspect-HTTP-Headers-for-Clickjacking-Protection

## Summary

This procedure involves sending an HTTP HEAD request to a target web endpoint to inspect response headers for the absence of X-Frame-Options, identifying potential clickjacking vulnerabilities where the site can be embedded in iframes from malicious domains.

## Description

Clickjacking, or UI redressing, allows attackers to overlay invisible iframes on malicious pages to trick users into clicking unintended elements. The primary root cause is the lack of frame-busting headers like X-Frame-Options in HTTP responses. This procedure targets web applications like shop.khanacademy.org, using a simple HEAD request to retrieve headers without downloading the full body. Expected outcomes include confirming the vulnerability if no X-Frame-Options is present, enabling further assessment of impacts such as unauthorized actions via tricked clicks. Prerequisites include basic command-line access and internet connectivity; no authentication is required for public sites.

## Requirements

1. Command-line environment with curl installed
2. Network access to the target URL (e.g., http://shop.khanacademy.org/)
3. Basic knowledge of HTTP headers and security concepts

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in server configurations (e.g., nginx or Apache)
- Use Content-Security-Policy (CSP) frame-ancestors directive as a modern alternative
- Monitor server logs for unusual HEAD requests or iframe embedding attempts
- Employ web application firewalls (WAFs) to detect and block anomalous header inspections

## Objectives

1. Retrieve and analyze HTTP response headers from the target
2. Identify absence of clickjacking protections
3. Assess potential for UI redressing attacks

## Instructions

### Step 1: Send HEAD Request and Inspect Headers

**Context**: This step fetches only the HTTP headers from the target URL using a HEAD method, following any redirects, to check for frame-busting protections without loading the page content.

**Command** ([[commands/curl-inspect-headers]]):
```bash
curl -L -I http://shop.khanacademy.org/
```

> The -I flag performs a HEAD request, -L follows redirects, and the URL is the target endpoint. Expected output includes status code (e.g., 200 OK), Server: nginx, X-XSS-Protection: 1; mode=block, but notably no X-Frame-Options. If missing, the site can be iframed from any origin, enabling clickjacking.

### Step 2: Analyze Output for Vulnerabilities

**Context**: Manually review the headers for security-related entries. Absence of X-Frame-Options indicates the vulnerability.

**Command** (No additional command; use output from Step 1):

> Pipe the output to grep for specific headers if needed: `curl -L -I http://shop.khanacademy.org/ | grep -i frame`. Success is confirmed if no matching line appears for X-Frame-Options.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning
- [[Client Configurations]] Gather Victim Host Information: Client Configurations

### Sub-Techniques


## Commands Used

- [[commands/curl-inspect-headers]]

## Tools Used

- [[tools/curl]]

## Tags

- clickjacking
- web-security
- headers
