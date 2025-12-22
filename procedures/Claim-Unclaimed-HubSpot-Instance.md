---
tags:
  - subdomain-takeover
type: procedure
tools:
  - '[[tools/HubSpot]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/dig-dns-lookup]]'
  - '[[commands/curl-host-content]]'
platforms:
  - Web
techniques:
  - '[[Compromise Infrastructure]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: e998ae3a-8d58-4844-958d-80d1db2117e9
created_at: '2025-12-11T06:10:30.559Z'
updated_at: '2025-12-11T06:10:30.559Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1584]]'
---
# Claim Unclaimed HubSpot Instance

## Summary

This procedure involves registering and claiming an unclaimed HubSpot instance linked to a dangling CNAME, granting control over the associated subdomain.

## Description

Attackers can sign up for HubSpot and claim expired sites, allowing them to host content on the subdomain. In the Roblox case, this enabled control over devrel.roblox.com for further exploits like phishing or script hosting.

## Requirements

1. HubSpot account
2. Knowledge of the unclaimed instance URL
3. Web browser access

## Defense

Defensive measures and detection strategies:

- Remove dangling DNS records promptly
- Monitor for unauthorized claims on third-party services

## Objectives

1. Gain control of the subdomain
2. Enable content hosting
3. Set stage for malicious payloads

## Instructions

### Step 1: Access HubSpot Claim Page

**Context**: Navigate to HubSpot and initiate claim process.

Manual step: Log in to HubSpot and search for the unclaimed site using the CNAME value.

> Expected: Option to claim the site.

### Step 2: Complete Registration

**Context**: Register the site under attacker control.

Manual step: Follow HubSpot prompts to claim and verify ownership.

> Expected: Confirmation of successful claim.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Compromise Infrastructure]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/HubSpot]]

## Tags

- [[subdomain-takeover]]
