---
id: proc-access-pullrequest-sso
tags:
  - sso
  - saml
  - access
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
updated_at: '2025-12-14T17:30:58.349Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access PullRequest Using HackerOne Login

## Summary

This procedure uses the unauthorized HackerOne account to authenticate via SSO into the PullRequest organization, exploiting the SAML integration for unauthorized entry.

## Description

Navigate to PullRequest's login and select HackerOne SSO, which federates the session. Target: app.pullrequest.com with SAML. Prerequisites: Active HackerOne session. Outcome: Access to organization resources.

## Requirements

1. Valid HackerOne session
2. SAML-enabled organization (e.g., HackerOne PullRequest)
3. Browser with cookies intact

## Defense

Defensive measures and detection strategies:

- Validate SAML assertions for domain restrictions on IdP side
- Audit SSO logins for unexpected accounts
- Implement just-in-time provisioning with strict domain checks

## Objectives

1. Chain access from HackerOne to PullRequest
2. Gain organization-level privileges
3. Enable data exfiltration

## Instructions

### Step 1: Initiate SSO Login

**Context**: Select HackerOne as the identity provider on PullRequest login.

No command; manual:

Go to https://app.pullrequest.com/login, click 'Sign in with HackerOne', authenticate if prompted.

> Expected: Successful redirect to PullRequest dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- sso
- saml
- access
