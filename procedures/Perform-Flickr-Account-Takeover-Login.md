---
id: proc-005
tags:
  - account-takeover
  - login
  - auth-bypass
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
  - '[[Valid Accounts]]'
  - '[[T1078.004]]'
updated_at: '2025-12-14T17:33:34.439Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[T1078.004]]'
---
# Perform-Flickr-Account-Takeover-Login

## Summary

This procedure logs into Flickr using the case-variant email and attacker's password, exploiting normalization to takeover the victim's account.

## Description

Flickr's login normalizes emails case-insensitively from Cognito but accepts unverified ones. Using the exact variant capitalization in the login request matches the stored value, granting access to the victim's data since normalized emails collide.

## Requirements

1. Modified email variant in Cognito
2. Attacker's password
3. Access to login endpoint

## Defense

Defensive measures and detection strategies:

- Verify emails on every login
- Case-sensitive email storage and comparison
- Detect login attempts with mismatched case variants

## Objectives

1. Bypass verification for login
2. Access victim's account
3. Exfiltrate or control Flickr resources

## Instructions

### Step 1: Craft Login Request

**Context**: Prepare POST with exact case-variant email.

Send to https://identity.flickr.com/ with AuthParameters: USERNAME=exact-variant-email, PASSWORD=attacker-password.

> Ensure capitalization matches the updated value; normalization allows match to victim's account.

### Step 2: Submit and Access

**Context**: Complete authentication.

Intercept or directly send the request.

> Successful response grants session to victim's account, allowing photo access, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[T1078.004]] Cloud Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[login]]
- [[auth-bypass]]
