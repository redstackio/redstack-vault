---
tags:
  - api-token
  - hackerone
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
updated_at: '2025-12-14T17:32:48.476Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: dc6d6aa4-c741-4044-95f6-c8222d3be1ac
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Generate-HackerOne-API-Token

## Summary

This procedure describes generating an API token for a HackerOne user account, which will be used to demonstrate persistent access after account banning.

## Description

Once logged into the HackerOne account, navigate to the API token generation section in user settings. The token serves as a long-lived credential for API authentication. In this vulnerability scenario, the token is created before banning to show it remains valid post-deletion. Prerequisites include an active account from the previous procedure.

## Requirements

1. Active HackerOne user account
2. Web browser access to account settings
3. Understanding of API authentication basics

## Defense

Defensive measures and detection strategies:

- Revoke API tokens upon account suspension or banning
- Implement token expiration policies
- Log token generation events for auditing

## Objectives

1. Create a valid API token for the test account
2. Store the token securely for later use
3. Prepare for testing token validity after ban

## Instructions

### Step 1: Access API Settings

**Context**: Log in to HackerOne and go to user profile settings to find the API token section.

No command; use web interface at https://hackerone.com/settings/tokens.

> Select 'Generate New Token' and confirm scopes (full access for testing).

### Step 2: Retrieve and Note Token

**Context**: Copy the generated token for use in API calls.

The token will appear as a base64-like string, e.g., 'XXXXXXXXXXXXXXXXXXXX=' associated with username 'mrtst'.

> Verify by making a test API call if possible, but save for post-ban testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- api-token
- hackerone
