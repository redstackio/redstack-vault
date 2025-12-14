---
tags:
  - web-access
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2025-12-14T03:15:30.654Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:30.654Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 225e6d4e-24f2-4707-8119-3b6b9e661347
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Navigate to Merchant Settlements Page

## Summary

This procedure involves accessing the Kartpay merchant settlements page, which serves as the entry point for exploiting the reflected XSS vulnerability in the search parameter.

## Description

In the context of testing or exploiting web vulnerabilities, the first step is to reach the specific endpoint hosting the flawed search functionality. The page at https://merchant.kartpay.com/settlements allows merchants to view settlement data and includes a search field that reflects user input without proper sanitization, making it susceptible to XSS attacks. This step requires only basic web access and positions the attacker to interact with the vulnerable component. Expected outcomes include loading the page and confirming the presence of the search interface, setting the stage for payload injection.

## Requirements

1. Web browser with JavaScript enabled
2. Internet connectivity to access the public-facing URL
3. No authentication required for initial access to the page

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on page accesses to detect automated scanning
- Use web application firewalls (WAFs) to monitor and block suspicious navigation patterns
- Log all accesses to sensitive merchant pages for anomaly detection

## Objectives

1. Establish initial access to the vulnerable web application
2. Verify the availability of the search interface
3. Prepare for subsequent input manipulation steps

## Instructions

### Step 1: Open Web Browser and Access URL

**Context**: Launch a browser session and direct it to the target endpoint to load the settlements page.

Navigate to the URL https://merchant.kartpay.com/settlements in your web browser.

> This action loads the page, displaying settlement records and the search field. If the page requires login, ensure valid credentials are used; however, the vulnerability is in the public or authenticated search reflection.

### Step 2: Confirm Page Elements

**Context**: Inspect the loaded page to ensure the search functionality is present.

Visually confirm the search input field is available for user input.

> Successful loading shows the search box without errors, ready for payload entry.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-access]]
- [[initial-access]]
