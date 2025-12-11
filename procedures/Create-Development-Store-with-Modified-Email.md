---
id: 5e5168b9-f722-444c-9070-67c1faf2ce3e
name: Create Development Store with Modified Email
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:40.644Z'
updated_at: '2025-12-11T06:10:40.644Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - shopify
  - email-modification
commands:
  - '[[commands/update-organization-email]]'
  - '[[commands/update-user-email]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Browser-Console]]'
  - '[[tools/Browser-Dev-Tools]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---

# Create Development Store with Modified Email

## Summary

This procedure involves creating a Shopify development store and modifying its email fields to a controlled non-existing address, bypassing read-only restrictions to set up for further exploitation.

## Description

In this attack scenario, an attacker uses the Shopify partner dashboard to create a development store and alters the email fields using browser tools or interception, enabling validation of a controlled email without standard checks. This targets web-based Shopify environments running Ruby on Rails, leading to potential account merging.

## Requirements

1. Access to Shopify partner dashboard
2. Control over an email address for receiving validation links
3. Browser with developer tools enabled

## Defense

Defensive measures and detection strategies:

- Monitor for unusual email modifications in store creation requests
- Implement server-side validation for read-only fields

## Objectives

1. Create a manipulable development store
2. Set controlled email without verification
3. Prepare for POS enablement

## Instructions

### Step 1: Initiate Store Creation

**Context**: Access the partner dashboard to start creating a development store.

Navigate to https://partners.shopify.com and initiate store creation.

> This sets up the base store for email modification.

### Step 2: Modify Email Fields

**Context**: Alter the read-only email fields to a controlled address.

Execute [[commands/update-organization-email]] in [[tools/Browser-Console]]:

```javascript
window.RailsData.current_organization.business_email = "nonexistingemail@shopify.com";
```

Then execute [[commands/update-user-email]]:

```javascript
window.RailsData.user.email = "nonexistingemail@shopify.com";
```

> These commands update the form data to the attacker's controlled email.

Alternatively, use [[tools/Burp-Suite]] to intercept and modify the HTTP request.

### Step 3: Validate Email

**Context**: Confirm the modified email.

Click the validation link sent to the controlled email address.

> This validates the email without further checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- [[commands/update-organization-email]]
- [[commands/update-user-email]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Browser-Console]]

## Tags

- shopify
- email-modification
