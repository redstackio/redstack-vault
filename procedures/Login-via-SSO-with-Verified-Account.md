---
tags:
  - wordpress
  - sso-login
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - WordPress
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: badb32d4-fdd9-4765-a2b3-1e178f8d8e2c
created_at: '2025-12-13T09:01:26.545Z'
updated_at: '2025-12-13T09:01:26.545Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Login via SSO with Verified Account

## Summary

This procedure uses the now-verified WordPress.com account to log into the target WordPress site via SSO, achieving unauthorized access.

## Description

With the email verified and matched, the attacker can access the admin panel without legitimate credentials, potentially leading to further compromises.

## Requirements

1. Verified WordPress.com account with target email
2. Target WordPress site URL
3. Web browser

## Defense

Defensive measures and detection strategies:

- Disable email matching in JetPack
- Monitor SSO login attempts for anomalies

## Objectives

1. Gain admin access to WordPress site
2. Validate unauthorized entry
3. Prepare for post-exploitation

## Instructions

### Step 1: Navigate to Login

**Context**: Access the SSO login option.

Go to host.com WordPress panel, click 'sign in with wordpress.com'.

> SSO login prompt appears.

### Step 2: Complete Login

**Context**: Log in using the verified account.

Proceed to log in as admin.

> Successful access to admin dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[wordpress]]
- [[sso-login]]
