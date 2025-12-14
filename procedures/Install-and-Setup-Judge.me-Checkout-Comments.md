---
id: uuid-install-setup
tags:
  - setup
  - shopify
  - judge.me
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:47.330Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Install-and-Setup-Judge.me-Checkout-Comments

## Summary

This procedure installs the Judge.me Checkout Comments addon in a Shopify store to enable the vulnerable comment curation functionality, setting up the environment for IDOR exploitation.

## Description

The Judge.me Checkout Comments addon allows stores to collect and manage buyer comments during checkout. In the context of this attack, installation provides access to the admin interface where comments are curated via API calls lacking proper authorization checks. Prerequisites include a Shopify store admin account. Expected outcomes: addon enabled, ready for test order creation.

## Requirements

1. Active Shopify store admin credentials
2. Internet access to Shopify App Store
3. No prior Judge.me installation conflicts

## Defense

Defensive measures and detection strategies:

- Monitor app installations in Shopify admin logs for unauthorized addons
- Implement rate limiting on app API endpoints

## Objectives

1. Enable vulnerable comment management features
2. Prepare for legitimate request interception
3. Establish baseline for IDOR testing

## Instructions

### Step 1: Access Shopify Admin

**Context**: Log in to initiate app installation.

No specific command; use browser to navigate to your Shopify admin dashboard.

> Successful login grants access to Apps section.

### Step 2: Install Judge.me App

**Context**: Search and install the Checkout Comments addon.

No specific command; in Shopify admin, go to Apps > Search for "Judge.me Checkout Comments" > Click Install.

> App installation completes without errors, visible in installed apps list.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- setup
- shopify
- judge.me

