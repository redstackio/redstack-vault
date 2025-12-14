---
tags:
  - csrf
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:15.614Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a0ad9f27-be06-4909-96aa-413164f62868
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger-CSRF-for-Press-This-Endpoint

## Summary

This procedure exploits the lack of CSRF protection on the WordPress Press This scan endpoint by crafting a malicious img tag on an attacker-controlled site, tricking an authenticated user into triggering an unauthorized server request.

## Description

In WordPress, the /wp-admin/press-this.php endpoint accepts GET parameters 'u' for the URL to scan and 'url-scan-submit=Scan' to initiate scraping. Without CSRF tokens for GET requests, an attacker can embed this in a cross-site img tag, leveraging the victim's session cookies to invoke the endpoint from their browser. This allows remote triggering of server-side actions without user awareness, setting up SSRF exploitation.

## Requirements

1. Control over a website to host the malicious HTML
2. Knowledge of the victim's WordPress domain (e.g., myWordpress.com)
3. Victim must be authenticated to WordPress admin

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens for all state-changing endpoints, even GET if they trigger actions
- Validate and sanitize URL parameters to block internal IPs
- Monitor for anomalous requests to admin endpoints from user agents

## Objectives

1. Force victim's browser to send authenticated request to Press This endpoint
2. Bypass CSRF protections via cross-site embedding
3. Enable subsequent SSRF without direct access

## Instructions

### Step 1: Craft Malicious HTML Payload

**Context**: Create an invisible img tag that loads the vulnerable endpoint with scan parameters.

**Command** (HTML snippet):
```html
<img src="//myWordpress.com/wp-admin/press-this.php?u=http://internal-target&url-scan-submit=Scan" width="1" height="1" style="display:none;" />
```

> The protocol-relative URL (//) ensures the request uses the victim's protocol (HTTP/HTTPS). Embed this in a page on evil.com. When loaded, the browser sends the GET request using victim's cookies.

### Step 2: Distribute and Trigger

**Context**: Lure the victim to the page to execute the request.

**Instructions**: Send phishing link to victim. Upon page load, monitor network traffic or use a proxy to confirm the request hits the WordPress server.

> Expected: 200 OK or redirect response indicating processing; no alert to victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[csrf]]
- [[wordpress]]
