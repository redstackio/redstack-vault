---
id: proc-uuid-3
tags:
  - csrf
  - web
  - token-manipulation
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
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
updated_at: '2025-12-14T17:27:15.693Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Replace CSRF Token in New Session

## Summary

This procedure uses browser developer tools to overwrite the newly generated CSRF crumb token in the account settings form with the old token from the previous session, preparing for bypass.

## Description

Exploiting the flaw where tokens do not expire on logout, this step manipulates the DOM in the new session to reuse the old token. This tricks the server into accepting requests as valid. Manual editing via inspector on the web platform; requires dev tools access.

## Requirements

1. New session with settings page loaded
2. Copied old crumb token
3. Browser with dev tools

## Defense

Defensive measures and detection strategies:

- Bind tokens strictly to session IDs and regenerate on login
- Detect DOM manipulations via client-side integrity checks
- Server-side validation of token freshness

## Objectives

1. Modify form token value
2. Maintain page integrity
3. Enable reuse for submission

## Instructions

### Step 1: Inspect New Form

**Context**: Locate the crumb field.

Load settings page, right-click form > Inspect.

> Find <input name="crumb" value="newvalue">.

### Step 2: Edit Token Value

**Context**: Replace with old token.

Double-click value attribute, paste old token, press Enter.

> Value updated to old token.

### Step 3: Verify Edit

**Context**: Ensure no breakage.

Interact with page; form should remain submittable.

> No JavaScript errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[csrf]]
- [[web]]
- [[token-manipulation]]
