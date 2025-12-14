---
tags:
  - csrf
  - shopify
  - paypal
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.904Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 23327ab2-20a6-4f6e-a5e0-0c50d5ab14da
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Disconnect-Existing-PayPal-Account

## Summary

This procedure clears any prior PayPal integration in a Shopify store, ensuring the CSRF exploit can proceed without conflicts from existing connections.

## Description

In the context of exploiting CSRF in Shopify's PayPal activation, disconnecting an existing account resets the payment provider state. This step requires victim admin access and targets the Shopify admin panel's payments settings. The outcome is a clean slate for token extraction and forged activation.

## Requirements

1. Valid admin login to the target Shopify store
2. Web browser with session cookies intact
3. Knowledge of the store's subdomain (e.g., YOURDOMAIN.myshopify.com)

## Defense

Defensive measures and detection strategies:

- Enable multi-factor authentication (MFA) on admin accounts to prevent unauthorized logins
- Monitor admin panel access logs for unusual payment setting changes
- Use Shopify's activity logs to alert on payment provider modifications

## Objectives

1. Remove any active PayPal connection to avoid activation errors
2. Prepare the store for the merchantId extraction phase
3. Ensure the CSRF URL can successfully trigger activation

## Instructions

### Step 1: Access Payments Settings

**Context**: Navigate to the Shopify admin payments configuration to check and disconnect PayPal.

Log in to the admin panel and visit the payments settings page.

No command required; use browser navigation:

Visit `https://YOURDOMAIN.myshopify.com/admin/settings/payments`.

> Locate the PayPal section and verify if it's connected.

### Step 2: Disconnect PayPal Integration

**Context**: If PayPal is active, initiate disconnection to reset the integration.

Click the 'Disconnect' or 'Manage' button in the PayPal provider section and confirm the action.

> Expected confirmation message: "PayPal has been disconnected from your store."

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[shopify]]
- [[paypal]]
