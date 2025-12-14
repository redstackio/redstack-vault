---
tags:
  - oauth-login
  - session-creation
  - weblate
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
updated_at: '2025-12-14T17:31:10.919Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 5ad004d9-1844-4f46-a2d5-5e4be3b2d0f8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Establish-Session-via-Third-Party-Login-on-Separate-Device

## Summary

This procedure creates an active session on a secondary device using third-party OAuth credentials, isolating it for later validation of persistence after deauthorization.

## Description

Targeting Weblate's login endpoint, this step leverages the linked Google OAuth to authenticate and establish a session cookie on a separate device. It requires prior linkage and simulates multi-device access scenarios common in real-world usage. The outcome is a fully functional session without using primary credentials, highlighting reliance on external auth.

## Requirements

1. Third-party provider (Google) already linked to the Weblate account
2. Separate device or browser instance to avoid session conflicts
3. Valid Google credentials for the linked account
4. Uninterrupted network access to the platform

## Defense

Defensive measures and detection strategies:

- Log all OAuth login attempts with IP and device fingerprinting
- Enforce session binding to specific devices or user agents
- Alert on logins from new devices post-linkage

## Objectives

1. Create an isolated session using alternative auth
2. Simulate legitimate multi-device usage
3. Prepare for testing session revocation mechanisms

## Instructions

### Step 1: Initiate Login on Secondary Device

**Context**: Start the authentication process using the third-party provider.

Open a browser on the second device and navigate to https://hosted.weblate.org, selecting the Google login option.

> Enter Google credentials when prompted to proceed with OAuth.

### Step 2: Confirm Session Establishment

**Context**: Verify successful authentication and session activation.

Upon redirection, access the dashboard and check browser developer tools for active session indicators like cookies.

> Ensure no further credential prompts and full account functionality is available.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth-login]]
- [[session-creation]]
