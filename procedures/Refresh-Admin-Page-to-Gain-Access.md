---
tags:
  - auth-bypass
  - web
  - privilege-escalation
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
updated_at: '2025-12-14T17:31:19.537Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 264c86ba-f162-40dd-99ef-33c9760716e8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Refresh-Admin-Page-to-Gain-Access

## Summary

This procedure refreshes the admin page after the POST submission to activate the bypassed authentication and gain full access to sensitive functions.

## Description

The vulnerable application fails to properly validate the admin flag set via POST, so a simple page refresh applies the unauthorized session changes, granting access to view and modify sensitive DoD data.

## Requirements

1. Browser session from previous submission
2. Admin page URL (https://███████/█████)
3. No logout or session reset

## Defense

Defensive measures and detection strategies:

- Require re-authentication on privilege changes
- Audit logs for session flag modifications
- Use short session timeouts for admin areas

## Objectives

1. Confirm bypass success
2. Access admin dashboard
3. Enable data exposure and modification

## Instructions

### Step 1: Refresh the Page

**Context**: Reload the admin page to trigger the application to honor the manipulated session.

No specific command; browser action:

Press F5 or Ctrl+R on https://███████/█████.

> The page should reload showing the full admin interface, including menus for sensitive data viewing and editing. If access is denied, verify the POST parameters were correct.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[web]]
- [[privilege-escalation]]
