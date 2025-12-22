---
tags:
  - shopify
  - app-creation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: f9524725-0723-44f9-95cc-8870697ec1ca
created_at: '2025-12-13T23:55:20.848Z'
updated_at: '2025-12-13T23:55:20.848Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-New-Application-in-Partners-Dashboard

## Summary

This procedure outlines the creation of a new sales channel application within the Shopify Partners dashboard, serving as the initial setup for exploiting the SVG icon upload vulnerability.

## Description

In the context of the stored XSS attack on Shopify, creating a new application provides the foundation for uploading malicious SVGs. The target environment is the web-based Partners dashboard, requiring authenticated access. Successful execution positions the attacker to convert the app and introduce the payload, ultimately leading to XSS on partner and admin domains.

## Requirements

1. Valid Shopify partner account credentials
2. Web browser access to https://partners.shopify.com/
3. Basic familiarity with Shopify's app management interface

## Defense

Defensive measures and detection strategies:

- Monitor partner dashboard for unusual app creation patterns
- Implement rate limiting on app registrations
- Log and review new app metadata for anomalies

## Objectives

1. Establish a controllable application for payload delivery
2. Gain access to the sales channel configuration features
3. Prepare for subsequent SVG upload without triggering alerts

## Instructions

### Step 1: Log In and Navigate to App Creation

**Context**: Authenticate and access the section for building new applications to initiate the process.

No specific command; use the browser to navigate to https://partners.shopify.com/ and select "Create app" from the dashboard menu.

> Upon login, the dashboard loads; clicking "Create app" opens the creation wizard. Expected output: Form fields for app name, description, and type appear.

### Step 2: Configure Basic App Details

**Context**: Fill in required details to complete app registration without enabling sales channel yet.

No specific command; enter app name (e.g., "Test Sales Channel"), description, and save the initial setup.

> Submission creates the app entry. Expected output: App listed in the dashboard with editable settings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[app-creation]]
