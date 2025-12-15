---
id: proc-uuid-2
tags:
  - clickjacking
  - browser
  - testing
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
updated_at: '2025-12-14T17:28:12.657Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Test-Clickjacking-in-Browser

## Summary

This procedure tests the clickjacking PoC by loading the HTML file in a browser while authenticated to the target site, confirming unrestricted iframe embedding and potential for user deception.

## Description

Once the PoC HTML is created, this step involves opening it in a browser to verify that the refer.wordpress.com campaign-settings page loads without frame protections. The test simulates an attack by observing if authenticated content is accessible and overlayable, enabling tricks like unintended account changes. Expected outcomes include full page rendering in the iframe; prerequisites are an active login to the site and a modern browser like Chrome or Firefox.

## Requirements

1. Authenticated browser session to refer.wordpress.com
2. Local HTML PoC file from previous procedure
3. Optional: Local web server for remote-like testing

## Defense

Defensive measures and detection strategies:

- Enable frame-busting JavaScript on pages
- Use browser extensions like NoScript to block suspicious iframes
- Log and alert on cross-origin iframe loads in application logs

## Objectives

1. Confirm vulnerability by successful iframe load
2. Demonstrate overlay potential for action hijacking
3. Gather evidence for vulnerability disclosure

## Instructions

### Step 1: Authenticate to Target

**Context**: Ensure the browser session is logged into the affiliate network to load protected content.

Navigate to https://refer.wordpress.com/affiliate-network/ and log in if needed.

> No command; manual browser action.

### Step 2: Load PoC in Browser

**Context**: Open the HTML file to test embedding.

Double-click `clickjack-poc.html` or use a local server:

```bash
python3 -m http.server 8000
```
Then visit `http://localhost:8000/clickjack-poc.html`.

> The iframe should display the campaign-settings page without errors or blocks.

### Step 3: Verify and Simulate Attack

**Context**: Check for restrictions and test overlay clicks.

Interact with the bait button; confirm clicks propagate to iframe elements. Adjust CSS if needed for alignment.

> Success if page is fully interactive and invisible overlay works.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[clickjacking]]
- [[browser-testing]]
- [[web-vulnerability]]
