---
id: proc-inject-gitlab-key
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
updated_at: '2025-12-13T23:55:37.953Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Deployment-Key-in-GitLab

## Summary

This procedure involves creating a deployment key in GitLab's project repository settings with a malicious title containing an HTML script tag, exploiting the lack of input sanitization to set up an XSS payload for later execution.

## Description

In GitLab's project settings, the deployment key title field accepts user input without proper HTML escaping. By injecting a script tag like '<script>alert(document.domain)</script>', an attacker with project access can prepare a payload that will be rendered unsafely in subsequent UI elements. This step requires authenticated access to the project and a valid SSH key. The payload remains dormant until triggered, allowing potential for broader impacts like session hijacking or API abuse once executed.

## Requirements

1. Authenticated GitLab account with maintainer or owner permissions on the target project.
2. A valid SSH public key for the deployment key.
3. Access to the web interface at /project/settings/repository.

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and HTML escaping for all user-controlled fields, especially titles rendered in dropdowns.
- Enforce comprehensive CSP policies without relying on 'strict-dynamic' for script execution control; audit jQuery usage for unsafe insertions.
- Monitor for anomalous script executions in browser consoles or unexpected alerts in user reports.

## Objectives

1. Inject arbitrary HTML/script into a persistent project setting.
2. Prepare payload for client-side execution without immediate detection.
3. Enable follow-on exploitation of victim sessions.

## Instructions

### Step 1: Access Repository Settings

**Context**: Navigate to the project settings page to reach the deploy keys management section.

Go to your GitLab project dashboard, then select Settings > Repository from the left sidebar.

### Step 2: Add New Deployment Key

**Context**: Fill the deploy keys form with the malicious payload in the title while providing a legitimate SSH key to avoid validation errors.

In the Deploy keys section, click 'Add new key'. Enter:
- Title: `test <script>alert(document.domain)</script>`
- Key: Paste a valid SSH public key (e.g., generated via `ssh-keygen`).
- Check 'Write access allowed' for broader permissions if needed.

Click 'Add key' to submit.

> This injects the payload into the database without execution at this stage. Expected output: Success message and key listed in the deploy keys table.

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
- [[injection]]
- [[gitlab]]
