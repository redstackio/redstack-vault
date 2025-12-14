---
tags:
  - nextcloud
  - permission-revocation
  - access-control
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
  - Nextcloud
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:29:28.245Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 1f6b735f-c72e-44d5-b508-0d73ac72f299
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Revoke-App-Token-Filesystem-Permissions

## Summary

This procedure revokes filesystem access permissions for the previously created app token, simulating a defensive action to test enforcement.

## Description

Nextcloud allows editing app token scopes via the security settings. This step removes the 'Files' permission from the token, which should prevent further filesystem access using that token. However, due to the vulnerability, session-based access remains unaffected. Performed via web UI or API. Expected outcome: Token updated with reduced scopes, direct token use fails for files.

## Requirements

1. Administrative or owner access to the app token
2. Logged-in session in Nextcloud
3. Token identifier from Step 1

## Defense

Defensive measures and detection strategies:

- Automate permission revocation with session invalidation
- Audit token modifications in real-time
- Use least-privilege scoping for all tokens

## Objectives

1. Trigger the access control mechanism
2. Establish conditions for bypass validation
3. Confirm revocation via token inspection

## Instructions

### Step 1: Access Token Management

**Context**: Locate the app token in settings.

Log in to Nextcloud, go to Settings > Security > Devices & sessions, find the "TestApp" token.

### Step 2: Edit Permissions

**Context**: Remove filesystem scope.

Click edit on the token, uncheck or deselect "Files" permissions, and save changes.

**Expected Output**: Token updated, shows no filesystem access.

### Step 3: Verify Revocation

**Context**: Test that token alone no longer works.

Attempt a filesystem API call with the token; it should fail with permission denied.

**Expected Output**: Access denied error.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- nextcloud
- permission-revocation
- access-control
