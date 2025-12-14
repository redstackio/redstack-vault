---
id: proc-brave-leak-downloads-001
tags:
  - brave
  - tor
  - disclosure
  - downloads
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web Browser
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:24:56.281Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# View-Leaked-Downloads-Tor

## Summary

This procedure accesses the chrome://downloads page in Brave's Tor mode to view and disclose download history from normal sessions, exploiting inconsistent privacy controls.

## Description

Due to global inheritance of download history, Tor mode displays normal session data when accessing chrome://downloads. This affects Brave on Chromium, leading to information disclosure of file names and URLs. Requires prior download in normal mode; outcomes confirm leak with visible sensitive details.

## Requirements

1. Active Tor window
2. Prior download in normal session
3. Access to chrome://downloads URI

## Defense

Defensive measures and detection strategies:

- Implement URI-specific blocks in Tor mode extensions
- Use separate browser profiles for Tor vs. normal use
- Audit browser for cross-session data inheritance

## Objectives

1. Retrieve leaked download history in Tor
2. Expose file names and source URLs
3. Demonstrate privacy impact

## Instructions

### Step 1: Navigate to Downloads Page

**Context**: Enter the URI in Tor to load the potentially leaking page.

No command; UI action:

- In Tor window, type `chrome://downloads` in address bar and press Enter.

> Expected: Page loads without redirect, inheriting global history.

### Step 2: Inspect Leaked Entries

**Context**: Review the displayed data for normal session leaks.

No command; manual inspection:

- Scroll through the list to find recent downloads (e.g., .jnlp file).

> Successful: Entries show file names and originating URLs from normal browsing, confirming disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[leak]]
- [[chrome-downloads]]
- [[info-disclosure]]
