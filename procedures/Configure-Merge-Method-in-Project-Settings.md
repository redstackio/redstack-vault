---
tags:
  - configuration
  - merge-method
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:44.374Z'
sub_techniques: []
id: 68d4c508-2af9-4b59-b5fc-776cccce590c
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Merge-Method-in-Project-Settings

## Summary

This procedure adjusts project settings to use merge methods that force rebase prompts, enabling the XSS trigger in the mr_widget_rebase.vue component.

## Description

In GitLab, setting 'Fast-forward merge' or 'Merge commit with semi-linear history' ensures merge requests with conflicts display a rebase widget, where the vulnerable branch name rendering occurs.

## Requirements

1. Project owner or maintainer permissions
2. Access to project settings UI

## Defense

Defensive measures and detection strategies:

- Review merge settings for high-risk projects
- Enable merge request approvals
- Monitor setting changes via audit logs

## Objectives

1. Enable rebase-required MRs
2. Set up conditions for widget display
3. Prepare for XSS injection

## Instructions

### Step 1: Access Settings

**Context**: Modify general merge request options.

**Instructions**: In project > Settings > General > Merge requests section, select 'Fast-forward merge' or 'Merge commit with semi-linear history', then save changes.

> Expected output: Confirmation message; settings updated.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- configuration
- merge-method
