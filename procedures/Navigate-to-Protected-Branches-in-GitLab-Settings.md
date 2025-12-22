---
id: proc-navigate-gitlab-branches
tags:
  - xss
  - gitlab
  - ui-interaction
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
updated_at: '2025-12-13T23:55:37.949Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Navigate-to-Protected-Branches-in-GitLab-Settings

## Summary

This procedure positions the GitLab interface to the protected branches section within repository settings, loading the UI components necessary to render deployment keys in a dropdown for the subsequent XSS trigger.

## Description

After injecting the payload, the attacker must navigate to the protected branches area on the same settings page. This section includes a dropdown for 'Allowed to push' that lists deployment keys, using jQuery to dynamically insert their titles. No payload execution occurs here, but it sets up the vulnerable rendering path. This step assumes the malicious key is already added and requires no additional privileges beyond project access.

## Requirements

1. Previous completion of deployment key injection.
2. Remain on the /settings/repository page.
3. Standard web browser access.

## Defense

Defensive measures and detection strategies:

- Log and monitor navigation patterns in settings pages for unusual access sequences.
- Use client-side validation to prevent rendering of unsanitized content in dynamic UI elements.
- Implement rate limiting on settings modifications to detect rapid key additions followed by branch interactions.

## Objectives

1. Load the vulnerable dropdown component without alerting defenses.
2. Prepare the interface for payload rendering.
3. Maintain session integrity for execution step.

## Instructions

### Step 1: Expand Protected Branches

**Context**: From the repository settings page, locate and interact with the protected branches link to reveal the form.

Scroll down or click the 'Protected branches' link in the left sidebar or main content area to expand the section.

> Expected output: The form expands, displaying fields for branch rules, including the 'Allowed to push' dropdown. No errors or redirects should occur.

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
- [[ui-interaction]]
