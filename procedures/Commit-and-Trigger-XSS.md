---
id: proc-uuid-4
name: Commit-and-Trigger-XSS
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.887Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - commit-trigger
  - xss-execution
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Commit-and-Trigger-XSS

## Summary

This procedure finalizes the payload by committing it to the repository and triggers the XSS by clicking the rendered link, demonstrating arbitrary JavaScript execution in the viewer's browser.

## Description

After injection, committing via GitLab's interface makes the payload persistent. Viewing the project README renders the RDoc, creating the executable link. Clicking it executes the JavaScript in the context of the GitLab domain, allowing attacks like cookie theft. Similar issues exist in other formats, but RDoc is exploited here due to its weak link validation.

## Requirements

1. Payload already injected in README.rdoc
2. Commit permissions in the project
3. Victim (or self) to view and interact with the page

## Defense

Defensive measures and detection strategies:

- Enforce strict URI scheme validation in markup parsers
- Monitor for JavaScript alerts or errors in browser consoles
- Use web application firewalls to block javascript: URIs

## Objectives

1. Persist the payload in the repository
2. Execute JavaScript upon user interaction
3. Validate impact through alert or data exfiltration

## Instructions

### Step 1: Commit Changes

**Context**: Make the payload live.

In the GitLab editor, add a commit message and click 'Commit changes'.

### Step 2: View Rendered README

**Context**: Trigger rendering.

Navigate to the project overview page where the README is displayed.

### Step 3: Interact with Link

**Context**: Execute the payload.

Click the 'XSS' link in the rendered content to trigger the alert(1) or replace with malicious code.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[trigger]]
- [[Execution]]
