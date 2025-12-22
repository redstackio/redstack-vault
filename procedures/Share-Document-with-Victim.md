---
id: proc-share-document-victim
tags:
  - nextcloud
  - sharing
  - social-engineering
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
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.546Z'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Share-Document-with-Victim

## Summary

This procedure shares the created document with a target victim via Nextcloud's sharing functionality, ensuring it appears in their files for collaborative access.

## Description

Nextcloud's sharing feature allows users to send documents to other accounts, either by link or direct user selection. This step delivers the document containing the attacker's malicious username to the victim, who must open it in Collabora to trigger the XSS.

## Requirements

1. Ownership of the document to share
2. Knowledge of the victim's Nextcloud username or email
3. Sharing permissions enabled in Nextcloud

## Defense

Defensive measures and detection strategies:

- Require approval for incoming shares from unknown users
- Monitor share logs for patterns of mass sharing or suspicious links
- Educate users on verifying share sources before opening

## Objectives

1. Deliver the document to the victim's account
2. Prompt the victim to engage in collaborative editing
3. Maintain plausible deniability in the share

## Instructions

### Step 1: Select Document

**Context**: Locate the document in your files.

Go to the Files app and right-click or select the target document.

> Expected: Context menu appears with sharing option.

### Step 2: Initiate Share

**Context**: Configure the share to the victim.

Choose "Share" and enter the victim's username or email; set permissions to view/edit as needed.

> Expected: Share invitation sent; document added to victim's shared items.

### Step 3: Confirm Delivery

**Context**: Verify the victim has access.

Check share status or ask the victim to confirm receipt (if possible).

> Expected: Victim sees the document in their shared files list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[sharing]]
- [[social-engineering]]
