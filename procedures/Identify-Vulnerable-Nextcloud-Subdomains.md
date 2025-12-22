---
tags:
  - clickjacking
  - recon
  - headers
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-check-headers]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.418Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 328b080a-7a4a-4508-9fbb-857130a9ad26
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Identify-Vulnerable-Nextcloud-Subdomains

## Summary

This procedure scans Nextcloud subdomains to detect the absence of the X-Frame-Options HTTP response header, identifying sites vulnerable to clickjacking attacks where pages can be embedded in iframes without restrictions.

## Description

In a clickjacking attack, the lack of frame-busting headers like X-Frame-Options allows attackers to embed victim sites in iframes on malicious pages. This procedure targets Nextcloud's public subdomains, listing 13 known ones (e.g., nextcloud.com, download.nextcloud.com) and using HTTP HEAD requests to check for the header. If missing, browsers permit unrestricted embedding, enabling UI redressing to trick users into unintended actions like submitting credentials.

## Requirements

1. Command-line access with curl installed
2. Internet connectivity to query public subdomains
3. List of target subdomains (e.g., from domain enumeration)

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN in web server configs (e.g., Nginx/Apache)
- Monitor for anomalous iframe embeddings via WAF logs or browser security tools like Content-Security-Policy (CSP) frame-ancestors
- Use browser extensions or security scanners to detect missing headers

## Objectives

1. Confirm vulnerability on multiple subdomains
2. Gather evidence for exploitation feasibility
3. Prepare list of targets for PoC development

## Instructions

### Step 1: List and Query Subdomain Headers

**Context**: Enumerate known Nextcloud subdomains and check each for the X-Frame-Options header using a HEAD request to avoid full page loads.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://nextcloud.com | grep -i x-frame-options || echo "Missing on nextcloud.com"
```

> This command sends a HEAD request and greps for the header. If no output, echo confirms absence. Expected output: Either the header value or "Missing". Repeat for each subdomain like https://download.nextcloud.com, https://docs.nextcloud.com, etc., covering all 13 listed.

### Step 2: Document Vulnerable Targets

**Context**: Compile results into a list for further exploitation steps.

**Command** (Manual logging, no specific command):

> Save outputs to a file, e.g., vulnerable.txt, noting each missing header subdomain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/curl-check-headers]]

## Tools Used


## Tags

- [[clickjacking]]
- [[recon]]
- [[web-headers]]
