---
id: demo-xss-csrf-2024
tags:
  - xss
  - csrf
  - exploitation
  - demo
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:43.083Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Demonstrate-XSS-Execution-via-CSRF

## Summary

This procedure simulates the full exploitation by having a victim (or tester) load the CSRF HTML page while authenticated on the Acronis site, resulting in the XSS payload execution and demonstration of impacts like cookie theft.

## Description

Once the CSRF page is created, delivering it to an authenticated user (e.g., via email link) causes their browser to submit the form cross-origin, exploiting the lack of CSRF protection. The reflected XSS then executes in the victim's context, allowing arbitrary JS like alerting cookies or exfiltrating data. This demonstrates the chained attack's potential for session hijacking. Prerequisites: Authenticated session on target, hosted CSRF page. Expected outcomes: JS execution confirming vulnerability and impact.

## Requirements

1. Authenticated browser session on www.acronis.com
2. Hosted CSRF HTML page accessible via URL
3. Victim or tester to load the page

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens and validate origin headers
- Sanitize all reflected inputs to prevent XSS
- Implement browser-based protections like X-Frame-Options and monitor for unexpected form submissions

## Objectives

1. Trigger XSS via CSRF in victim context
2. Observe JavaScript execution and data exposure
3. Validate full attack chain impact

## Instructions

### Step 1: Deliver and Load CSRF Page

**Context**: Provide the link to the CSRF HTML to the victim; upon loading, the form auto-submits.

No command; use phishing or direct link: <a href="http://attacker.com/csrf-poc.html">Click here</a>

> Victim clicks or loads the page; browser submits POST to target.

### Step 2: Observe Execution

**Context**: In the victim's browser, the response renders the XSS, executing the payload.

Monitor via dev tools (F12) for confirm dialog or network requests.

> Success: Alert shows document.cookie; potential for further actions like sending data to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[csrf]]
- [[exploitation]]
- [[demo]]
