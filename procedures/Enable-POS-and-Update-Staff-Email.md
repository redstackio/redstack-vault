---
id: 414cb390-e234-45ec-b42f-5ce1b7e9571e
name: Enable POS and Update Staff Email
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:40.642Z'
updated_at: '2025-12-11T06:10:40.642Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Modify Authentication Process]]'
sub_techniques: []
tags:
  - shopify
  - pos-update
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
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1556]]'
---

# Enable POS and Update Staff Email

## Summary

This procedure enables Point of Sale (POS) in a Shopify store and updates staff emails via a modified CURL request, bypassing verification to target a victim's email.

## Description

After setting up a development store, the attacker enables POS and uses browser tools to capture and alter requests to the POS staff endpoint, allowing unauthorized email updates. This exploits the GraphQL proxy in Shopify's web environment, facilitating account merging.

## Requirements

1. Development store created and email validated
2. Access to shop admin interface
3. Browser with dev tools for CURL capture

## Defense

Defensive measures and detection strategies:

- Require email confirmation for staff updates
- Log and alert on modified requests to POS endpoints

## Objectives

1. Activate POS functionality
2. Update staff to victim's email without verification
3. Set stage for account merge

## Instructions

### Step 1: Enable POS

**Context**: Add POS to the shop's sales channels.

Enable Point of Sale (POS) in the shop's admin interface.

> This unlocks the staff management page.

### Step 2: Access Staff Page

**Context**: Navigate to the POS staff section.

Navigate to POS > Staff in the shop admin.

> Load the page for request capture.

### Step 3: Modify and Send CURL Request

**Context**: Capture, modify, and send request to update email.

Use [[tools/Browser-Dev-Tools]] to inspect and copy the CURL request from the staff page. Replace the email field with the victim's email and send the modified request to https://pos-channel.shopifycloud.com/graphql-proxy/admin.

> This updates the staff email without requiring confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Modify Authentication Process]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Browser-Dev-Tools]]

## Tags

- shopify
- pos-update
