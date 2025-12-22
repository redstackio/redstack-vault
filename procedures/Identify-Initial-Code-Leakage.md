---
id: uuid-identify-leak
tags:
  - leakage
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:35.857Z'
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
# Identify-Initial-Code-Leakage

## Summary

This procedure detects minor OAuth code exposure to third-party services like Google Fonts during the verification phase on edoverflow.com.

## Description

During OAuth code verification on comments widget pages, requests to external resources such as Google Fonts include the code in the URL, resulting in a 200 OK response and potential leakage. This step uses browser tools to inspect and confirm the issue in a web-based OAuth setup.

## Requirements

1. Browser with Network inspector
2. Target page with OAuth flow
3. GitHub account for testing

## Defense

Defensive measures and detection strategies:

- Strip sensitive params before external requests
- Use rel=noreferrer on all links

## Objectives

1. Confirm leakage to fonts.googleapis.com
2. Assess initial exposure risk
3. Inform manipulation strategy

## Instructions

### Step 1: Initiate Verification

**Context**: Trigger code verification after auth.

**Command** (Browser Action):

Complete OAuth on widget page and monitor requests.

> Look for https://fonts.googleapis.com/css?family=Inconsolata with code in query.

### Step 2: Validate Response

**Context**: Check if service responds, confirming access.

**Command** (Inspect Response):

Verify 200 OK in Network tab.

> Indicates code reachable by third-party.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- leakage
- google-fonts
