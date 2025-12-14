---
tags:
  - xss
  - phishing
  - execution
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:30.440Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e1265313-84f6-4539-b44c-781c3bae86f6
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Deliver-URL-and-Trigger-XSS-Execution

## Summary

This procedure delivers the malicious callback URL to a victim, prompting login and triggering the reflected XSS payload for JavaScript execution in the authenticated context.

## Description

In a phishing scenario, the crafted URL is shared with the victim, who accesses it and is redirected to login. Upon authentication, the server reflects the unsanitized path payload, executing JS like prompt(1) or more malicious code (e.g., cookie exfiltration). This impacts all OWOX BI users with high severity due to post-auth code execution. Requires social engineering for delivery; outcomes include arbitrary JS in victim browser.

## Requirements

1. Crafted malicious URL from previous step
2. Phishing channel (email, chat) to victim
3. Victim with OWOX BI account

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious URLs
- Implement multi-factor authentication (MFA) for logins
- Deploy XSS auditors or WAF rules to block reflected payloads

## Objectives

1. Induce victim to access and authenticate via malicious URL
2. Achieve JS execution in post-login session
3. Enable data theft or session hijacking

## Instructions

### Step 1: Share Malicious URL

**Context**: Deliver the URL to the target via a convincing pretext.

Send the URL (e.g., https://bi.owox.com/ui/callbacks/google-supervisors/analytics%3Cimg%20src=xss%20onerror=prompt(1)%3E/?state=... ) in an email claiming "Fix Google Analytics integration error".

> Expected: Victim clicks and is prompted for OWOX BI login.

### Step 2: Observe Execution

**Context**: Confirm payload triggers after login.

Victim logs in; monitor for execution indicators like the prompt dialog or network requests if payload is enhanced.

> Expected: JS executes, e.g., alert box appears, confirming vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- xss
- delivery
- trigger
