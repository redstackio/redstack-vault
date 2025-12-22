---
tags:
  - account-claim
  - uservoice
  - no-verification
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T04:51:10.582Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[T1133.001]]'
id: cc672402-0688-4a72-bb98-9844b96f9307
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Claim Subdomain by Signing Up on UserVoice

## Summary

This procedure exploits the lack of verification in UserVoice to create an account and claim a subdomain namespace tied to an existing CNAME record.

## Description

Attackers sign up at uservoice.com, choosing the 'Screenhero' username, which automatically links to screenhero.uservoice.com due to no ownership checks. This grants control over the associated subdomain without prior access.

## Requirements

1. Web browser access to uservoice.com
2. Valid email for signup (no special creds)
3. Confirmed inactive instance from prior step

## Defense

Defensive measures and detection strategies:

- Contact UserVoice to enable verification for custom instances
- Audit and reclaim abandoned third-party accounts periodically
- Use DNSSEC or CAA records to restrict subdomain delegations

## Objectives

1. Secure ownership of the subdomain namespace
2. Establish persistence on the legitimate domain
3. Enable content hosting under the trusted subdomain

## Instructions

### Step 1: Access Signup Page

**Context**: Navigate to UserVoice registration to initiate account creation.

Visit https://www.uservoice.com/signup in a browser and start the process.

### Step 2: Select and Claim Username

**Context**: During setup, enter 'Screenhero' as the site name or username to associate with the inactive instance.

Complete registration; UserVoice will provision the instance without verification, linking to the CNAME.

**Expected Output**: Dashboard access for the new 'Screenhero' site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques

- [[T1133.001]]

## Commands Used


## Tools Used


## Tags

- [[account-claim]]
- [[no-verification]]
