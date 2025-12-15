---
id: p-identify-frameable-endpoints
tags:
  - recon
  - web
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:28:05.005Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Frameable Login Endpoints

## Summary

This procedure scans a target login page for missing frame-busting protections like X-Frame-Options headers, allowing identification of clickjacking opportunities by confirming the page can be embedded in an iframe.

## Description

In a clickjacking attack, attackers exploit web pages that lack protections against being framed. This procedure involves inspecting HTTP headers and testing iframe embedding to verify vulnerability. It targets public-facing login endpoints, such as https://hackers.upchieve.org/login, where absence of headers enables embedding on attacker sites. Expected outcomes include confirmation of frameability, setting the stage for credential theft via deception.

## Requirements

1. Access to curl or a similar HTTP client
2. Target URL publicly accessible
3. Web browser for manual iframe testing

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers
- Use Content-Security-Policy with frame-ancestors directive
- Monitor for unusual iframe embeddings via WAF logs

## Objectives

1. Confirm absence of frame protections
2. Validate page embeddability in iframe
3. Identify potential for clickjacking exploitation

## Instructions

### Step 1: Check Response Headers

**Context**: Retrieve and inspect HTTP headers to detect missing X-Frame-Options or CSP frame-ancestors.

**Command** ([[commands/curl-check-headers]]):
```bash
curl -I https://hackers.upchieve.org/login
```

> This command fetches headers only. Look for X-Frame-Options; if absent, the page is potentially frameable. Expected output includes status 200 and no frame-busting directives.

### Step 2: Test Iframe Embedding

**Context**: Manually verify if the page can be loaded in an iframe using a local HTML file.

Create and open this HTML in a browser:

```html
<!DOCTYPE html>
<html><body><iframe src="https://hackers.upchieve.org/login" width="800" height="600"></iframe></body></html>
```

> If the login page loads without errors or blocks, it's vulnerable. Expected output: Full page render inside iframe.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-headers]]

## Tools Used


## Tags

- [[recon]]
- [[web]]
