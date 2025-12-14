---
id: proc-uuid-003
tags:
  - xss
  - execution-trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.803Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS Execution via Admin Review

## Summary

This procedure relies on the project admin interacting with the tainted invite, causing the reflected XSS payload to execute JavaScript in their browser, confirming the vulnerability and enabling further compromise.

## Description

The admin's review page fetches and displays pending translator names without HTML escaping, rendering the injected SVG element. The onload event fires, executing the JavaScript. In a real attack, replace the proof-of-concept prompt with code to steal session cookies (e.g., document.cookie) or redirect to a phishing site. This exploits the trust in the admin interface and the elevated privileges of the admin account.

## Requirements

1. Pending join request with malicious payload
2. Social engineering or waiting for admin to review
3. Victim must use a vulnerable browser without XSS protections

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., htmlspecialchars) when rendering user data in HTML contexts
- Implement XSS auditors or browser extensions for admins
- Train admins to report suspicious prompts or behaviors during reviews

## Objectives

1. Cause payload rendering in admin context
2. Execute JavaScript for confirmation or exploitation
3. Achieve impacts like session theft or data access

## Instructions

### Step 1: Prepare for Review

**Context**: Ensure the admin is prompted to check invites.

- Send a notification or use social engineering (e.g., email) to urge review.
- Monitor indirectly if possible.

### Step 2: Admin Interaction

**Context**: The trigger occurs when the admin loads the review page.

Admin navigates to 'Project Settings > Pending Invites' and clicks the request link.

> The page renders: <div class="translator-name">"><svg onload="prompt(/xss/);"></div>, executing the script.

### Step 3: Verify Execution

**Context**: Observe or confirm the impact.

- In POC, a prompt appears in admin's browser.
- For advanced, exfiltrate data via fetch to attacker server.

> Expected output: JavaScript alert/prompt; potential console errors if blocked.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[javascript-execution]]
