---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - verification
  - discovery
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:58.368Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
---

# Verify-Public-Comment-Visibility

## Summary

This procedure confirms the success of the bypass by checking if the submitted comment is visible to non-internal participants, validating the privilege escalation.

## Description

After manipulation, refresh the report or switch to a reporter account to inspect the comment section. The comment should appear in the public activity without internal markers, indicating exposure. This step is crucial for assessing impact in a controlled test environment on HackerOne.

## Requirements

1. Access to the target report from multiple accounts (team and reporter)
2. Recently submitted manipulated comment
3. Web browser for viewing

## Defense

Defensive measures and detection strategies:

- Regularly audit comment visibility logs for mismatches between user permissions and post types
- Implement client-side indicators for internal content
- Use automated scans to detect parameter tampering attempts

## Objectives

1. Confirm comment is public
2. Identify visibility to unauthorized users
3. Evaluate information disclosure risk

## Instructions

### Step 1: Refresh Report Page

**Context**: Check the comment in the current session.

No command; reload the report page.

> Expected output: Comment appears in activity feed.

### Step 2: Verify from Reporter Account

**Context**: Log in as a non-team participant to test visibility.

Switch accounts and view the report.

> Expected output: Comment visible without login errors or restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[Discovery]]

---
