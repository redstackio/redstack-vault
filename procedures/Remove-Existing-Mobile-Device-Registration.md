---
tags:
  - cleanup
  - device-removal
  - api
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:09.566Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 757fee12-e62d-49bd-8d5c-f19d1f4259f3
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Remove-Existing-Mobile-Device-Registration

## Summary

This procedure deletes any prior mobile device registrations for the target account to ensure a clean state before replaying the unauthorized request.

## Description

After capturing the initial registration, removing the device via the admin interface prevents conflicts. This uses Shopify's UI or API to DELETE the entry, targeting the APNS token-based record in the mobile_devices resource.

## Requirements

1. Admin access to device management (pre-revocation)
2. APNS token or device ID from interception

## Defense

Defensive measures and detection strategies:

- Log all device registration/deletion events
- Require approval for device changes in multi-user environments

## Objectives

1. Clear existing registrations
2. Avoid duplicate errors in replay
3. Maintain attack stealth

## Instructions

### Step 1: Navigate to Device Settings

**Context**: Access the management interface.

In Shopify admin, go to 'Settings' > 'Notifications' > 'Mobile' (or equivalent device section).

### Step 2: Delete Device Entry

**Context**: Remove the specific registration.

Locate the device by APNS token or name, and select 'Remove' or 'Delete'. Confirm the action.

**Expected Output**: Device list updated; no active registrations.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence (cleanup to enable persistence via notifications)

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- cleanup
- shopify
- mobile-device
