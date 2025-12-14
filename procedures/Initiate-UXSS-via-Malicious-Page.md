---
id: proc-uxss-init-001
tags:
  - uxss
  - drive-by-compromise
  - browser-exploitation
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
updated_at: '2025-12-14T17:27:35.796Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Initiate UXSS via Malicious Page

## Summary

This procedure tricks a logged-in HackerOne user into visiting an attacker-controlled malicious page in a vulnerable browser (e.g., Internet Explorer), exploiting a UXSS vulnerability to enable cross-origin interactions without direct JavaScript execution on the target domain.

## Description

The attack relies on known UXSS bugs in browsers like IE, where visiting a malicious page allows framing and limited script execution on cross-origin sites like HackerOne. This sets up token extraction by bypassing Same-Origin Policy (SOP) restrictions. Prerequisites include the victim being authenticated on HackerOne and using a vulnerable browser version. Expected outcome: Establishment of a cross-origin frame for further exploitation.

## Requirements

1. Attacker-controlled domain to host the malicious HTML page
2. Victim logged into HackerOne in a browser with UXSS vulnerability (e.g., IE 11 with specific patches missing)
3. No additional tools; relies on browser flaws like those referenced in CVE or blog posts on IE UXSS

## Defense

Defensive measures and detection strategies:

- Enforce modern browsers without known UXSS vulnerabilities
- Implement Content Security Policy (CSP) to restrict framing and script execution
- Monitor for anomalous cross-origin requests from user sessions

## Objectives

1. Gain initial cross-origin access via browser vulnerability
2. Position for CSRF token extraction
3. Enable unauthorized actions without user consent

## Instructions

### Step 1: Host Malicious Page

**Context**: Create and deploy an HTML page that triggers the UXSS upon loading, targeting the victim's browser to frame HackerOne resources.

Embed the following JavaScript in the malicious page to initiate framing:

```html
<iframe src="https://hackerone.com/cdn-cgi/trace"></iframe>
<script>
  // Exploit UXSS to interact with framed content
  // Specific IE UXSS payload (e.g., re-implementation from blog references)
  var iframe = document.querySelector('iframe');
  // Trigger cross-origin access
</script>
```

> This loads the page and exploits the browser bug to allow subsequent AJAX without SOP blocks. Expected output: Frame loads without X-Frame-Options denial.

### Step 2: Lure Victim

**Context**: Socially engineer the victim to visit the page while logged into HackerOne.

Distribute the malicious URL via phishing or compromised sites. No command needed; monitor access logs on attacker server.

> Expected output: Victim browser executes the UXSS payload silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- uxss
- browser-exploit
