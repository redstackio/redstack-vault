---
id: proc-trigger-shopify-xss-dashboard
name: Trigger-Stored-XSS-in-Partners-Dashboard
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.556Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - stored-xss
  - execution
platforms:
  - Web
commands: []
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Trigger-Stored-XSS-in-Partners-Dashboard

## Summary

This procedure triggers the execution of a stored XSS payload by accessing Shopify's partners dashboard pages, where the unsanitized user profile data is reflected and executed in the browser of authenticated users.

## Description

After injecting a payload into the account profile, navigating to partner confirmation or completion pages causes the server to render the user's name without proper output encoding. This leads to JavaScript execution in the context of the viewing user, who must be authenticated as a partner. The attack impacts any partner viewing the affected pages, enabling theft of session cookies, keystroke logging, or further exploitation. It targets web browsers interacting with Shopify's partner subdomain.

## Requirements

1. Pre-injected XSS payload in the attacker's Shopify profile
2. Access to create or view a partner account at https://partners.shopify.com/
3. Authenticated session as a partner user

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML entity encoding) when rendering user data in templates
- Use strict CSP headers to block unauthorized script sources
- Implement client-side monitoring for unexpected script execution and log to a SIEM

## Objectives

1. Reflect and execute the stored payload in victim browsers
2. Gain arbitrary JavaScript control in authenticated contexts
3. Facilitate data collection or session manipulation

## Instructions

### Step 1: Access Partners Dashboard

**Context**: Log in or create a partner account to reach pages that display user profile data.

Navigate to https://partners.shopify.com/ and sign up for a new account if needed, or use an existing one.

### Step 2: Navigate to Trigger Pages

**Context**: Proceed to pages that reflect the profile name, such as confirmation or completion endpoints.

Go to https://partners.shopify.com/[partnerID]/confirm or https://partners.shopify.com/[partnerID]/complete, replacing [partnerID] with the actual ID from the URL.

> The payload executes automatically upon rendering the page.

### Step 3: Observe Execution

**Context**: Verify the XSS by checking for payload effects like alerts or console logs.

Inspect the browser console or watch for the alert; if using a data-exfiltrating payload, check for network requests to attacker-controlled servers.

> Expected output: JavaScript alert or network activity confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[Execution]]
