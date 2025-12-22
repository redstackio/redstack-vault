---
tags:
  - shopify
  - recon
  - authorization
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:18.656Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: bc2da8ee-3991-4dcb-a51c-dc1b0d8a1443
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Shopify-Wholesale-Admin-and-Identify-Targets

## Summary

This procedure logs into the Shopify Plus admin panel using a low-privilege staff account and navigates to the wholesale customers section to identify active (enabled) accounts suitable for targeting, confirming UI restrictions on invite actions.

## Description

In Shopify's wholesale feature, staff with only 'apps and channels' or wholesale permissions can access the admin but are UI-blocked from sending invites to activated customers. This step sets up the attack by verifying access and selecting a victim account ID from the list, where accounts show 'Enabled' status and UI buttons like 'Send invite' are disabled or error out.

## Requirements

1. Valid staff login credentials with limited wholesale permissions
2. Web browser with proxy to Burp Suite for traffic interception
3. Access to Shopify Plus partner sandbox or live store admin

## Defense

Defensive measures and detection strategies:

- Enforce strict role-based access control (RBAC) in Shopify staff permissions
- Log all admin panel navigations and customer views for anomaly detection
- Monitor for unusual access patterns from low-priv accounts to wholesale sections

## Objectives

1. Gain initial access to wholesale admin without triggering alerts
2. Enumerate active customer accounts and extract IDs
3. Confirm UI blocks to validate bypass opportunity

## Instructions

### Step 1: Login to Admin Panel

**Context**: Authenticate as staff to access the wholesale feature.

No specific command; use browser to navigate to https://wholesale.shopifyapps.com/admin and log in with credentials.

> Successful login redirects to dashboard; ensure permissions limit to apps/channels or wholesale.

### Step 2: Navigate to Wholesale Customers

**Context**: Locate and inspect customer list for enabled accounts.

No command; in admin, go to 'Customers' > 'Wholesale customers' section.

> View list; note account IDs (e.g., 5182518) with 'Enabled' status. Attempt UI 'Send invite' to see error like 'Cannot send invite to enabled account'.

### Step 3: Configure Interception

**Context**: Set up Burp Suite to capture future requests.

Use [[tools/Burp-Suite]] to proxy browser traffic.

> Proxy configured; ready for API interception in next procedures.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- shopify
- admin-access
- customer-enum
