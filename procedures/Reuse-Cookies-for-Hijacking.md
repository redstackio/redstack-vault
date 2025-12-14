---
tags:
  - hijacking
  - cookies
type: procedure
tools:
  - '[[tools/EditThisCookie-Extension]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.639Z'
sub_techniques: []
id: 46068ced-78e4-4718-9c86-18a3a0964b44
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Valid Accounts]]'
---
# Reuse-Cookies-for-Hijacking

## Summary

This procedure imports previously extracted session cookies after logout and delay, restoring access without authentication to hijack the victim's session in HackerOne.

## Description

Exploiting non-invalidated cookies, this reuses them post-logout to impersonate the user. Applicable to web apps with poor session expiry. Technical: Browser imports cookies, server accepts them as valid. Prerequisites: Saved cookies, delay to simulate real hijack. Outcome: Unauthorized access.

## Requirements

1. Saved cookie file from extraction
2. Cookie management extension installed
3. Wait period (6-8 hours) to test persistence

## Defense

Defensive measures and detection strategies:

- Enforce session timeouts and idle expiration
- IP binding or device fingerprinting for session validation
- Detect cookie reuse from new contexts (e.g., different user agents)

## Objectives

1. Restore hijacked session
2. Access protected resources post-logout
3. Demonstrate indefinite reuse risk

## Instructions

### Step 1: Wait and Prepare

**Context**: Simulate time passage for real-world hijack scenario.

No command; time-based:

1. Wait 6-8 hours after logout
2. Open browser and ensure no active HackerOne session

> Prepares for import without interference.

### Step 2: Import Cookies

**Context**: Load saved cookies to reinstate session.

Use extension:

1. Open [[tools/EditThisCookie-Extension]]
2. Select hackerone.com domain
3. Use 'Import' function and paste/load from cookies.txt
4. Apply changes and refresh https://www.hackerone.com/

> Session restores; user is logged in automatically.

### Step 3: Verify Hijack

**Context**: Test access to confirm success.

Navigate to protected page (e.g., reports).

> Expected: Full access as original user, no login required.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/EditThisCookie-Extension]]

## Tags

- [[hijacking]]
- [[cookies]]
