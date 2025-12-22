---
id: proc-register-modulus-claim
tags:
  - account-creation
  - subdomain-takeover
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
  - '[[T1583.003]]'
updated_at: '2025-12-14T04:51:26.598Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1583.003]]'
---
# Register Modulus.io Account and Attempt Subdomain Claim

## Summary

This procedure involves creating a Modulus.io account and attempting to add a specific dangling subdomain (api.legalrobot.com) to test claimability, revealing if it's already partially registered but inactive.

## Description

Modulus.io, a now-defunct PaaS, allowed domain additions for hosting apps. In this scenario, after detecting the dangling record, an attacker signs up and tries adding the subdomain in the dashboard, receiving an error that it's 'already added somewhere'. This confirms the DNS points to Modulus but no active app exists, paving the way for wildcard claims. Target environment: Modulus.io web dashboard. Prerequisites: email for signup. Expected outcomes: account ready, direct claim blocked.

## Requirements

1. Valid email address for Modulus.io signup
2. Web browser access to modulus.io
3. Awareness of the target subdomain

## Defense

Defensive measures and detection strategies:

- Remove or update dangling DNS records promptly
- Monitor for new accounts claiming your domains on third-party services
- Use automated scanners like Subjack to detect takeovers early

## Objectives

1. Establish presence on the hosting service
2. Probe for direct subdomain availability
3. Identify restrictions leading to alternative claim methods

## Instructions

### Step 1: Create Modulus.io Account

**Context**: Sign up to gain access to the domain management dashboard.

Navigate to modulus.io and complete the registration form with an email and password.

> Expected output: Confirmation email and dashboard access.

### Step 2: Attempt Subdomain Addition

**Context**: Try adding the specific subdomain to see if it's claimable.

In the dashboard, enter 'api.legalrobot.com' in the domain addition field and submit.

> Expected output: Error message 'already added somewhere', indicating dangling status.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1583.003]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[subdomain-takeover]]
