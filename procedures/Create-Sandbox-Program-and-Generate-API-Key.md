---
tags:
  - auth-bypass
  - api-key
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
updated_at: '2025-12-14T17:32:48.312Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: 61056636-4b57-4fc0-aaa5-4eeebc7c550f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Sandbox-Program-and-Generate-API-Key

## Summary

This procedure creates a sandbox program on HackerOne and generates an API key from it, which can be used to bypass account-level bans on report submissions.

## Description

Banned accounts can still access sandbox creation features. Navigate to the HackerOne dashboard, create a new test/sandbox program, and generate an API key scoped to it. This key authenticates API requests without inheriting the ban, allowing unrestricted report submissions. The technical approach leverages the separation between UI bans and API authentication.

## Requirements

1. Banned but active HackerOne account
2. Web browser access to dashboard
3. Permissions to create programs (researcher level)

## Defense

Defensive measures and detection strategies:

- Revoke API keys on user bans
- Scope API keys to ban status
- Monitor sandbox creation by banned users

## Objectives

1. Obtain an API key not affected by ban
2. Enable API-based submissions
3. Expected outcome: Valid API key generated

## Instructions

### Step 1: Create Sandbox Program

**Context**: Use the dashboard to set up a test environment.

**Command** (Manual UI action):

Go to Programs > Create New > Select Sandbox.

> Complete setup. Expected output: Sandbox program created.

### Step 2: Generate API Key

**Context**: Access API settings for the new program.

**Command** (Manual UI action):

In program settings, navigate to API > Generate Key.

> Copy the generated key (format: username:api_token). Expected output: API key displayed for use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- auth-bypass
- api-key
- hackerone
