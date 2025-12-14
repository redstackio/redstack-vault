---
id: proc-observe-csrf-001
tags:
  - csrf
  - recon
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
updated_at: '2025-12-14T17:27:22.770Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Observe Notification Marking on Report Access

## Summary

This procedure involves testing HackerOne's report viewing endpoint to confirm that a simple GET request marks associated unread notifications as read without CSRF protection, setting the stage for exploitation.

## Description

In the HackerOne platform, accessing a report URL like `/reports/{id}` via GET automatically triggers the server to mark unread notifications for that report as read. This behavior lacks proper CSRF safeguards, such as requiring a POST method or token validation, making it vulnerable to cross-site requests. The procedure requires an authenticated session and is typically performed during reconnaissance to validate the vulnerability before crafting an exploit payload. Expected outcome is confirmation of the side-effect action on notification state.

## Requirements

1. Authenticated HackerOne account with unread notifications
2. Access to a specific report ID (e.g., 5315)
3. Web browser for manual testing

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens for all state-changing actions, even on GET
- Require POST for sensitive operations like marking notifications
- Monitor for anomalous GET requests to report endpoints from unexpected referers

## Objectives

1. Confirm automatic notification marking on report access
2. Identify absence of CSRF protection
3. Gather report ID for targeted exploitation

## Instructions

### Step 1: Access Report URL

**Context**: Log in to HackerOne and ensure there are unread notifications for a target report.

No command required; manually navigate to `https://hackerone.com/reports/{id}` in the browser.

> The page loads, and the server processes the GET request, marking notifications as read. Verify by checking the notifications panel before and after.

### Step 2: Validate Behavior

**Context**: Confirm the side effect without additional user interaction.

No command; inspect the notifications list post-access.

> Expected: Unread indicators disappear for the report's notifications.

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
