---
id: 30798fcd-2199-4674-be2a-eefc9e84d00c
name: Add Malicious Markdown Content
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:28.510Z'
updated_at: '2025-12-11T06:10:28.510Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - markdown
  - payload-injection
commands:
  - '[[commands/gitlab-env-info]]'
platforms:
  - Web
tools:
  - '[[tools/Docker]]'
  - '[[tools/Firefox]]'
  - '[[tools/GitLab]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---

# Add Malicious Markdown Content

## Summary

This procedure adds Markdown content to a GitLab wiki page that reconstructs into a javascript: URI, enabling stored XSS.

## Description

The content '[XSS](.alert(1);)' combined with the slug creates a clickable link that executes JavaScript when interacted with.

## Requirements

1. Existing wiki page with malicious slug
2. Edit access to the page

## Defense

Defensive measures and detection strategies:

- Sanitize Markdown links and validate URI schemes
- Content security policy (CSP) to block inline scripts

## Objectives

1. Inject XSS payload via Markdown
2. Store the vulnerability persistently

## Instructions

### Step 1: Fill Forms

**Context**: Enter title, format, and content.

Set Title: 'javascript:', Format: Markdown, Content: '[XSS](.alert(1);)'.

### Step 2: Save Page

**Context**: Commit the changes.

Click 'Create page' button.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/GitLab]]

## Tags

- [[xss]]
- [[markdown]]
- [[payload-injection]]
