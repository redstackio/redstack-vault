---
tags:
  - csrf
  - phishing
  - drive-by
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
updated_at: '2025-12-14T17:27:15.922Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7b9f240a-bf9a-4e5f-89f0-80d68e252dfb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deliver-CSRF-Attack-via-Malicious-Webpage

## Summary

This procedure outlines the delivery of a CSRF attack by tricking authenticated users into visiting a malicious webpage that automatically submits forged requests to vulnerable endpoints, exemplified by forcing changes to TopCoder wiki user preferences.

## Description

Delivery relies on social engineering to direct victims to the PoC HTML page while they remain logged into the target application. For TopCoder wiki, the malicious page hosts the auto-submitting forms, leveraging the browser's automatic inclusion of session cookies in cross-origin POST requests. Impact includes unauthorized modifications to general and email preferences, potentially disrupting user experience or enabling further attacks like spam redirection. Prerequisites: Functional PoC HTML from prior steps; a hosting method (e.g., free web host); victim must be authenticated to https://apps.topcoder.com/wiki.

## Requirements

1. Hosted PoC HTML files accessible via URL
2. Social engineering vector (e.g., email, link in forum)
3. Victim authentication to the target wiki
4. Monitoring capability to verify request success

## Defense

Defensive measures and detection strategies:

- Deploy Content Security Policy (CSP) to restrict form submissions
- Implement user confirmation dialogs for sensitive changes
- Scan for and block known malicious domains in email filters
- Audit logs for cross-origin requests and unexpected updates

## Objectives

1. Induce victim visit to malicious page during active session
2. Trigger forged requests to alter preferences
3. Confirm impact through preference verification

## Instructions

### Step 1: Host the PoC Files

**Context**: Make the HTML accessible over the web for victim access.

Upload csrf_general.html and csrf_mail.html to a hosting service (e.g., GitHub Pages, ngrok for local testing).

Obtain URLs like https://attacker.com/csrf_general.html.

> Ensure HTTPS to avoid mixed content blocks.

### Step 2: Lure the Victim

**Context**: Use phishing or other methods to direct the victim to the page while authenticated.

Send a link via email or embed in a seemingly legitimate site: "Click here to view TopCoder updates: [malicious URL]".

Target users known to be logged into TopCoder (e.g., via prior recon).

> Victim's browser will auto-submit if they visit while session is active.

### Step 3: Execute and Verify

**Context**: Monitor for successful request delivery and impact.

Upon visit, the page loads and submits POST to TopCoder endpoints.

Check victim account (if accessible) or wait for reports of changed preferences.

> Expected output: Preferences updated (e.g., email notifications disabled); server may log the request from attacker's domain.

### Step 4: Cleanup and Evasion

**Context**: Minimize detection post-attack.

Remove or redirect the malicious page after exploitation.

> Use URL shorteners or redirects to obscure the source.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[drive-by]]
- [[Phishing]]
