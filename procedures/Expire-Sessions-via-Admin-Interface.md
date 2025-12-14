---
id: proc-shopify-expire-sessions-001
tags:
  - expiration
  - admin
  - shopify
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:44.628Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Expire-Sessions-via-Admin-Interface

## Summary

This procedure uses the Shopify admin web interface to trigger session expiration for all users, simulating an access revocation attempt.

## Description

As the owner, access the admin site and activate the 'Expire User Sessions' feature, which should invalidate all active sessions but fails for the iOS app due to lack of synchronization. This step targets the web admin's session management endpoint. Requires owner access to the store. Expected result is a success notification, though ineffective for mobile.

## Requirements

1. Owner credentials for Shopify admin.
2. Web browser access to the admin dashboard.
3. Active staff session in another client for testing.

## Defense

Defensive measures and detection strategies:

- Verify session expiration logs include mobile clients.
- Implement API calls to invalidate sessions across all platforms upon admin trigger.

## Objectives

1. Attempt global session revocation via admin.
2. Observe confirmation without actual mobile impact.
3. Highlight synchronization failure.

## Instructions

### Step 1: Navigate to Expiration Feature

**Context**: Locate the session management tool in admin.

Log in as owner (e.g., Dimitris) to the admin site and find the 'Expire User Sessions' option.

### Step 2: Trigger Expiration

**Context**: Execute the revocation action.

Click 'Expire User Sessions' and confirm, noting the success notification that all users are logged out.

**Expected Output**: Notification: "All users are logged out."

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[expiration]]
- [[admin]]
- [[shopify]]
