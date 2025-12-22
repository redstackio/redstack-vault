---
id: proc-infogram-access-001
tags:
  - web-access
  - infogram
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:02.901Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Infogram-Report-Editor

## Summary

This procedure outlines logging into Infogram and navigating to the report creation or editing interface, setting the stage for vulnerability exploitation in the Report Designer.

## Description

Infogram's web-based platform allows users to create interactive reports. Accessing the editor requires a standard user account. This step establishes the environment for injecting payloads into report elements like the Overview Table, where sanitization is insufficient, leading to stored DOM XSS. Expected outcome: Editor interface ready for input without authentication bypass needed.

## Requirements

1. Valid Infogram account (free tier works)
2. Web browser with JavaScript enabled
3. Internet connection to https://infogram.com

## Defense

Defensive measures and detection strategies:

- Implement account activity logging to monitor report creation spikes
- Use WAF rules to flag unusual editor access patterns

## Objectives

1. Enter the report editing mode
2. Locate the Overview Table input field
3. Prepare for payload insertion

## Instructions

### Step 1: Log In to Infogram

**Context**: Authenticate to gain access to the dashboard.

Navigate to https://infogram.com and sign in with credentials.

> Successful login redirects to the dashboard.

### Step 2: Navigate to Report Editor

**Context**: Open a new or existing report for editing.

Click 'Create' or edit an existing report, using URL like https://infogram.com/app/#edit/e7b161f1-f708-48e5-bab7-de9887ae202a.

> Editor loads with sections including Overview Table.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-access]]
- [[infogram]]
