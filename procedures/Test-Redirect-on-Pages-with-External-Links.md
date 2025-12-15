---
id: uuid-test-external-links
tags:
  - external-links
  - noreferrer
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/github-oauth-manipulate-redirect-to-about]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:35.849Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Test-Redirect-on-Pages-with-External-Links

## Summary

This procedure tests redirect_uri manipulation on site pages containing insecure external links, setting up conditions for Referer-based code leakage.

## Description

Pages like /about/ and /metadata on edoverflow.com include links to external sites (e.g., keybase.io, twitter.com) without rel='noreferrer', allowing full URL with code to be sent in Referer headers upon click.

## Requirements

1. Knowledge of target page structure
2. Manipulated OAuth URL
3. Victim interaction simulation

## Defense

Defensive measures and detection strategies:

- Add rel='noreferrer' to all external <a> tags
- Monitor Referer logs on third-parties

## Objectives

1. Identify vulnerable pages with external links
2. Confirm code exposure risk on click
3. Prepare for full exploitation

## Instructions

### Step 1: Set Redirect to Vulnerable Page

**Context**: Target /about/ for links.

**Command** ([[commands/github-oauth-manipulate-redirect-to-about]]):
```bash
# Visit in browser
https://github.com/login?client_id=5f45cc999f7812d0b6d2&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D5f45cc999f7812d0b6d2%26redirect_uri%3Dhttps%253A%252F%252Fedoverflow.com%252Fabout%252f%26scope%3Dpublic_repo
```

> Redirects to /about/?code=...; inspect for links to keybase.io, etc.

### Step 2: Check Link Attributes

**Context**: Verify lack of noreferrer.

**Command** (DOM Inspection):

Use console: document.querySelectorAll('a[href^=http]')

> Expected: No rel='noreferrer' on external <a> tags.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

-

## Commands Used

- [[commands/github-oauth-manipulate-redirect-to-about]]

## Tools Used

-

## Tags

- external-links
- referer-leak
