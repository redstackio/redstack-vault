---
tags:
  - csrf
  - web-vulnerability
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
updated_at: '2025-12-14T17:27:30.050Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 6c71578a-6b4b-44de-8b5d-0d57141d2d7d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Open-Starbucks-Lost-Stolen-Page

## Summary

This procedure uses JavaScript to open the Starbucks lost/stolen card management page in a new window, leveraging the victim's authenticated session to access protected functionality without their knowledge.

## Description

By calling window.open() on the vulnerable endpoint https://www.starbucks.com/account/card/loststolen, the procedure prepares the environment for automated form submission. This step exploits the site's lack of CSRF checks, allowing the attack to proceed in the context of the victim's session.

## Requirements

1. Victim's browser with active Starbucks authentication
2. JavaScript execution enabled
3. No popup blockers interfering with window.open

## Defense

Defensive measures and detection strategies:

- Enforce same-site cookies (Lax/Strict) to limit cross-origin requests
- Monitor for unexpected page loads or form submissions in browser dev tools
- Implement referrer checks on sensitive endpoints

## Objectives

1. Load the target page silently
2. Maintain session context for subsequent submissions
3. Avoid user detection

## Instructions

### Step 1: Implement JavaScript Function

**Context**: Add the window.open call to the onload function in the malicious HTML.

Update the script in `csrf-poc.html`:

```javascript
window.open('https://www.starbucks.com/account/card/loststolen');
```

> This opens the page in a new window upon body load.

### Step 2: Test the Open

**Context**: Verify the page opens correctly in an authenticated session.

Load the malicious page while logged into Starbucks and confirm the target loads.

> Expected: New tab/window shows the lost/stolen form.

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
- [[web-vulnerability]]
