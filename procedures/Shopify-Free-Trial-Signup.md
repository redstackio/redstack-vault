---
tags:
  - auth-bypass
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
id: 4e1f7a60-a06b-4ad2-a701-58a28496ccf2
created_at: '2025-12-11T06:10:40.592Z'
updated_at: '2025-12-11T06:10:40.592Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Shopify Free Trial Signup

## Summary

This procedure involves signing up for a Shopify free trial using an attacker-controlled email, establishing the foundation for exploiting email confirmation bypass vulnerabilities.

## Description

The signup process creates a new account and store instance, which can then be manipulated to change emails and bypass confirmations. This is targeted at Shopify's web platform and requires no special tools beyond a browser.

## Requirements

1. Attacker-controlled email address
2. Access to Shopify website
3. Internet connection

## Defense

Defensive measures and detection strategies:

- Monitor for unusual signup patterns from single IPs
- Implement CAPTCHA on signup forms

## Objectives

1. Gain initial access to Shopify dashboard
2. Prepare for profile manipulation
3. Establish verifiable email base

## Instructions

### Step 1: Visit Signup Page

**Context**: Navigate to the pricing page to start the free trial.

Visit https://www.shopify.com/pricing and complete the signup process with an email like attacker@gmail.com.

> This creates the account and sends initial emails.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- auth-bypass
- initial-access
