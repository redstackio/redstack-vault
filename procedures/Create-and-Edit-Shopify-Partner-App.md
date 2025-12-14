---
tags:
  - shopify
  - app-creation
  - web-exploit
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
updated_at: '2025-12-13T23:52:33.723Z'
sub_techniques: []
id: 9748308e-3c82-44eb-a06b-31a77c72bb23
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-and-Edit-Shopify-Partner-App

## Summary

This procedure outlines the steps to create a new app in a Shopify partner account and navigate to the vulnerable app submissions edit page, setting the stage for XSS payload injection.

## Description

In the context of exploiting stored XSS in Shopify's app submission fields, an attacker first needs to establish a malicious app within their partner dashboard. This involves logging into the Shopify partner account, creating a new application, and accessing the edit page at https://apps.shopify.com/services/app_submissions/edit#. The page contains unsanitized URL fields that allow storage of JavaScript payloads, which execute during previews. Prerequisites include a valid Shopify partner account; outcomes enable subsequent injection steps leading to code execution for any viewer.

## Requirements

1. Valid Shopify partner account credentials
2. Web browser with access to apps.shopify.com
3. Basic understanding of Shopify's partner dashboard interface

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and URL sanitization in form fields
- Use Content Security Policy (CSP) to restrict JavaScript execution on preview pages
- Monitor for anomalous app creations and preview accesses in partner logs

## Objectives

1. Gain access to the vulnerable edit page
2. Prepare the environment for payload injection
3. Enable preview-based exploitation

## Instructions

### Step 1: Log In and Create App

**Context**: Authenticate and initiate app creation to access submission features.

Log into the Shopify partner dashboard at partners.shopify.com, navigate to the 'Apps' section, and click 'Create app'. Provide basic details like app name and description.

> Expected output: App creation confirmation with an overview page.

### Step 2: Navigate to Edit Page

**Context**: Reach the specific form with vulnerable URL fields.

From the app overview, select 'App submissions' or directly access https://apps.shopify.com/services/app_submissions/edit# for the app.

> Expected output: Edit form loaded, showing DEMO URL and pricing URL fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- shopify
- app-creation
