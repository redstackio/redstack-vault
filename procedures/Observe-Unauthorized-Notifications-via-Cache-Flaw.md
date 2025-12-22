---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - information-disclosure
  - caching-misconfiguration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.374Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Observe Unauthorized Notifications via Cache Flaw

## Summary

This procedure involves browsing the HackerOne platform's notification feed to observe and identify notifications belonging to other users, exposed due to incorrect cache key generation for Notification::NotEligibleForBounty types.

## Description

In HackerOne's notification system, cache keys are generated based on notification type and user context. A flaw causes keys for ineligible bounty notifications to overlap, serving cached data from other users. This leads to partial visibility of report-related notifications (e.g., Yahoo or Slack bugs) in an authenticated user's feed. The procedure targets web-based discovery without tools, relying on standard browser navigation. Expected outcomes include sighting unauthorized metadata, confirming a privacy leak that persists until session reset.

## Requirements

1. Authenticated HackerOne account with access to notifications
2. Web browser (e.g., Chrome, Firefox)
3. Internet connection to HackerOne platform

## Defense

Defensive measures and detection strategies:

- Implement user-specific cache key prefixes to prevent cross-user data leakage
- Monitor cache hit rates for anomalies in notification endpoints
- Enforce strict access controls on JSON notification fetches

## Objectives

1. Detect presence of unauthorized notifications in the feed
2. Gather evidence of privacy leak for reporting
3. Assess scope of disclosed information (partial metadata only)

## Instructions

### Step 1: Access Notification Feed

**Context**: Log in and navigate to the notifications section to load the feed via the underlying JSON endpoint.

No specific command required; use browser to visit https://hackerone.com/notifications.

> The feed populates from a JSON endpoint that fetches cached notifications. Look for entries not matching your reports.

### Step 2: Scan for Anomalies

**Context**: Visually inspect the feed for notifications related to external reports.

Browse pages and note any mentions of Yahoo or Slack reports not submitted by you.

> Successful observation indicates cache key collision, leaking partial details like report titles or types.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[information-disclosure]]
- [[caching-misconfiguration]]
- [[privacy-leak]]
