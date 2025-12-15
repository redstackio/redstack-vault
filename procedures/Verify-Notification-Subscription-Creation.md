---
tags:
  - shopify
  - verification
  - admin-settings
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Additional Cloud Credentials]]'
updated_at: '2025-12-14T17:29:28.987Z'
sub_techniques: []
id: e4f4b3ac-7b9d-4748-a00e-6ee803fc7a4c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Additional Cloud Credentials]]'
---
# Verify Notification Subscription Creation

## Summary

This procedure verifies the success of the unauthorized GraphQL mutation by inspecting Shopify admin notification settings, confirming the addition of the email recipient despite low-privilege execution.

## Description

After executing the mutation, the backend effect persists, allowing verification in the admin interface. This step requires admin-level access to view settings and demonstrates the vulnerability's impact on confidentiality and integrity. The target is the '/admin/settings/notifications' page.

## Requirements

1. Admin access to the Shopify store settings
2. Web browser to navigate admin pages
3. Knowledge of the added email for confirmation

## Defense

Defensive measures and detection strategies:

- Regularly audit notification recipient lists for unauthorized additions
- Implement change logging for settings modifications
- Restrict settings views to verified roles with anomaly detection

## Objectives

1. Confirm backend execution of the mutation
2. Observe unauthorized email in notifications
3. Validate potential for order data disclosure

## Instructions

### Step 1: Access Admin Settings

**Context**: Log in as an admin and navigate to notification settings.

Visit https://yoursubdomain.myshopify.com/admin/settings/notifications.

> The page loads the order notifications section.

### Step 2: Inspect Order Notifications

**Context**: Check the list of email recipients for orders.

Look for the added email (e.g., 'testingforshopify@ngailong.com') in the recipients list.

> Expected output: The email appears, confirming creation despite the access denied response.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Additional Cloud Credentials]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- verification
- admin-settings
