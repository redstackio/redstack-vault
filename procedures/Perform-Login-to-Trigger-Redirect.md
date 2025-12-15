---
id: uuid-proc-3-683298
tags:
  - login-bypass
  - redirect-trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:35.080Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Perform-Login-to-Trigger-Redirect

## Summary

This procedure authenticates on the vulnerable MoPub login page to trigger the open redirect defined in the 'next' parameter, confirming the vulnerability's exploitability.

## Description

After setting a malicious 'next' parameter, completing the login process causes the application to redirect to the specified URL. The lack of validation allows this even for external sites, enabling attacks like phishing. This interactive step requires valid credentials and observes the post-auth flow.

## Requirements

1. Valid username and password for MoPub.
2. Modified login URL with 'next' parameter.
3. Browser session to handle cookies and redirects.

## Defense

Defensive measures and detection strategies:

- Validate user sessions and redirect origins server-side.
- Rate-limit login attempts with suspicious parameters.
- Audit authentication logs for redirect patterns.

## Objectives

1. Successfully authenticate while preserving the 'next' parameter.
2. Trigger redirection to verify exploit.
3. Maintain session for potential follow-on attacks.

## Instructions

### Step 1: Enter Credentials

**Context**: Fill the login form on the modified URL.

Navigate to https://app.mopub.com/login?next=https://evil.com and input credentials.

> Form should submit without stripping the parameter.

### Step 2: Submit and Observe

**Context**: Complete authentication to initiate redirect.

Click login button.

> Expected: Redirect to evil.com upon success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[T1566.002]] Phishing: Spearphishing Link

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[authentication]]
- [[redirect]]
