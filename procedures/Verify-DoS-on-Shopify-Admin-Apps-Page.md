---
tags:
  - shopify
  - dos
  - admin-panel
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/shopify-admin-apps-access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:28:45.013Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: bdba7eb2-2b47-4ad3-822b-9936b5dede6c
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Verify-DoS-on-Shopify-Admin-Apps-Page

## Summary

This procedure verifies the denial of service impact by attempting to access the Shopify admin's installed apps page, which returns a 500 error due to the malformed app installation.

## Description

Post-installation of the malicious app, the target store's /admin/apps endpoint enters a faulty state because of the unresolved redirect. Shop admins cannot view, manage, or remove installed apps, receiving a 500 Internal Server Error. This persists until the app developer deletes the app from the Partner Dashboard. The procedure simulates admin access to confirm the DoS.

## Requirements

1. Admin login to the affected Shopify store
2. Web browser
3. Prior successful installation of the malicious app

## Defense

Defensive measures and detection strategies:

- Add error handling for invalid redirect_uris in app management backend
- Monitor 500 errors on /admin/apps and correlate with recent installations
- Allow admin overrides for app removal in failure cases

## Objectives

1. Access the apps management page as admin
2. Observe the 500 error confirming DoS
3. Demonstrate inability to manage apps

## Instructions

### Step 1: Log In as Shop Admin

**Context**: Authenticate to the target store's admin panel.

**Instructions**: Navigate to https://{store}.myshopify.com/admin and log in with admin credentials.

### Step 2: Attempt to Access Apps Page

**Context**: Trigger the faulty endpoint to verify DoS.

**Command** ([[commands/shopify-admin-apps-access]]):
Visit https://{store}.myshopify.com/admin/apps.

> The page attempts to load but fails with a 500 Internal Server Error. No apps list is displayed, and removal options are inaccessible.

**Expected Output**: HTTP 500 error; error message or blank page preventing app management.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/shopify-admin-apps-access]]

## Tools Used


## Tags

- shopify
- dos
- admin-panel
