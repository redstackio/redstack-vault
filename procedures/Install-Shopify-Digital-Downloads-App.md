---
id: proc-uuid-1
tags:
  - shopify
  - app-install
  - setup
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:31.863Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Shopify-Digital-Downloads-App

## Summary

This procedure installs the Digital Downloads App on a Shopify store, enabling the vulnerable file upload functionality for digital attachments.

## Description

In the context of testing the reflected XSS vulnerability, this setup step involves accessing the Shopify App Store and installing the app on a *.myshopify.com store. It requires admin access and serves as the initial access point to the exploit surface. The outcome is the app being ready for product configuration.

## Requirements

1. Valid Shopify account with admin privileges on a *.myshopify.com store
2. Web browser like Firefox for navigation
3. Internet access to the Shopify App Store

## Defense

Defensive measures and detection strategies:

- Review app installations for unauthorized or test apps in store logs
- Implement app review policies to limit installations from untrusted sources

## Objectives

1. Enable digital download features in the store
2. Prepare environment for file upload testing
3. Confirm app accessibility without errors

## Instructions

### Step 1: Access App Store

**Context**: Navigate to the official Shopify App Store to locate the Digital Downloads App.

No command required; use browser to visit https://apps.shopify.com/digital-downloads.

> Click 'Add app' and authorize installation on your store.

### Step 2: Authorize and Install

**Context**: Complete the installation process by granting necessary permissions.

No command required; follow on-screen prompts to install.

> Successful installation redirects to the store admin with the app listed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[shopify]]
- [[app-install]]
