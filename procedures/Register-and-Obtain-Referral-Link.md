---
id: proc-uuid-1
tags:
  - registration
  - web
  - airbnb
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.637Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register-and-Obtain-Referral-Link

## Summary

This procedure outlines creating an Airbnb account and accessing the referral invite feature to obtain a base URL for subsequent IDOR exploitation.

## Description

In the context of exploiting Airbnb's referral system, initial access requires a legitimate account to generate a standard referral link. This link contains parameters vulnerable to IDOR manipulation. The process targets the public-facing web application and assumes no prior authentication beyond registration.

## Requirements

1. Internet access and a web browser
2. Valid email address for account verification
3. No special permissions or tools needed

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA on registration to prevent automated account creation
- Monitor for rapid successive registrations from the same IP
- Rate-limit referral link generations per account

## Objectives

1. Establish initial legitimate access to the referral system
2. Capture a sample URL with exploitable parameters
3. Prepare base for parameter tampering

## Instructions

### Step 1: Create Airbnb Account

**Context**: Register a new user account to gain access to personalized features like invites.

Navigate to https://www.airbnb.com and click "Sign up". Provide an email, password, and complete any verification steps. No payment details are required for this.

### Step 2: Access Invite Friends Feature

**Context**: Generate the referral link from the account dashboard.

After logging in, go to your profile, select "Invite friends", and copy the provided referral URL, which includes euid, ri, and s parameters.

**Expected Output**: URL like `http://www.airbnb.com/c/spent1?euid=ed736125-704e-f1ec-bb76-4ca60026141d&ri=14052412&s=30`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[registration]]
- [[web]]
- [[airbnb]]
