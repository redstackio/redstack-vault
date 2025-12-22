---
tags:
  - subdomain-takeover
  - feedpress
type: procedure
tools:
  - '[[tools/Feed-Press]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Email Accounts]]'
updated_at: '2025-12-14T04:51:10.708Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9057c4b2-a9e1-4e6f-a918-8132a0a79b49
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Email Accounts]]'
---
# Claim-Subdomain-on-Feed-Press

## Summary

This procedure registers a dangling subdomain on Feed.Press to gain control, exploiting the lack of an active account.

## Description

Feed.Press allows custom domain registration for podcast/RSS hosting. By creating an account and setting podcasts.slack-core.com as the custom domain, DNS propagation hands over control, enabling content serving via nginx on 5.135.16.40.

## Requirements

1. Access to Feed.Press (https://feed.press/)
2. Confirmed dangling CNAME
3. Email for account creation

## Defense

Defensive measures and detection strategies:

- Proactively claim or delete dangling records
- Monitor third-party registrations for owned domains
- Use domain monitoring services like Certificate Transparency logs

## Objectives

1. Secure control of the subdomain
2. Enable custom configuration
3. Achieve initial access via misconfiguration

## Instructions

### Step 1: Create Feed.Press Account

**Context**: Sign up to access domain registration features.

Visit https://feed.press/ and register a new account.

> Expected: Account created successfully.

### Step 2: Configure Custom Domain

**Context**: Claim the dangling subdomain.

In the dashboard, add podcasts.slack-core.com as a custom domain and verify.

> Expected: Domain propagation (may take minutes); control granted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Email Accounts]] Third-party Software

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Feed-Press]]

## Tags

- [[subdomain-takeover]]
- [[feedpress]]
