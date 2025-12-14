---
id: proc-verify-spam-001
tags:
  - verification
  - spam
  - hackerone
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/post-batched-report-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:29:57.223Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Verify Bulk Report Creation

## Summary

This procedure checks the target HackerOne program's reports page post-attack to confirm successful bypass and spam creation of over 6400 reports.

## Description

After the race attack, refresh the team's inbox to observe the impact. This validates the exploitation of batching and race conditions, showing the vulnerability's severity in enabling DoS via overwhelming notifications.

## Requirements

1. Web browser with HackerOne login
2. Access to the target team's reports page
3. Recent execution of the attack chain

## Defense

Defensive measures and detection strategies:

- Alert on sudden spikes in report volume per program
- Log and review batched GraphQL operations for abuse patterns

## Objectives

1. Confirm rate limit evasion
2. Quantify impact (e.g., 6400+ reports)
3. Document for reporting the vulnerability

## Instructions

### Step 1: Access Reports Page

**Context**: Navigate to the target team in HackerOne.

Open browser, log in to HackerOne, and go to https://hackerone.com/{target-team-handle}/reports.

> Prepares for verification. Expected output: Standard reports interface.

### Step 2: Refresh and Inspect

**Context**: Check for new bulk reports after ~40 seconds.

Refresh the page (F5) and scroll to view recent submissions.

If verifying a single batch, resend [[commands/post-batched-report-request]] via Burp.

> Displays all new reports with batched content. Expected output: 6400+ entries visible, each with identical title/impact from the script.

**Success Indicators**:
- Report count exceeds 500
- Timestamps clustered within 40 seconds

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/post-batched-report-request]]

## Tools Used

- [[tools/Web-Browser]]

## Tags

- verification
- spam
- hackerone
