---
tags:
  - shopify
  - authentication
  - bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Cloud
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 8b13ac23-19bd-4e7c-af3f-61a120537d53
created_at: '2025-12-14T17:32:48.519Z'
updated_at: '2025-12-14T17:32:48.519Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Target-Store-with-Restricted-Permissions

## Summary

This procedure authenticates to the target Shopify store using a staff account with limited permissions, confirming the absence of upload rights to set up the permission bypass scenario.

## Description

Staff accounts in Shopify can have granular permissions; this step uses one without 'Files' upload access to demonstrate how the fileCopy mutation circumvents these controls. Login establishes a session token for API calls, simulating an insider threat or compromised low-priv account.

## Requirements

1. Valid staff credentials for target store (e.g., username: jack_mccracken)
2. Target store URL (e.g., storeA.myshopify.com)
3. Browser or API client for authentication

## Defense

Defensive measures and detection strategies:

- Enforce least privilege for staff roles
- Log failed upload attempts post-login
- Multi-factor authentication on staff accounts

## Objectives

1. Obtain authenticated session for API exploitation
2. Verify restricted permissions
3. Prepare for unauthorized file operations

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the target store's admin login.

Open https://storeA.myshopify.com/admin/login in a browser.

> Expected: Login form displayed.

### Step 2: Authenticate as Staff

**Context**: Enter credentials for restricted staff account.

Use username 'jack_mccracken' and password; submit.

> Expected: Redirect to admin dashboard.

### Step 3: Verify Permissions

**Context**: Test upload to confirm restrictions.

Go to Settings > Files and attempt to upload a file.

> Expected: Error denying upload due to permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[authentication]]
