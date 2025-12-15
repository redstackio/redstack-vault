---
id: proc-632017-05
tags:
  - account-takeover
  - token-theft
  - phishing
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/xss-payload-fb-token-steal]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:27:49.943Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Execute-Account-Takeover-via-Victim-Interaction

## Summary

This procedure tricks the victim into visiting the malicious page, chaining CSRF and XSS to steal their OAuth tokens for account takeover.

## Description

Victim clicks phishing link: page logs them out (CSRF), logs in attacker (CSRF), redirects to XSS review. Victim edits review, triggering XSS to steal their new tokens. Attacker uses tokens to access victim's account. Prerequisites: Malicious page from Step 4; social engineering. Outcome: Full control of victim's account.

## Requirements

1. Hosted malicious page URL
2. Victim's interest in the review (e.g., targeted phishing)
3. Attacker server for token receipt
4. Valid XSS review link

## Defense

Defensive measures and detection strategies:

- User education on phishing links
- Multi-factor authentication beyond OAuth tokens
- Anomaly detection on session changes/logins
- Block known malicious domains

## Objectives

1. Induce victim interaction
2. Chain exploits for token theft
3. Achieve account control

## Instructions

### Step 1: Distribute Phishing Link

**Context**: Send the malicious page URL to victim (e.g., via email/SMS).

**Command** (No CLI; social engineering):

> "Check this review: [malicious URL]"

### Step 2: Monitor Execution and Theft

**Context**: Victim loads page; wait for edit trigger.

**Command** ([[commands/xss-payload-fb-token-steal]]):

> On edit, XSS runs: Loads FB SDK, gets authResponse, POSTs to attacker.com.

> Expected: Tokens arrive at server; use them to login as victim on https://www.zomato.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used

- [[commands/xss-payload-fb-token-steal]]

## Tools Used


## Tags

- [[account-takeover]]
- [[token-theft]]
- [[Phishing]]
