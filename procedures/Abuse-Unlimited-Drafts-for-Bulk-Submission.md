---
tags:
  - misconfiguration
  - dos
  - spam
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
created_at: '2025-12-14T17:30:26.559Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:26.559Z'
skill_level: novice
impact_level: low
detection_risk: low
sub_techniques: []
id: 9a9a8320-2169-490c-9b6e-01538bbff62d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Abuse-Unlimited-Drafts-for-Bulk-Submission

## Summary

This procedure exploits a misconfiguration in the HackerOne report submission system that permits unlimited creation of draft reports, allowing an attacker to generate and submit them in bulk, potentially spamming the platform or causing minor overload.

## Description

The HackerOne platform's draft feature, intended for users to save unfinished reports, lacked restrictions on the number of drafts that could be created or submitted simultaneously. An authenticated user can repeatedly start new drafts with minimal input, accumulate them, and then submit all at once, bypassing any per-report rate limits. This was discovered and demonstrated during a platform celebration event, leading to a low-severity rating and subsequent mitigation by capping drafts at 500. The attack requires only a standard user account and targets the web interface, with impacts limited to administrative annoyance or temporary load spikes.

## Requirements

1. Authenticated HackerOne account with report submission access
2. Web browser with JavaScript enabled for interface interaction
3. Direct network access to hackerone.com (no VPN or proxy restrictions)

## Defense

Defensive measures and detection strategies:

- Implement hard limits on draft creation (e.g., 500 per user/session)
- Add rate limiting on submission endpoints to prevent bulk actions
- Monitor for anomalous submission patterns, such as high-volume drafts from single accounts
- Use CAPTCHA or secondary verification for bulk operations

## Objectives

1. Create unlimited draft reports to accumulate submissions
2. Submit drafts in bulk to overwhelm or spam the system
3. Demonstrate misconfiguration for vulnerability disclosure

## Instructions

### Step 1: Access Report Submission Interface

**Context**: Log in to HackerOne and navigate to the report creation page to begin exploiting the draft feature.

No specific command required; use the web interface to start a new report and enter draft mode by partially filling the form without submitting.

> Repeat this process multiple times (e.g., 100+ drafts) to build up the queue. Each draft remains unsaved and unrestricted.

### Step 2: Accumulate and Submit Drafts

**Context**: Once multiple drafts are created, use the drafts management to select and submit them all simultaneously.

No specific command required; from the user's dashboard or drafts list, bulk-select and trigger submission.

> This action sends all drafts to the backend for processing, potentially flooding the system with simultaneous requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[misconfiguration]]
- [[dos]]
- [[spam]]
- [[web]]

---
