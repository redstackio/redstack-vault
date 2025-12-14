---
tags:
  - bypass
  - google
  - direct-redirect
type: procedure
tools:
  - '[[tools/Clean-Browser-Instance]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Google
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.900Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7aa94a5e-181c-4aa5-856a-518095aa2f5b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Bypass-Google-Login-for-Direct-Redirect

## Summary

For victims not logged into Google, this procedure skips the logout/relogin and credential capture, directly redirecting to the follower site to proceed with Twitter app installation.

## Description

If no active Google session is detected, the SetSID URL bypasses authentication steps and chains straight to getmorefollowers.biz, ensuring the attack continues toward OAuth misuse.

## Requirements

1. Malicious URL without dependency on Google session
2. Clean browser without prior Google cookies
3. Redirect logic to handle non-logged-in state

## Defense

Defensive measures and detection strategies:

- Log direct redirects from suspicious sources
- Warn users about unsolicited follower sites
- Block domains like getmorefollowers.biz

## Objectives

1. Avoid stalled chain on non-logged-in users
2. Maintain attack flow to Twitter phase
3. Ensure broad victim coverage

## Instructions

### Step 1: Detect Non-Logged-In State

**Context**: URL loads without session, skipping SetSID effects.

Browser navigates directly past Google.

> Expected: No logout prompt.

### Step 2: Direct to Follower Site

**Context**: Chain proceeds to getmorefollowers.biz.

Follow built-in redirect.

> Expected: Lands on site, ready for Twitter redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Clean-Browser-Instance]]

## Tags

- [[bypass]]
- [[google]]
- [[direct-redirect]]
