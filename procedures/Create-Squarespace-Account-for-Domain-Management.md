---
tags:
  - account-creation
  - domain-hijacking
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
  - '[[Email Accounts]]'
updated_at: '2025-12-14T04:51:10.498Z'
sub_techniques: []
id: f322918d-9662-4375-95bb-1c841d9d8a2d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Email Accounts]]'
---
# Create Squarespace Account for Domain Management

## Summary

This procedure involves signing up for a free Squarespace trial to gain access to domain management features, allowing the claiming of unowned subdomains with existing verification DNS records.

## Description

Squarespace's domain claiming process can be abused if a subdomain has a lingering CNAME to their verification servers. By creating a free account, the attacker unlocks the UI to input and claim such domains, redirecting traffic to their hosted site. This targets web platforms and requires no prior access.

## Requirements

1. Email address for signup
2. Internet browser
3. No payment info for trial

## Defense

Defensive measures and detection strategies:

- Monitor for unauthorized domain claims on third-party platforms
- Revoke old verification records promptly after use
- Implement account verification for domain management

## Objectives

1. Obtain domain settings access
2. Prepare for subdomain claiming
3. Enable hosting under claimed domain

## Instructions

### Step 1: Sign Up for Free Trial

**Context**: Initiate account creation to access premium features like domain tools.

**Command** (Browser-based):

Navigate to https://www.squarespace.com/ and click 'Start Free Trial'.

> Fill in details; account activates immediately with domain access.

### Step 2: Access Domain Settings

**Context**: Verify dashboard access for claiming.

**Command** (UI Navigation):

Log in and go to Settings > Domains.

> Confirms availability of 'Use a Domain I Own' option.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Email Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[domain-hijacking]]
