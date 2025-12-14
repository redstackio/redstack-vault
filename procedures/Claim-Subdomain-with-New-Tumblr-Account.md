---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - tumblr-claim
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Compromise Accounts]]'
updated_at: '2025-12-14T04:51:10.439Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Compromise Accounts]]'
---
# Claim Subdomain with New Tumblr Account

## Summary

This procedure creates a new account on the third-party service and claims the dangling custom domain, gaining control over the associated subdomain.

## Description

By registering a free Tumblr account and adding the expired domain as a custom domain, the attacker redirects the DNS resolution to their controlled blog. In this case, adding 'snapchat-blog.com' to a new account under 'jreynoldsdev' seizes control, allowing content manipulation on blog.snapchat.com.

## Requirements

1. Free Tumblr account creation (email required)
2. Access to Tumblr dashboard settings
3. Confirmed unclaimed domain from prior verification

## Defense

Defensive measures and detection strategies:

- Renew custom domain claims proactively before expiration
- Monitor DNS changes and third-party logs for unauthorized claims
- Use domain monitoring services to alert on resolution changes

## Objectives

1. Secure control of the external domain via third-party service
2. Redirect subdomain traffic to attacker-controlled content
3. Enable hosting of arbitrary pages

## Instructions

### Step 1: Create Tumblr Account

**Context**: Register a new account to serve as the claiming entity.

Visit tumblr.com and sign up with a new username (e.g., jreynoldsdev) and email.

> Account creation completes in seconds; no verification needed for basic use.

### Step 2: Add Custom Domain

**Context**: Configure the account to claim the dangling domain.

In the Tumblr dashboard, go to Settings > Custom Domain and enter 'snapchat-blog.com'.

> Tumblr verifies and assigns control; DNS propagation may take minutes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Compromise Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[tumblr-claim]]
- [[subdomain-takeover]]
