---
tags:
  - shopify
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 42ee0227-4ebe-4120-b5c9-64299a0e66aa
created_at: '2025-12-13T09:01:26.850Z'
updated_at: '2025-12-13T09:01:26.850Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Sign Up for Shopify Free Trial with Controlled Email

## Summary

This procedure involves signing up for a Shopify free trial using an attacker-controlled email address to establish the initial account for further exploitation.

## Description

By creating a new account with a controlled email, the attacker sets the stage for bypassing email confirmation in subsequent steps. This targets the Shopify web platform during the free trial period.

## Requirements

1. Web browser with internet access
2. Attacker-controlled email account
3. No prior Shopify access needed

## Defense

Defensive measures and detection strategies:

- Monitor for unusual signup patterns from the same IP
- Implement CAPTCHA on signup forms

## Objectives

1. Create a new Shopify account
2. Gain access to the store dashboard
3. Prepare for email change exploitation

## Instructions

### Step 1: Perform Signup

**Context**: Navigate to the Shopify pricing page and complete the free trial signup.

Visit https://www.shopify.com/pricing and fill in the signup form with a controlled email like attacker@gmail.com.

> This creates the account and grants access to the dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- shopify
- initial-access
