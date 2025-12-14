---
tags:
  - app-installation
  - stripe
  - initial-access
type: procedure
tools:
  - '[[tools/Custom-Links-App]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: a5dbe6c0-443d-488e-8d01-7a8dc2f2af0a
created_at: '2025-12-13T23:56:03.590Z'
updated_at: '2025-12-13T23:56:03.590Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Custom-Links-App

## Summary

This procedure installs the Custom Links app from the Stripe marketplace, enabling the creation of custom hyperlinks in products for potential payload injection in XSS attacks.

## Description

In the context of testing for stored XSS in Stripe, installing third-party apps like Custom Links provides functionality to add user-controlled URLs to dashboard elements. The app integrates directly into the products section, allowing links to be created and shared within an organization. Prerequisites include a Stripe account with app installation permissions. Expected outcome is seamless integration without authentication hurdles, setting up for link creation.

## Requirements

1. Valid Stripe dashboard access with app installation privileges
2. Browser access to https://dashboard.stripe.com
3. No additional tools beyond the web interface

## Defense

Defensive measures and detection strategies:

- Restrict app installations to admin roles via Stripe organization settings
- Monitor app marketplace activity for unusual installations
- Implement app review processes before enabling third-party integrations

## Objectives

1. Enable custom link creation in Stripe products
2. Prepare environment for injecting malicious payloads
3. Assess app integration security without triggering alerts

## Instructions

### Step 1: Navigate to Marketplace

**Context**: Access the Stripe app marketplace to locate and install the Custom Links app.

No command required; use the browser to visit https://marketplace.stripe.com/apps/custom-links and click the install button.

> Follow on-screen prompts to authorize and install the app into your Stripe account.

### Step 2: Confirm Installation

**Context**: Verify the app is active in the dashboard.

No command required; return to https://dashboard.stripe.com/products and check for the custom links option.

> Successful installation shows the app icon and new link creation UI in products.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-Links-App]]

## Tags

- [[app-installation]]
- [[stripe]]
- [[initial-access]]
