---
id: proc-gitlab-inject-xss-branch-001
tags:
  - xss
  - injection
  - gitlab
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.933Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Default-Branch-Name

## Summary

This procedure exploits the lack of input sanitization in GitLab's group repository settings to store an XSS payload in the 'Default initial branch name' field, which is later rendered without escaping on project pages using HAML's pre and preserve tags.

## Description

The vulnerability stems from improper handling of user input in group settings, allowing HTML and JavaScript tags to be injected. When a new blank project is created, the branch name is interpolated into setup instructions displayed on the project main page, executing the script in the victim's browser. This enables actions like keylogging or token exfiltration. Prerequisites include Owner access to the group.

## Requirements

1. Logged-in attacker account with Owner role in a GitLab group.
2. Access to group settings via web UI.
3. Knowledge of basic JavaScript payloads for testing (e.g., alert).

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in settings with HTML escaping (e.g., use .html_safe only after validation).
- Implement Content Security Policy (CSP) to block inline scripts.
- Audit logs for changes to default branch names containing suspicious characters like <script>.

## Objectives

1. Store persistent XSS payload in group configuration.
2. Ensure payload executes on project creation without initial repo.
3. Prepare for victim targeting via project invites.

## Instructions

### Step 1: Access Group Repository Settings

**Context**: Navigate to the vulnerable settings page to prepare injection.

No command required; use the UI:

Visit https://gitlab.domain.com/groups/attack_group/-/settings/repository.

> Page loads with expandable sections for repository configurations.

### Step 2: Inject and Save Payload

**Context**: Enter the malicious script as the default branch name, exploiting lack of validation.

No command required; use the UI:

Expand 'Default initial branch name', input `<script>alert(1);</script>`, and click Save changes.

> Settings update successfully; payload is stored and will be displayed unsanitized in HAML templates like `pre` and `preserve` tags on project pages.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
