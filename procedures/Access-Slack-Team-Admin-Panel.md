---
tags:
  - admin-access
  - slack
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:19.790Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 9bd7d7c4-6af7-4966-a489-c7072edf24b4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Slack-Team-Admin-Panel

## Summary

This procedure outlines how to access the Slack team administration panel to modify workspace settings, such as the team name, requiring admin privileges.

## Description

In a Slack workspace, administrators can access the /admin/name endpoint to edit the team name. This step is the entry point for exploiting vulnerabilities in input handling. The target environment is a web-based Slack instance, and success enables payload injection. Prerequisites include valid admin credentials; outcomes include reaching the editable team name field.

## Requirements

1. Admin-level credentials for the Slack workspace
2. Web browser with network access to the Slack domain
3. No additional tools required

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) to limit admin panel access
- Monitor admin actions via audit logs for unusual name changes

## Objectives

1. Reach the team name modification interface
2. Verify edit permissions
3. Prepare for payload injection

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to the Slack workspace and direct to the admin panel to access the team name settings.

No specific command; use browser navigation:

Open `https://hunter22.slack.com/admin/name` (replace `hunter22` with your workspace subdomain).

> Ensure you are logged in as an admin; the page should load the current team name in an editable form.

### Step 2: Verify Access

**Context**: Confirm the form is editable to proceed.

Inspect the page source or interact with the input field to ensure no restrictions.

> Expected: Input field accepts text input without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[admin-access]]
- [[slack]]
