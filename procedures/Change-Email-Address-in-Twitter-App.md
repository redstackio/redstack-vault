---
id: proc-twitter-email-change-001
tags:
  - twitter
  - android
  - privacy-violation
  - logic-error
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Stored Data Manipulation]]'
updated_at: '2025-12-14T17:24:45.324Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Stored Data Manipulation]]'
---
# Change-Email-Address-in-Twitter-App

## Summary

This procedure exploits a logic error in the Twitter Android app by changing the account's email address, which automatically unsets the 'Protect your Tweets' option without user consent, exposing private tweets publicly.

## Description

Navigating to the account settings in the Twitter Android app, a new valid email is entered and submitted via the 'Next' button. Due to the vulnerability, this action immediately disables tweet protection, making all previous private tweets visible to the public. This can be part of a phishing attack where the user is tricked into performing the change. The target is the Twitter Android app's email change feature. Prerequisites include a logged-in protected account. Expected outcome is unprotected tweets and an email change request sent.

## Requirements

1. Logged-in session in Twitter Android app with protected account
2. A new valid email address not associated with the account
3. Internet access for submission

## Defense

Defensive measures and detection strategies:

- Twitter should add confirmation prompts for protection changes during email updates
- Users should verify account settings after any email change
- Monitor for sudden protection status changes via API notifications or email alerts
- Phishing awareness training to avoid tricked email changes

## Objectives

1. Trigger the logic error to unprotect tweets
2. Initiate email change without alerting user to side effects
3. Expose private content for collection or further exploitation

## Instructions

### Step 1: Navigate to Email Settings

**Context**: Access the email change interface.

No command required; from the app dashboard, tap profile icon > Settings and privacy > Your account > Account information > Email.

> Expected output: Current email displayed with option to change.

### Step 2: Enter New Email

**Context**: Input details to trigger the flaw.

No command required; enter a new valid email address and tap 'Next'.

> The app submits the request, automatically unsetting protection. Expected output: Progress indicator for email update; check settings to see 'Protect your Tweets' now off.

### Step 3: Confirm Unprotection

**Context**: Validate the vulnerability activation.

No command required; go back to Privacy and safety > Protect your Tweets and observe it's disabled.

> Expected output: Toggle off without user action; tweets now potentially public.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Stored Data Manipulation]] Stored Data Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[twitter]]
- [[android]]
- [[privacy-violation]]
- [[logic-error]]
