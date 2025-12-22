---
tags:
  - burp-suite
  - request-manipulation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b1a17b02-c2a5-4ce9-a7a1-90f7b068ca83
created_at: '2025-12-11T06:10:22.798Z'
updated_at: '2025-12-11T06:10:22.798Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Configure Burp Suite for Request Manipulation

## Summary

This procedure sets up Burp Suite to intercept and replace email addresses in HTTP requests, enabling manipulation of Shopify's email confirmation process.

## Description

Burp Suite is configured with match and replace rules to swap the attacker's email with the victim's in transit. This is crucial for bypassing verification during page refreshes and uploads. The procedure targets Shopify's web requests, with the outcome being dynamic email substitution for exploitation.

## Requirements

1. Installed Burp Suite
2. Browser configured to proxy through Burp
3. Active Shopify session

## Defense

Defensive measures and detection strategies:

- Enforce server-side validation of email changes
- Detect proxy tool signatures in request patterns

## Objectives

1. Set up email replacement rules
2. Enable interception for specific actions
3. Prepare for confirmation bypass

## Instructions

### Step 1: Set Up Match and Replace

**Context**: Configure Burp to replace emails.

Set up a match and replace rule in Burp to swap the email in requests to the victim's email.

### Step 2: Refresh Page with Replacement

**Context**: Reload the account page with interception.

Refresh the account page to update with the victim's email, with Burp intercepting and replacing.

### Step 3: Toggle Rules as Needed

**Context**: Disable and re-enable rules for confirmation.

Disable match and replace, refresh, change to owned email, then re-enable for substitution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- burp-suite
- request-manipulation
