---
id: proc-uuid-1
tags:
  - account-creation
  - reddit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:25:33.843Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-and-Configure-Reddit-Accounts

## Summary

This procedure sets up multiple Reddit accounts for testing badge visibility and IDOR exploitation, using email or mobile verification to simulate attacker and target environments.

## Description

In the context of the Reddit IDOR vulnerability, creating accounts allows unlocking specific badges and verifying hiding mechanisms. The primary account is used to earn and hide badges, while a secondary account observes public visibility. No advanced tools are needed; standard web registration suffices. Prerequisites include access to email or a mobile number for verification.

## Requirements

1. Internet access to reddit.com
2. Valid email address or mobile number for verification
3. Web browser for navigation and registration

## Defense

Defensive measures and detection strategies:

- Monitor for bulk account creations from single IPs (rate limiting)
- Require CAPTCHA on registrations
- Log unusual verification patterns

## Objectives

1. Establish a primary account for badge manipulation
2. Create a secondary account for external observation
3. Ensure accounts are verified and functional

## Instructions

### Step 1: Register Primary Account

**Context**: Create the main account to unlock badges.

Navigate to reddit.com and click 'Sign Up'. Provide username, email, and password. Complete email verification.

### Step 2: Register Secondary Account

**Context**: Set up an observer account with mobile verification.

Repeat registration process using a mobile number for SMS verification. Log in to confirm access.

### Step 3: Log In to Primary Account

**Context**: Prepare for badge unlocking actions.

Enter credentials at reddit.com/login to access the primary account dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[account-creation]]
- [[reddit]]
