---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - account-creation
  - subdomain-hijack
  - instapage
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
  - '[[Email Accounts]]'
updated_at: '2025-12-14T04:39:01.942Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Email Accounts]]'
---
# Claim-Subdomain-via-Instapage-Account

## Summary

This procedure details creating a new Instapage account and exploiting the 0day to claim a dangling subdomain like www.hacker.one by associating it with the existing CNAME record.

## Description

Targeting Instapage's weak validation, the attacker signs up and links the subdomain directly. In a web-based environment, this grants publishing rights without ownership proof. Outcomes include hijacked subdomain control, with prerequisites being a confirmed dangling CNAME.

## Requirements

1. Email for Instapage signup.
2. Identified dangling subdomain from prior enumeration.
3. Web browser access to Instapage.

## Defense

Defensive measures and detection strategies:

- Require DNS TXT records for domain verification in services like Instapage.
- Monitor third-party service logs for new domain claims on known CNAMEs.
- Use certificate transparency logs to detect unauthorized subdomain usage.

## Objectives

1. Successfully create and configure an Instapage account.
2. Associate the target subdomain via CNAME.
3. Gain administrative control over the subdomain.

## Instructions

### Step 1: Create Instapage Account

**Context**: Sign up for a new account to access domain claiming features.

Navigate to instapage.com and complete registration with an email.

> Expected: Account dashboard accessible.

### Step 2: Associate Dangling Subdomain

**Context**: Link the subdomain in domain settings.

In the dashboard, go to Domains > Add Custom Domain, enter www.hacker.one, and confirm CNAME setup (already exists).

> Expected output: Domain associated successfully, no validation errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Email Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-hijack]]
- [[instapage]]
