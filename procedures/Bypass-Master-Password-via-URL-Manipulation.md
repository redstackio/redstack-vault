---
tags:
  - url-manipulation
  - authentication-bypass
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Modify Authentication Process]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5342f9ef-b4a8-4d7b-8b46-8c138cf25658
created_at: '2025-12-13T09:01:26.808Z'
updated_at: '2025-12-13T09:01:26.808Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Bypass Master Password via URL Manipulation

## Summary

This procedure bypasses the master password prompt in Shopify's account merging by directly modifying the URL to access the new-password endpoint.

## Description

At the login path, change to /accounts_merge/new-password while preserving query parameters. This exploits lack of access control, allowing direct password setting. Outcome is access to password change without master credentials.

## Requirements

1. Active merging session
2. Web browser for URL editing

## Defense

Defensive measures and detection strategies:

- Implement proper access controls on endpoints
- Validate navigation paths in merging flow

## Objectives

1. Avoid master password requirement
2. Reach new password setting page

## Instructions

### Step 1: Modify URL Path

**Context**: Change the path manually.

From /login?query-params, update to /accounts_merge/new-password?query-params.

> Bypasses the password prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Modify Authentication Process]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[url-manipulation]]
- [[authentication-bypass]]
- [[shopify]]
