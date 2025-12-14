---
tags:
  - verification
  - impact-assessment
  - web-check
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:28.826Z'
sub_techniques: []
id: 5e459154-c915-4978-a472-05bdc000fe03
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Verify Zomato Review Modification

## Summary

This procedure confirms the success of the privilege escalation exploit by checking the target review page for the injected modifications, validating unauthorized data tampering.

## Description

After exploiting the endpoint, this step involves accessing the public review URL to observe changes. It targets Zomato's review display system, where edits propagate immediately. Prerequisites are the known review URL (e.g., https://www.zomato.com/review/QvneAY); outcomes confirm the attack's impact, such as altered content visible to all users.

## Requirements

1. Browser access to Zomato.com
2. Known review URL from exploitation (e.g., /review/QvneAY)
3. No special privileges needed for verification

## Defense

Defensive measures and detection strategies:

- Implement content versioning and audit logs for review changes
- Monitor for rapid or anomalous edits from non-owner accounts
- Use client-side validation to flag unexpected content shifts

## Objectives

1. Observe the modified review content
2. Confirm privilege escalation impact
3. Assess potential for further exploitation

## Instructions

### Step 1: Access Review Page

**Context**: Navigate to the target review URL to inspect the content.

No command; open https://www.zomato.com/review/QvneAY in a browser.

> Look for the updated text 'Privilege Escalation' in the review body.

### Step 2: Validate Changes

**Context**: Compare pre- and post-exploit states to ensure the modification persisted.

Refresh the page or check timestamps; success if the injected content is displayed without errors.

> Expected output: Visible review edit matching the POST payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[impact-validation]]
