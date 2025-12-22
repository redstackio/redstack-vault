---
id: d8c886f7-7586-4319-b5c0-8b5fdf4bc78b
name: Create New Wiki Page with Malicious Slug
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:28.512Z'
updated_at: '2025-12-11T06:10:28.512Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - gitlab
  - wiki
  - xss-setup
commands:
  - '[[commands/gitlab-env-info]]'
platforms:
  - Web
tools:
  - '[[tools/Docker]]'
  - '[[tools/Firefox]]'
  - '[[tools/GitLab]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---

# Create New Wiki Page with Malicious Slug

## Summary

This procedure creates a new GitLab wiki page with a slug designed to enable dangerous URI schemes like javascript: for XSS exploitation.

## Description

By setting the page slug to 'javascript:', it allows hierarchical link reconstruction that bypasses URI validation, setting up for stored XSS.

## Requirements

1. Authenticated GitLab session with wiki edit access
2. Access to wiki new page form

## Defense

Defensive measures and detection strategies:

- Validate and filter wiki slugs for dangerous schemes
- Monitor for anomalous page creations

## Objectives

1. Create page with exploitable slug
2. Bypass URI scheme restrictions

## Instructions

### Step 1: Initiate New Page

**Context**: Start creating a new wiki page.

Click 'New page' button.

### Step 2: Set Slug

**Context**: Enter malicious slug.

Fill 'Page slug' with 'javascript:'.

### Step 3: Create Page

**Context**: Submit the form.

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

- [[tools/GitLab]]
- [[wiki]]
- [[xss-setup]]
