---
id: proc-uuid-002
tags:
  - race-condition
  - web
  - authentication
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:18.791Z'
skill_level: intermediate
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Log-In-with-Multiple-Accounts-in-Separate-Browsers

## Summary

This procedure establishes concurrent sessions for multiple user accounts using separate browser instances to enable parallel actions in a race condition attack.

## Description

To exploit timing-based vulnerabilities like race conditions in web applications, multiple authenticated sessions are needed. This involves logging into distinct accounts (e.g., two test users) in isolated browser environments to avoid cookie/session interference. The target is a web platform's login endpoint, ensuring each session can independently interact with invitation endpoints. Prerequisites include having multiple valid accounts; outcomes include ready sessions for simultaneous requests.

## Requirements

1. Two or more valid user accounts on the target platform
2. Web browser supporting multiple sessions (e.g., Chrome with incognito)
3. Network access to the login page

## Defense

Defensive measures and detection strategies:

- Rate-limit login attempts per IP
- Detect and flag multi-session logins from the same IP
- Enforce session isolation with unique tokens

## Objectives

1. Authenticate multiple accounts without session overlap
2. Prepare for concurrent endpoint interactions
3. Verify session validity for exploitation

## Instructions

### Step 1: Open Separate Browser Sessions

**Context**: Isolate sessions to simulate independent users.

**Instructions**: Launch two instances of [[tools/Web-Browser]], such as one standard window and one incognito/private mode.

> UI Action: In Browser 1, go to login page; in Browser 2, do the same in a new incognito tab.

### Step 2: Authenticate Each Account

**Context**: Log in to establish active sessions for each account.

**Instructions**: In Browser 1, enter credentials for Account A and submit; repeat in Browser 2 for Account B.

> UI Action: Fill username/password fields and click 'Log In'. Confirm dashboard access in both.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- race-condition
- web
- authentication
