---
tags:
  - clickjacking
  - headers
  - nextcloud
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.187Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 00868995-0839-4ee0-9dd3-54dbefeb102b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Verify-Nextcloud-Login-Page-Accessibility

## Summary

This procedure verifies the accessibility of the Nextcloud login page and checks for the absence of the X-Frame-Options header, a prerequisite for clickjacking exploitation.

## Description

In a clickjacking attack, the target page must be publicly accessible and framable. This step involves loading the Nextcloud login page (e.g., https://portal.nextcloud.com/login.php) in a browser and inspecting HTTP response headers using developer tools to confirm no X-Frame-Options is set, allowing embedding in iframes on malicious sites. The expected outcome is confirmation of vulnerability, enabling subsequent embedding steps. Prerequisites include internet access and a modern web browser.

## Requirements

1. Internet connectivity to access public URLs
2. Web browser with developer tools (e.g., Chrome DevTools)
3. No authentication required for the login page

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN header on all pages
- Use Content-Security-Policy (CSP) frame-ancestors directive to restrict framing
- Monitor for anomalous iframe embeddings via web application firewall (WAF) logs

## Objectives

1. Confirm page loads without errors
2. Identify missing security headers
3. Validate potential for iframe embedding

## Instructions

### Step 1: Load the Target Page

**Context**: Access the Nextcloud login page to ensure it's reachable.

Open https://portal.nextcloud.com/login.php or https://nextcloud.com/ in your browser.

> The page should display the login form without redirects or errors.

### Step 2: Inspect HTTP Headers

**Context**: Check response headers for X-Frame-Options absence.

In browser developer tools (F12), navigate to the Network tab, reload the page, and select the request for login.php. Examine response headers.

> Look for absence of X-Frame-Options; if missing, the page is framable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- clickjacking
- headers
- reconnaissance
