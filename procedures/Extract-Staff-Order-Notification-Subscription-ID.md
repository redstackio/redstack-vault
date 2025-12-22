---
tags:
  - enumeration
  - shopify
  - graphql-id
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[System Information Discovery]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 6ecbc5d6-50d6-4934-bce7-188d97096ee5
created_at: '2025-12-14T17:29:29.023Z'
updated_at: '2025-12-14T17:29:29.023Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Extract-Staff-Order-Notification-Subscription-ID

## Summary

This procedure retrieves the global ID (GID) of a staff order notification subscription from Shopify's admin settings, enabling its use in unauthorized GraphQL mutations.

## Description

To exploit the authorization flaw, the subscription ID must be obtained from the notifications settings page. This involves navigating the admin interface, potentially creating a test notification, and extracting the numeric ID from the URL. The target is the Shopify web admin, requiring admin or settings access. Outcome is a formatted GID ready for API deletion.

## Requirements

1. Access to Shopify admin with 'Settings' or higher permission
2. Web browser to inspect URLs
3. Existing or creatable staff order notification

## Defense

Defensive measures and detection strategies:

- Log access to sensitive settings pages
- Obfuscate or protect ID exposure in URLs
- Rate-limit notification creation and viewing

## Objectives

1. Locate and copy the subscription ID
2. Format it correctly for GraphQL
3. Avoid detection during enumeration

## Instructions

### Step 1: Navigate to Notifications Settings

**Context**: Access the page containing staff order notifications.

**Command** (Browser Navigation):

Go to https://yoursubdomain.myshopify.com/admin/settings/notifications.

> Scroll to the 'Staff order notifications' section.

### Step 2: Create or View Subscription and Extract ID

**Context**: Add a notification if needed, then capture the ID from the URL.

**Command** (URL Inspection):

Click to add/edit a staff notification; note the URL parameter (e.g., /staff_order_notifications/82867191864).

> Copy the number (e.g., 82867191864) and format as gid://shopify/StaffOrderNotificationSubscription/82867191864.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- enumeration
- id-extraction
