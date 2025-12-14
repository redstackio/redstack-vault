---
tags:
  - gitlab
  - integrations
  - configuration
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
updated_at: '2025-12-14T04:39:10.159Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d17b8f64-14fe-40a2-8f36-ef559e865946
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-GitLab-Project-Integrations

## Summary

This procedure details accessing the webhook integration settings within a GitLab project to prepare for SSRF payload entry.

## Description

Once a project is created, the attacker navigates to the settings/integrations section. This page hosts the webhook configuration where arbitrary URLs, including localhost addresses, can be entered without validation, enabling SSRF exploitation for internal scanning.

## Requirements

1. Existing GitLab project
2. Authenticated session
3. Web browser

## Defense

Defensive measures and detection strategies:

- Validate and log all integration URL submissions
- Restrict integration configurations to verified projects
- Alert on rapid or anomalous settings changes

## Objectives

1. Reach the integrations configuration page
2. Identify the webhook URL input field
3. Set up for payload testing

## Instructions

### Step 1: Access Project Settings

**Context**: From the project dashboard, enter the settings area.

Click on 'Settings' in the left sidebar.

> Settings menu expands with options including integrations.

### Step 2: Select Integrations

**Context**: Load the specific integrations tab.

Navigate to 'Integrations' under settings.

> Page loads at https://gitlab.com/{username}/{project}/settings/integrations, showing webhook options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[integrations]]
- [[configuration]]
