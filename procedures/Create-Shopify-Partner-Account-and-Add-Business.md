---
tags:
  - setup
  - shopify
  - account-creation
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:44.887Z'
sub_techniques: []
id: edb45130-28b3-418d-9ea5-67d17bb82a16
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Create-Shopify-Partner-Account-and-Add-Business

## Summary

This procedure sets up a Shopify Partner account and associates a business entity, providing the foundation for testing IDOR vulnerabilities in the platform.

## Description

In the context of exploiting IDOR in Shopify's partners.shopify.com, this initial step involves registering a new partner account to gain access to the dashboard. A business is then added to enable store creation and permission testing. This simulates an attacker's preparation phase where legitimate access is obtained to probe for weaknesses. Expected outcomes include a functional dashboard for subsequent steps.

## Requirements

1. Internet access and web browser
2. Valid email for registration
3. No prior Shopify account conflicts

## Defense

Defensive measures and detection strategies:

- Monitor new account registrations for anomalous patterns
- Implement rate limiting on signup endpoints

## Objectives

1. Establish controlled test environment
2. Obtain business ID for URL construction
3. Prepare for permission-based testing

## Instructions

### Step 1: Register Partner Account

**Context**: Create the base account to access the partner dashboard.

Navigate to https://partners.shopify.com/signup and complete the registration form with email, name, and password.

> Upon submission, verify email and log in to access the dashboard.

### Step 2: Add Business Entity

**Context**: Link a business to enable store management features.

In the dashboard, go to the 'Organizations' section and click 'Add business', providing business details like name and address.

> Business ID is generated and displayed for reference in later URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[shopify]]
- [[account-creation]]
