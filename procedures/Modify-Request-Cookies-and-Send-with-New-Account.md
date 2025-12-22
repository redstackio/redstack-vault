---
tags:
  - cookie-manipulation
  - session-hijacking
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Default Accounts]]'
id: c7d574fd-5286-4c8c-9064-71fb3fd6e1b1
created_at: '2025-12-14T17:30:07.259Z'
updated_at: '2025-12-14T17:30:07.259Z'
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Modify-Request-Cookies-and-Send-with-New-Account

## Summary

Replace the session cookies in an intercepted blog creation request with those from an ineligible new Lichess account and forward it to bypass access controls.

## Description

The vulnerability stems from the server trusting session cookies for authentication without re-validating account eligibility (e.g., age or activity). By swapping cookies in Burp Repeater, the request appears to come from the new account, tricking the server into creating the blog under the ineligible user.

## Requirements

1. Intercepted request from previous procedure
2. Session cookies from new Lichess account (view in browser dev tools or separate Burp session)
3. Burp Suite Repeater active

## Defense

Defensive measures and detection strategies:

- Re-validate eligibility on every request, not just authentication
- Bind requests to additional factors like IP or user-agent
- Log cookie mismatches or unusual session behaviors

## Objectives

1. Associate the valid request payload with the new account's session
2. Trigger blog creation without eligibility checks
3. Obtain the redirect to the new blog URL

## Instructions

### Step 1: Extract New Account Cookies

**Context**: Get the session identifiers for substitution.

Log in to the new account in a separate browser or tab, open dev tools (F12), go to Network tab, and copy the Cookie header values (e.g., session_id, user_id) from a simple page load.

### Step 2: Modify and Send Request

**Context**: Swap cookies to bypass restrictions.

In Burp Repeater, edit the Cookie header to replace with new account's values (e.g., Cookie: session=abc123; user=newuser). Ensure other headers and body remain intact. Click 'Send' to forward.

**Expected Output**: 302 response with Location: https://lichess.org/blog/[generated-slug]

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[Default Accounts]] Default Accounts

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[cookie-manipulation]]
- [[session-hijacking]]
- [[web]]
