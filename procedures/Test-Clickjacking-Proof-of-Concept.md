---
id: proc-test-clickjacking-poc-001
tags:
  - clickjacking
  - testing
  - web
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:12.199Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Clickjacking Proof-of-Concept

## Summary

This procedure tests the clickjacking PoC by loading the HTML in a browser, simulating user deception, and capturing evidence to validate the vulnerability's exploitability for harvesting user data from the Legal Robot form.

## Description

Testing involves loading the PoC locally or on a server, observing the semi-transparent iframe, and clicking overlays to trigger hidden form interactions. The attack scenario deceives users into submitting name, email, and company info unknowingly. Due to AWS S3 and CloudFlare setup, no framing blocks occur. Expected outcomes: Visual proof via screenshots of deceptive UI.

## Requirements

1. Web browser
2. The created PoC HTML file
3. Screenshot tool

## Defense

Defensive measures and detection strategies:

- Browser extensions to detect iframes (e.g., NoScript)
- Server-side logging of unusual referral patterns
- User training on phishing indicators

## Objectives

1. Verify iframe embedding works
2. Demonstrate overlay deception
3. Capture evidence of potential data submission

## Instructions

### Step 1: Load PoC in Browser

**Context**: Open the HTML to display the framed site.

Double-click clickjacking-poc.html or serve it via a local server (e.g., python -m http.server) and access via http://localhost:8000.

### Step 2: Simulate User Interaction

**Context**: Test clicks on overlays to ensure they affect the hidden form.

Observe the partial opacity (0.5) of the Legal Robot site. Click the overlay button, which should submit or interact with the form elements underneath. Monitor the target site for any submission indicators.

> Expected: Clicks translate to form actions without direct visibility.

### Step 3: Capture Evidence

**Context**: Document the test for reporting.

Take screenshots showing the iframe, overlay, and any resulting form behavior. Note that in a real attack, this could harvest data via backend logging on the attacker's site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[poc-testing]]
