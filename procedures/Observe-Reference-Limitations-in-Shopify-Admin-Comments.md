---
id: proc-shopify-observe-limits
tags:
  - recon
  - shopify
  - access-control
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:56.813Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Observe-Reference-Limitations-in-Shopify-Admin-Comments

## Summary

This procedure involves accessing the Shopify admin timeline comments and observing the permission-enforced limitations in the reference dropdown, confirming that restricted resources like orders and customers are not accessible via the UI.

## Description

In Shopify's admin interface, staff with limited permissions can access comment sections in permitted areas like product transfers. The # reference feature in the comment editor provides a dropdown of allowable resources based on user permissions. This step verifies the enforcement, setting up for bypass attempts by noting that manual ID crafting is needed to access hidden resources. The target environment is the Shopify admin web application, requiring a logged-in session with partial access rights. Expected outcomes include visual confirmation of restricted dropdown options, highlighting the vulnerability in backend resolution.

## Requirements

1. Valid Shopify staff account with limited permissions (e.g., product access only)
2. Access to Shopify admin dashboard
3. Burp Suite for potential proxy setup (optional for observation)

## Defense

Defensive measures and detection strategies:

- Implement consistent permission checks in both UI and backend reference resolution
- Log reference attempts and monitor for anomalous ID usage in comments
- Use role-based access control (RBAC) auditing to detect permission mismatches

## Objectives

1. Verify UI-level restrictions on resource references
2. Identify permitted vs. restricted resources
3. Prepare for request manipulation by understanding normal behavior

## Instructions

### Step 1: Access Permitted Comment Section

**Context**: Log in and navigate to a permitted area to load the comments interface.

No specific command; use the web interface:

- Log in to https://<store>.myshopify.com/admin
- Go to Products > Transfers > Select any transfer
- Open the timeline comments section and locate the # sign in the editor

> This loads the interface without triggering alerts.

### Step 2: Test Reference Dropdown

**Context**: Interact with the # sign to observe limitations.

No command; UI interaction:

- Click the # sign in the comment body editor
- Search or browse for resources like orders (#O) or customers (#C)

> Expected: Only permitted items (e.g., products #P) appear; restricted ones are absent.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- recon
- shopify
- access-control
