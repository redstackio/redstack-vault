---
tags:
  - spamming
  - reporting
  - abuse
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 90f333ef-484e-4bc9-ba97-4333dc146b18
created_at: '2025-12-14T17:28:28.720Z'
updated_at: '2025-12-14T17:28:28.720Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Spam-Report-Comment-with-Multiple-Accounts

## Summary

This procedure exploits the lack of rate limiting by using a secondary account to repeatedly report a target comment on IntenseDebate, reaching the deletion threshold (e.g., 10 reports) to trigger automatic removal.

## Description

The core vulnerability allows unlimited reports without throttling, enabling attackers to abuse the moderation system. This involves logging in with another account, locating the comment, and submitting reports multiple times. Target is the web interface; scalable with automation but manual here. Expected outcome: Threshold met, leading to deletion.

## Requirements

1. Secondary IntenseDebate account
2. Target comment from prior step
3. Web browser for manual actions

## Defense

Defensive measures and detection strategies:

- Enforce rate limits (e.g., 1 report per minute per account/IP)
- Flag accounts with high report volumes
- Require justification or CAPTCHA for reports
- Integrate AI to detect spam patterns

## Objectives

1. Bypass rate limiting to accumulate reports
2. Trigger automatic moderation action
3. Demonstrate abuse potential on any comment

## Instructions

### Step 1: Login with Secondary Account

**Context**: Switch to attacker account for reporting.

Log in to IntenseDebate with different credentials.

> Dashboard accessible without issues.

### Step 2: Locate and Report Comment

**Context**: Target the specific comment repeatedly.

Visit the site, find the test comment, click "Report this comment" button 10 times, submitting each.

> Each submission succeeds; no blocks occur due to missing limits.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[spamming]]
- [[reporting]]
- [[abuse]]
- [[web]]
