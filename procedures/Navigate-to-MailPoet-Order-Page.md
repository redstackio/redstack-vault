---
tags:
  - web
  - access
  - navigation
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
updated_at: '2025-12-14T17:25:23.583Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 178f093b-5c94-424d-ac3a-20c1b4ae461b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-MailPoet-Order-Page

## Summary

This procedure outlines accessing the MailPoet account portal and selecting a subscription plan to load the order creation page, setting the stage for IDOR exploitation in the payment process.

## Description

In the context of exploiting an IDOR in MailPoet's order system, this procedure involves logging into the account dashboard, navigating to subscription plans, and loading a specific order page using a plan ID parameter. It requires an authenticated session and targets the web-based interface at https://account.mailpoet.com/. Successful execution confirms the default EUR pricing, which will be manipulated in subsequent steps. No specialized tools are needed, as actions are performed via standard web browsing.

## Requirements

1. Valid MailPoet user account with login credentials
2. Web browser with JavaScript enabled
3. Internet access to https://account.mailpoet.com/

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account and order page accesses
- Monitor for unusual navigation patterns in user sessions
- Enforce session timeouts to prevent prolonged exploitation windows

## Objectives

1. Establish authenticated access to the order interface
2. Load a target plan's order page with default parameters
3. Verify initial pricing display for baseline comparison

## Instructions

### Step 1: Log In to Account Portal

**Context**: Authenticate to gain access to subscription features.

Navigate to https://account.mailpoet.com/ and enter credentials to log in.

> Upon success, the dashboard loads, allowing navigation to plans.

### Step 2: Select Subscription Plan

**Context**: Choose a plan to generate the order URL.

Click on a subscription plan, using the URL format https://account.mailpoet.com/orders/new?p=214 for plan ID 214.

> The order page loads, displaying plan details.

### Step 3: Observe Default Pricing

**Context**: Note the EUR currency and amount to assess manipulation potential.

Inspect the page for the price display, e.g., 33600€.

> Confirms default settings before alteration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- access
- navigation
