---
id: 123e4567-e89b-12d3-a456-426614174004
name: Trigger-XSS-in-Protected-Branches-Dropdown
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.500Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - gitlab
  - dropdown-trigger
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Trigger-XSS-in-Protected-Branches-Dropdown

## Summary

This procedure navigates to the protected branches settings and interacts with the vulnerable dropdown to render the injected username payload.

## Description

The vulnerability occurs in the 'Ability to Merge' dropdown at https://gitlab.com/group/project/settings/repository, where usernames from project members are loaded via access_dropdown.js without escaping (missing _.escape()). Viewing as a Master user causes the payload to render as HTML, executing JS.

## Requirements

1. Master access to the project
2. Protected branch already configured
3. Browser with JS enabled

## Defense

Defensive measures and detection strategies:

- Apply escaping to all user inputs in JS files
- Patch GitLab to version fixing CVE (if assigned)
- Monitor JS errors or alerts in browser consoles

## Objectives

1. Load the vulnerable UI component
2. Render the malicious username
3. Initiate payload execution

## Instructions

### Step 1: Navigate to Settings

**Context**: Access the repository protected branches page.

Go to Project > Settings > Repository > Protected Branches (URL: https://gitlab.example.com/group/project/-/settings/repository).

### Step 2: Interact with Dropdown

**Context**: Open the role selection to trigger rendering.

Click the dropdown under 'Ability to Merge' or 'Ability to Push'.

> The dropdown fetches and displays member usernames, injecting the payload.

### Step 3: Confirm Rendering

**Context**: Check for unescaped HTML in the dropdown.

Inspect the dropdown options; the malicious username should appear with raw HTML tags.

**Expected Output**: Dropdown shows `<img src=x ...>` in the option text.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[gitlab]]
- [[dropdown-trigger]]
