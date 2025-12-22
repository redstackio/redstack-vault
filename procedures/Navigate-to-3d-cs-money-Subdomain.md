---
tags:
  - subdomain-access
  - bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T05:32:10.084Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 7404fb4f-d15c-4367-8535-a99487f6de92
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Navigate-to-3d-cs-money-Subdomain

## Summary

This procedure accesses the 3d.cs.money subdomain using the partial session from the bypassed login, reaching features not protected by full authentication.

## Description

Following partial login, this step tests subdomain isolation flaws. It operates on the web platform and assumes a Steam-linked session. Outcomes include loading the subdomain without redirects to full auth.

## Requirements

1. Partial session active
2. Browser with JavaScript enabled
3. Network access to subdomains

## Defense

Defensive measures and detection strategies:

- Implement uniform auth checks across subdomains
- Monitor cross-subdomain navigation logs

## Objectives

1. Reach vulnerable subdomain
2. Confirm bypass extends to features
3. Avoid auth barriers

## Instructions

### Step 1: Enter Subdomain URL

**Context**: Directly target the isolated subdomain post-partial login.

In the browser address bar, enter https://3d.cs.money.

> Page should load without prompting for credentials.

### Step 2: Observe Loading Behavior

**Context**: Verify no enforcement of 2FA or login on subdomain.

Check for any auth modals; none should appear.

> Successful if interface elements (e.g., background viewer) are visible.

### Step 3: Test Persistence

**Context**: Ensure session holds during navigation.

Interact minimally with the page to confirm no logout or redirect.

> Stability indicates effective bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-access]]
- [[bypass]]
