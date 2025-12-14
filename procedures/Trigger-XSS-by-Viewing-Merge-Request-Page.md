---
tags:
  - xss-trigger
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:44.365Z'
sub_techniques: []
id: f2117a61-a538-49b9-bc0e-5cf6e4844277
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Viewing-Merge-Request-Page

## Summary

This procedure simulates a victim accessing the MR page, causing the Stored XSS to execute in the browser via the unsanitized branch name in the rebase widget.

## Description

Users without push access to the source branch view the MR; the Vue component at mr_widget_rebase.vue#L47 inserts the branch name without escaping, firing the onerror JS.

## Requirements

1. MR created with rebase required
2. Victim session (guest/anonymous ok)
3. No developer push permissions

## Defense

Defensive measures and detection strategies:

- Patch GitLab to latest (CVE fixed in 12.5+?)
- Content Security Policy (CSP) to block inline JS
- Browser extensions for XSS detection

## Objectives

1. Execute arbitrary JS in victim context
2. Steal session data/credentials
3. Perform actions as victim

## Instructions

### Step 1: Access MR as Victim

**Context**: Load the page to trigger rendering.

**Instructions**: Log out or use incognito/guest account without push perms, navigate to the MR URL (e.g., /project/-/merge_requests/1).

> Expected output: Alert box with domain; inspect element shows img tag injection. Extend payload for exfil (e.g., fetch to attacker server).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- execution
