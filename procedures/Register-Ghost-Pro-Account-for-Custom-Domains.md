---
tags:
  - account-creation
  - third-party-service
  - ghost.io
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
  - '[[Email Accounts]]'
updated_at: '2025-12-14T04:51:26.548Z'
sub_techniques: []
id: 5674b5ca-7949-4aa3-aa6d-f7aa2cf0505d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Email Accounts]]'
---
# Register-Ghost-Pro-Account-for-Custom-Domains

## Summary

This procedure involves signing up for a paid Ghost Pro account to access features for custom domain configuration, essential for claiming abandoned subdomains on platforms like Ghost.io in takeover attacks.

## Description

Ghost Pro is a hosted blogging platform that allows custom domains, but this requires a paid subscription. In the context of subdomain takeover, registering enables attackers to create publications and bind them to dangling DNS records. The process targets the ghost.org signup page, requiring payment information, and outcomes include dashboard access for further steps. No technical prerequisites beyond a web browser and payment method.

## Requirements

1. Web browser and internet access
2. Valid email and payment method (credit card for $20/month)
3. Knowledge of the target service (Ghost.io)

## Defense

Defensive measures and detection strategies:

- Organizations should avoid using third-party CNAMEs without ongoing monitoring
- Use service-specific tools to detect and revoke abandoned pointers
- Implement approval workflows for DNS changes

## Objectives

1. Obtain Ghost Pro access for custom DNS features
2. Prepare for publication creation tied to target subdomain
3. Enable SSL provisioning for claimed domains

## Instructions

### Step 1: Access Signup Page

**Context**: Navigate to the Ghost Pro registration to initiate account creation.

No command; use browser to visit https://ghost.org/pricing/ and select the Pro plan ($20/month).

> Fill in email, password, and payment details. Expected: Confirmation email and dashboard login.

### Step 2: Complete Payment and Activation

**Context**: Finalize subscription to unlock custom domain tools.

No command; submit payment via the form.

> Success if account is active and dashboard shows Pro features.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Email Accounts]] Compromise Accounts: Third-party Service

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[third-party-service]]
- [[ghost.io]]
