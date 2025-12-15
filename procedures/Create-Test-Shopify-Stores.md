---
id: proc-create-stores-001
tags:
  - setup
  - shopify
  - test-environment
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
updated_at: '2025-12-14T17:25:23.737Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Test-Shopify-Stores

## Summary

This procedure sets up two separate Shopify test stores to simulate an attacker and victim environment for testing IDOR vulnerabilities in integrated apps like Stocky.

## Description

In the context of exploiting web application vulnerabilities such as IDOR, creating isolated test stores on Shopify allows for controlled demonstration without affecting production data. Each store has a unique domain (e.g., test.myshopify.com and test1.myshopify.com), enabling separate authentication and app installations. This step is foundational for multi-tenant app testing where authorization relies on numeric IDs.

## Requirements

1. Shopify developer account access
2. Email addresses for two separate user sign-ups
3. Basic web browser for admin panel navigation

## Defense

Defensive measures and detection strategies:

- Monitor for unusual store creation patterns from single IP
- Implement rate limiting on developer account sign-ups

## Objectives

1. Establish attacker-controlled store (User A)
2. Establish victim-simulated store (User B)
3. Ensure isolation for safe testing

## Instructions

### Step 1: Sign Up for Shopify Accounts

**Context**: Create two distinct user accounts to avoid session crossover.

No specific command; use web interface:

Browse to shopify.com, sign up with email1@example.com for User A, creating test.myshopify.com. Repeat with email2@example.com for User B, creating test1.myshopify.com.

> Expected output: Confirmation emails and access to respective admin dashboards.

### Step 2: Verify Store Activation

**Context**: Confirm stores are active and ready for app installation.

Log in to each admin panel and ensure the dashboard loads without errors.

> Expected output: Functional store admin interfaces.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[shopify]]
