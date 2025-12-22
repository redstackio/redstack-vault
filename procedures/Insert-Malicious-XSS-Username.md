---
tags:
  - xss
  - stored-xss
  - username-injection
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
updated_at: '2025-12-13T23:55:37.831Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 62fcf95d-7e97-483c-bec3-972f5bf27077
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Insert-Malicious-XSS-Username

## Summary

This procedure involves setting a GitLab username with an embedded JavaScript payload and inserting it into the merge request approval field, exploiting poor sanitization to store the XSS for later execution.

## Description

Targeting GitLab's user profile and project settings, this step creates or modifies a username to include a proof-of-concept XSS payload (e.g., `<script>alert('XSS')</script>`). The payload is then placed in the approval requester field, where it is stored without proper escaping. In a web-based GitLab EE environment, this leads to the payload being rendered in the browser upon selection, enabling arbitrary JS execution for impacts like session hijacking.

## Requirements

1. Permissions to edit usernames or create users
2. Access to project settings approval configuration
3. Knowledge of a valid XSS payload suitable for the context

## Defense

Defensive measures and detection strategies:

- Enforce strict username validation and sanitization on input
- Use Content Security Policy (CSP) to restrict inline script execution
- Audit user profile changes and approval field interactions

## Objectives

1. Store malicious payload in username
2. Position it in the approval interface
3. Ensure payload survives storage without alteration

## Instructions

### Step 1: Create or Edit Username with Payload

**Context**: Embed the XSS script in the username to prepare for storage.

Go to user settings and set username to include `<script>alert('XSS')</script>` or a more advanced payload like `<img src=x onerror=alert(document.cookie)>`.

> Username updates successfully, payload intact.

### Step 2: Insert into Approval Field

**Context**: Place the malicious username in the project settings for rendering.

In the merge request approvals section, paste the username into the requester or approver field, referencing the malicious user.

> Field accepts the input, and dropdown shows the username with embedded payload.

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
- [[stored-xss]]
- [[username-injection]]
- [[gitlab]]
