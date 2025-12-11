---
tags:
  - gitlab
  - data-access
  - theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Data from Information Repositories]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: cbe4f9d4-dca2-40e7-9b05-8d670f7e7530
created_at: '2025-12-11T03:47:57.054Z'
updated_at: '2025-12-11T03:47:57.054Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1213]]'
---
# Access Stolen Private Issues

## Summary

This procedure involves accessing and viewing the stolen private issues in the imported GitLab project, potentially extracting sensitive information.

## Description

After import, the attacker's project displays issues from other private projects, allowing unauthorized access to data like CI variables or credentials. This can also disrupt original projects by making objects inaccessible.

## Requirements

1. Successfully imported project from prior steps.
2. GitLab access to view the new project's issues page.
3. No additional tools required.

## Defense

Defensive measures and detection strategies:

- Regularly audit project object assignments.
- Implement access logging for sensitive data views.

## Objectives

1. View and exfiltrate stolen private data.
2. Confirm successful exploitation.
3. Identify leaked sensitive information.

## Instructions

### Step 1: Navigate to Issues Page

**Context**: Access the issues section of the imported project.

Go to the issues page in the new GitLab project.

### Step 2: View Stolen Content

**Context**: Examine the displayed issues.

Review the issues, which will include private content from foreign projects created by unauthorized users.

### Step 3: Extract Data

**Context**: Copy or document sensitive information.

Extract any visible sensitive data such as secrets or credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #gitlab
- #data-theft
