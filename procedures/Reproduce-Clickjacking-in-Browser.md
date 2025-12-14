---
id: proc-reproduce-clickjacking-browser
name: Reproduce-Clickjacking-in-Browser
tags:
  - clickjacking
  - reproduction
  - browser
type: procedure
tools:
  - '[[tools/Browser-Unspecified]]'
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
updated_at: '2025-12-14T17:28:12.780Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Reproduce-Clickjacking-in-Browser

## Summary

This procedure demonstrates the clickjacking exploit by loading the PoC in a browser, framing the target site, and simulating tricked user interactions to perform unauthorized actions on logged-in sessions.

## Description

With the PoC HTML ready, this step involves opening it in a browser while authenticated to exchangemarketplace.com. The iframe loads seamlessly due to the weak header, and overlay clicks deceive the user into actions like inbox access, logout, store browsing, or initiating sales. Impact is high for logged-in users, as it enables stealthy account compromise. Prerequisites: PoC file and active login; outcomes include observed unauthorized behaviors confirming exploit success.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Logged-in session to https://exchangemarketplace.com
3. Local file access to the PoC HTML

## Defense

Defensive measures and detection strategies:

- Browser extensions like NoScript to block iframes
- Server-side logging of unexpected framing attempts
- User training on verifying site authenticity before interaction

## Objectives

1. Load PoC and frame the target
2. Trigger actions via overlay deception
3. Validate impact on sensitive features

## Instructions

### Step 1: Prepare Browser Session

**Context**: Ensure authentication to maximize impact.

Navigate to https://exchangemarketplace.com in the browser and log in with valid credentials. Do not close the tab.

### Step 2: Load PoC File

**Context**: Execute the exploit by rendering the malicious HTML.

Open `clickjacking-poc.html` via File > Open or drag-and-drop into the browser. The iframe should load the target without blocking.

> Interact with the page; clicks on the overlay area will execute framed actions (e.g., click 'Inbox' invisibly). Expected: No frame errors, actions complete silently.

### Step 3: Verify Exploitation

**Context**: Confirm tricked interactions succeed.

Attempt clicks on overlay positions corresponding to site buttons; check for changes like inbox opening or logout in the frame.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Browser-Unspecified]]

## Tags

- [[clickjacking]]
- [[drive-by-compromise]]
