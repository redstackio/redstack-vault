---
id: proc-brave-uri-nav-tor-001
tags:
  - brave
  - chrome-uri
  - tor
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
updated_at: '2025-12-14T17:24:56.300Z'
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
# Navigate-Privileged-URIs-Tor

## Summary

This procedure tests navigation to privileged chrome:// and brave:// URIs within Brave's Tor mode, revealing inconsistencies where some URIs load directly instead of being blocked or redirected for privacy.

## Description

Brave's Tor mode aims to isolate sensitive data, but manual testing shows that URIs like chrome://downloads load in the Tor context, unlike chrome://history which redirects. This targets Chromium-based Brave (93.0.4577.82), demonstrating potential for data leakage. Prerequisites include an active Tor window; outcomes confirm accessible URIs for further exploitation.

## Requirements

1. Active Brave Tor window from prior procedure
2. Knowledge of target URIs (e.g., chrome://downloads)
3. Local browser access

## Defense

Defensive measures and detection strategies:

- Patch Brave to consistent URI blocking in private modes
- Use content policies to restrict chrome:// access in Tor
- Log and alert on privileged URI navigations in isolated sessions

## Objectives

1. Identify accessible privileged URIs in Tor
2. Highlight privacy protection gaps
3. Set up for download history viewing

## Instructions

### Step 1: Enter URI in Address Bar

**Context**: Directly input a privileged URI to test loading behavior.

No command; UI action:

- In Tor window address bar, type `chrome://downloads` and press Enter.
- Repeat for `brave://inspect/#devices` and `brave://device-log/`.

> Expected: chrome://downloads loads; others may load or show partial access. Compare to `chrome://history`, which should redirect.

### Step 2: Observe Behavior

**Context**: Note differences in URI handling to confirm inconsistency.

No command; manual verification:

- Check if page content displays without redirect to normal browser.

> Successful: Direct access to URI content in Tor session, indicating leak potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[uri-navigation]]
- [[privileged-uri]]
- [[disclosure]]
