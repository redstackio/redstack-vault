---
id: 123e4567-e89b-12d3-a456-426614174003
name: Configure-Malicious-ZenTao-Integration
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.878Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - gitlab
  - zentao
  - integration
commands: []
platforms:
  - Web
tools:
  - '[[tools/GitLab]]'
  - '[[tools/ZenTao]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Configure-Malicious-ZenTao-Integration

## Summary

This procedure sets up GitLab's ZenTao integration to point to an attacker-controlled malicious server, enabling the delivery of XSS payloads via API responses.

## Description

By configuring the integration with a fake ZenTao URL, GitLab will fetch unvalidated data from the attacker's server when issue details are viewed, injecting HTML and JavaScript. This exploits the lack of URL validation and HTML encoding in the serializer.

## Requirements

1. Existing GitLab project
2. Attacker-controlled server URL (e.g., https://joaxcar.com)
3. Dummy credentials for the integration

## Defense

Defensive measures and detection strategies:

- Validate and whitelist integration URLs
- Implement strict CSP to block javascript: URLs
- Log and review all integration configurations

## Objectives

1. Redirect GitLab API calls to malicious endpoint
2. Enable payload delivery on issue page access
3. Set stage for XSS trigger

## Instructions

### Step 1: Access Integration Settings

**Context**: Navigate to the project's integration configuration.

No command; go to Settings > Integrations > ZenTao > Edit.

> Enter server URL: https://joaxcar.com, leave API empty, add dummy username/password.

### Step 2: Save Configuration

**Context**: Persist the malicious settings.

No command; click 'Save changes'.

> Expected: No validation errors, integration active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GitLab]]
- [[tools/ZenTao]]

## Tags

- [[tools/GitLab]]
- [[tools/ZenTao]]
- [[integration]]
