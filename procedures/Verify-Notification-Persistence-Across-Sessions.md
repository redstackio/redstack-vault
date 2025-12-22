---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - information-disclosure
  - persistence-testing
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
updated_at: '2025-12-14T17:29:09.364Z'
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
# Verify Notification Persistence Across Sessions

## Summary

This procedure tests the persistence of unauthorized notifications by refreshing pages and navigating URLs, confirming the caching issue endures beyond initial load.

## Description

The caching flaw in HackerOne causes invalid cache keys to serve stale data persistently until cache invalidation or session change. By refreshing and navigating, the procedure verifies the leak's stability, highlighting the vulnerability's reliability for unauthorized viewing. Targets web sessions; outcomes include sustained visibility of other users' notifications.

## Requirements

1. Active session with observed unauthorized notifications
2. Web browser with developer tools (optional for inspection)
3. Access to multiple platform URLs

## Defense

Defensive measures and detection strategies:

- Invalidate caches on user interactions or use short TTLs for sensitive data
- Log access patterns to notification endpoints for unusual persistence
- Implement client-side validation of notification ownership

## Objectives

1. Confirm leak persistence post-refresh
2. Test across navigation to assess scope
3. Document evidence for impact assessment

## Instructions

### Step 1: Refresh Page

**Context**: Reload the notifications page to check if cache serves the same unauthorized data.

Press F5 or Ctrl+R in the browser.

> If notifications remain, the cache key issue prevents proper invalidation.

### Step 2: Navigate URLs

**Context**: Change to other sections (e.g., reports or dashboard) and return to notifications.

Use browser navigation to switch URLs and revisit the feed.

> Persistence across URLs indicates broad cache contamination.

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
- [[persistence-testing]]
- [[web-vulnerability]]
