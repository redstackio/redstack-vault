---
id: p-login-enable-conversations-concrete-cms
tags:
  - authentication
  - concrete-cms
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
updated_at: '2025-12-14T03:16:20.646Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-and-Enable-Conversations-Feature-in-Concrete-CMS

## Summary

This procedure authenticates to a Concrete CMS instance and enables the Conversations feature, a prerequisite for accessing Sitemap functionalities in the attack chain for stored XSS exploitation.

## Description

In the context of exploiting a stored XSS vulnerability in Concrete CMS 8.2.0 RC2, initial access requires logging in with admin or editor credentials and enabling the Conversations add-on via the dashboard. This step ensures the Sitemap feature is available, setting up the environment for payload injection without altering core CMS configurations.

## Requirements

1. Valid admin or page editor credentials for the Concrete CMS instance.
2. Direct HTTP access to the CMS web interface (e.g., via browser).
3. Concrete CMS 8.2.0 RC2 or vulnerable version running on PHP 5.6.30 and Apache 2.4.25.

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for admin logins to prevent unauthorized access.
- Monitor dashboard access logs for unusual feature enablement patterns.

## Objectives

1. Establish authenticated session in Concrete CMS.
2. Enable Conversations feature to unlock Sitemap editing.
3. Prepare environment for subsequent vulnerability exploitation.

## Instructions

### Step 1: Access Admin Login

**Context**: Navigate to the Concrete CMS login page to initiate authentication.

Open a web browser and go to the CMS admin URL (e.g., `https://target.com/login`).

> Enter username and password in the login form and submit.

### Step 2: Navigate to Dashboard and Enable Feature

**Context**: After login, access the system dashboard to manage add-ons.

From the dashboard, locate the 'Add Functionality' or 'Extend' section, search for 'Conversations', and click 'Install' or 'Enable'.

> Confirm the enablement; the feature status should update to active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- concrete-cms
