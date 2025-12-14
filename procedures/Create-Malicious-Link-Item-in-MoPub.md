---
id: proc-mopub-create-link-item-001
tags:
  - xss
  - web
  - setup
type: procedure
tools: []
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
updated_at: '2025-12-14T03:46:37.933Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Malicious-Link-Item-in-MoPub

## Summary

This procedure sets up a link item in the MoPub platform's line items section, preparing the environment for injecting an XSS payload into the click URL field. It is the initial step in exploiting the lack of input validation in ad configuration features.

## Description

In the MoPub advertising platform at app.mopub.com, authenticated users can create line items associated with ad units. These line items support link types (text or tile) that include a click URL field vulnerable to XSS. This procedure navigates to the relevant dashboard section and creates a basic link item, which serves as the vector for subsequent payload injection. The target environment requires advertiser-level access, and the outcome is a configurable item ready for malicious URL setup. Prerequisites include valid credentials and no additional tools beyond a standard browser.

## Requirements

1. Authenticated session to https://app.mopub.com with permissions to manage line items
2. Access to the /advertise/line_items/ endpoint
3. Basic knowledge of MoPub's ad management interface

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit line item creation to trusted users
- Monitor for unusual ad configurations via logging of click URL inputs
- Use Content Security Policy (CSP) to restrict javascript: protocol execution in ad previews

## Objectives

1. Establish a link item as the XSS vector
2. Prepare for payload injection without triggering alerts
3. Ensure the item can be associated with ad units for testing

## Instructions

### Step 1: Navigate to Line Items Section

**Context**: Access the MoPub dashboard to reach the line items management area.

Log in to https://app.mopub.com and directly navigate to https://app.mopub.com/advertise/line_items/.

> This loads the interface for creating or editing line items. Expected output: Dashboard with options to add new items.

### Step 2: Create a New Link Item

**Context**: Select and configure a link-type item to host the future payload.

Click to create a new line item, choose 'Link' type (text or tile), provide basic details like name and description, but leave the click URL blank for now. Save the item.

> Successful creation returns the item in the list. No commands executed; this is UI-driven.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[setup]]
