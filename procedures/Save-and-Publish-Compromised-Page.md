---
id: proc-uuid-003
tags:
  - publish
  - cms
  - payload-activation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:03.320Z'
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
# Save-and-Publish-Compromised-Page

## Summary

This procedure finalizes the injection by saving and publishing the page, making the CSRF JavaScript live and executable for visitors.

## Description

After injecting the payload, saving and publishing activates it in Concrete CMS. This step relies on the non-admin's edit permissions and assumes no approval workflow. Target: Any Concrete CMS page. Outcome: Page goes live, script runs on load for authenticated users.

## Requirements

1. Edit access to the page
2. No pending approval required for publish
3. CMS instance configured for direct publishing

## Defense

Defensive measures and detection strategies:

- Require admin approval for page publishes
- Scan published content for malicious scripts
- Implement workflow reviews for edits

## Objectives

1. Persist the malicious header content
2. Make page accessible to admins
3. Activate payload without detection

## Instructions

### Step 1: Save Changes

**Context**: Commit the SEO header modifications.

**Command** (UI Action):

Click 'Save' in the page editor.

> Changes persisted; no output beyond success message.

### Step 2: Publish Page

**Context**: Set page to live status.

**Command** (UI Action):

Select 'Publish' from page options.

> Page status updates to published; verify by previewing source for script.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[publish]]
- [[cms]]
- [[payload-activation]]
