---
tags:
  - shopify
  - deactivation
  - web-admin
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
updated_at: '2025-12-14T17:24:44.991Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2f18c981-dc06-433d-b014-4c4bdc41eab2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-as-Store-Owner-and-Deactivate-Staff

## Summary

This procedure outlines logging into the Shopify web admin as the store owner to deactivate a staff account, which is a prerequisite for exploiting the authentication bypass in the mobile app. It simulates legitimate administrative actions that inadvertently expose the desynchronization vulnerability.

## Description

In a Shopify environment, store owners manage staff permissions through the web-based admin panel. Deactivating a staff account should revoke all access, but due to a failure in status synchronization, the mobile app does not enforce this change. This procedure requires owner credentials and targets stores with existing staff accounts. Expected outcomes include the account appearing deactivated in the web interface, setting the stage for bypass testing.

## Requirements

1. Valid Shopify store owner credentials (email and password)
2. Access to a web browser with internet connectivity
3. A target Shopify store with at least one active staff account

## Defense

Defensive measures and detection strategies:

- Implement real-time synchronization between web and mobile authentication services
- Monitor for anomalous logins from deactivated accounts via API logs
- Enforce multi-factor authentication (MFA) on all staff accounts to add an additional layer

## Objectives

1. Authenticate as store owner to gain admin privileges
2. Deactivate a specific staff account to test propagation failures
3. Verify deactivation in web interface without mobile checks

## Instructions

### Step 1: Access Shopify Web Admin

**Context**: Log in to the Shopify admin panel using owner credentials to establish administrative control.

Open a web browser and navigate to the Shopify admin URL (e.g., yourstore.myshopify.com/admin). Enter the owner email and password, then complete any CAPTCHA or 2FA if prompted.

> Successful login redirects to the dashboard, confirming owner access.

### Step 2: Navigate to Staff Management

**Context**: Locate and access the staff accounts section to select the target account.

In the left sidebar, go to Settings > Users and permissions > Staff. Select the target staff account from the list.

> The staff details page loads, showing current permissions and status.

### Step 3: Deactivate the Staff Account

**Context**: Change the account status to deactivated, which should revoke access but does not propagate to the mobile app.

Click the "Deactivate" or "Remove access" button, confirm the action, and save changes.

> A confirmation message appears, and the account status updates to "Deactivated" in the web interface.

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
- [[deactivation]]
- [[web-admin]]
