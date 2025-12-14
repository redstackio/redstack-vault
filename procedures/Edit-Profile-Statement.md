---
tags:
  - profile-edit
  - markdown-input
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:31.114Z'
sub_techniques: []
id: 4ed4831f-30e1-4777-9174-c803f582e2a2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Edit-Profile-Statement

## Summary

This procedure navigates to the user's profile and opens the statement editing interface, setting up for malicious payload insertion in the Stored XSS attack.

## Description

Once authenticated, this step accesses the profile page to locate and activate the edit mode for the statement field, which accepts Markdown input. The vulnerability stems from poor sanitization in this field, allowing XSS. Expected outcome is an open form ready for payload entry.

## Requirements

1. Active user session on Gratipay
2. Web browser
3. Knowledge of profile URL structure (e.g., https://gratipay.com/~username/)

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in edit forms
- Log and monitor profile edits for suspicious content
- Implement client-side validation for Markdown links

## Objectives

1. Access editable statement field
2. Prepare for XSS payload injection
3. Exploit Markdown rendering flaws

## Instructions

### Step 1: Navigate to Profile

**Context**: Load the personal profile page.

From the dashboard, click on your username or directly visit https://gratipay.com/~username/.

### Step 2: Initiate Edit

**Context**: Open the statement input form.

Locate the 'Edit Statement' option or button on the profile page and click it to reveal the text area.

### Step 3: Confirm Edit Mode

**Context**: Verify the form is ready for input.

Ensure the Markdown-enabled text field is visible and focused.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[profile-edit]]
- [[web]]
