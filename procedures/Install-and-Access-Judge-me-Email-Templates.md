---
tags:
  - shopify
  - judge-me
  - initial-access
type: procedure
tools:
  - '[[tools/Summernote-JS]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3d690f2d-ebe6-4580-a98c-1ef630b4663e
created_at: '2025-12-13T23:55:20.636Z'
updated_at: '2025-12-13T23:55:20.636Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-and-Access-Judge-me-Email-Templates

## Summary

This procedure installs the Judge.me app in a Shopify store and navigates to the vulnerable email templates section, establishing initial access to the exploitation point.

## Description

The Judge.me app, a product review tool for Shopify, integrates directly into the e-commerce platform. Installing it grants access to features like email templates, where the stored XSS vulnerability resides. This step is prerequisite for template manipulation and requires Shopify admin privileges. The target environment is any Shopify store, with the app pulling in the vulnerable Summernote JS library for editing.

## Requirements

1. Valid Shopify admin credentials for the target store
2. Internet access to the Shopify App Store
3. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Restrict app installations to trusted sources via Shopify admin permissions
- Monitor app installations and access logs for unusual activity in the admin dashboard
- Use Shopify's app review processes to vet third-party integrations like Judge.me

## Objectives

1. Install Judge.me to enable access to email templates
2. Navigate to the Requests > Email Templates section
3. Prepare for subsequent payload injection steps

## Instructions

### Step 1: Install Judge.me App

**Context**: Log in to Shopify and add the app to gain feature access.

No command required; use the Shopify interface:

- Go to Shopify Admin > Apps > Search for "Judge.me" > Click "Add app" > Follow installation prompts.

> Expected output: App dashboard appears post-installation.

### Step 2: Navigate to Email Templates

**Context**: Access the vulnerable feature within the app.

No command required; UI navigation:

- In Judge.me dashboard, select Requests > Email Templates.

> Expected output: Templates list or editor loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Summernote-JS]]

## Tags

- [[shopify]]
- [[judge-me]]
- [[initial-access]]
