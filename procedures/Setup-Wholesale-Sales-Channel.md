---
id: proc-uuid-001
name: Setup-Wholesale-Sales-Channel
tags:
  - shopify
  - app-installation
  - initial-access
type: procedure
tools:
  - '[[tools/HTTP-Proxy-Burp-Suite]]'
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:16.213Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Wholesale-Sales-Channel

## Summary

This procedure installs the Shopify Wholesale sales channel app and navigates to its admin interface, establishing the environment for subsequent price list manipulations in an attack targeting stored XSS.

## Description

In the context of exploiting a stored XSS vulnerability in Shopify's Wholesale channel, this initial procedure involves adding the app to a Shopify store and accessing its admin panel. The Wholesale channel allows merchants to manage B2B pricing, but its shared domain enables cross-shop impacts. Prerequisites include valid Shopify admin credentials. Expected outcomes: app integration without errors, ready for price list creation.

## Requirements

1. Valid Shopify admin account with store access
2. Web browser with internet connectivity
3. No proxy interception needed at this stage

## Defense

Defensive measures and detection strategies:

- Monitor app installations for unauthorized additions via Shopify audit logs
- Implement app review policies to restrict third-party channel apps
- Use web application firewalls (WAF) to scan for anomalous admin navigations

## Objectives

1. Gain access to the vulnerable Wholesale interface
2. Prepare for CSV-based price list imports
3. Establish baseline for payload injection

## Instructions

### Step 1: Install the Wholesale App

**Context**: Visit the app store to add the Wholesale integration, enabling the sales channel.

No specific command; perform via browser:

- Navigate to https://wholesale.shopifyapps.com and click 'Add app' or 'Install'.

> Successful installation redirects to the Shopify admin with confirmation.

### Step 2: Access the Admin Panel

**Context**: Enter the Wholesale channel dashboard to confirm setup.

No specific command; perform via browser:

- Go to https://your-store.myshopify.com/admin/apps/wholesale.

> Dashboard loads, showing options for price lists and customers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/HTTP-Proxy-Burp-Suite]]

## Tags

- [[shopify]]
- [[app-installation]]
- [[initial-access]]
