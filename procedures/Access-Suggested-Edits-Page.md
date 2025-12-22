---
tags:
  - web-navigation
  - authenticated-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Man in the Browser]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 582131d9-e429-406e-9c8c-67cd611e976e
created_at: '2025-12-13T23:56:20.322Z'
updated_at: '2025-12-13T23:56:20.322Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Man in the Browser]]'
---
# Access Suggested Edits Page

## Summary

This procedure loads the suggested edits page for a specific documentation entry on uber.readme.io using an authenticated session cookie, enabling the insertion of user-submitted content.

## Description

After authentication, accessing the /edit endpoint for the deep-linking page provides the interface for suggesting changes. This step is crucial in attacks involving content injection, as it positions the attacker to submit malicious payloads in a stored XSS scenario.

## Requirements

1. Authenticated connect.sid cookie.
2. Network access to https://uber.readme.io/docs/deep-linking/edit.
3. Web browser for interactive access.

## Defense

Defensive measures and detection strategies:

- Restrict edit access to verified users.
- Log and monitor access to edit endpoints.

## Objectives

1. Reach the edit suggestion interface.
2. Prepare for payload submission.
3. Maintain session integrity.

## Instructions

### Step 1: Navigate to Edit Page

**Context**: Use the authenticated cookie to load the page.

Access https://uber.readme.io/docs/deep-linking/edit in a browser with the cookie set.

> This loads the 'Suggest edits' page for content modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Man in the Browser]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- web-navigation
- authenticated-access
