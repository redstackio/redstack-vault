---
tags:
  - session-cookie-leak
  - credential-theft
type: procedure
tools:
  - '[[tools/cURL]]'
  - '[[tools/Browser-Console]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-with-session-cookie]]'
platforms:
  - Web
techniques:
  - '[[Steal Web Session Cookie]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 11917e6b-b0e5-4a1c-b95c-ec60b92a4bd6
created_at: '2025-12-11T06:10:40.572Z'
updated_at: '2025-12-11T06:10:40.572Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0006]]'
mitre_techniques:
  - '[[T1539]]'
---
# Discover Leaked Session Cookie in Report

## Summary

This procedure involves reviewing bug bounty report comments to identify accidentally leaked session cookies from pasted cURL commands or browser console output, enabling potential credential theft.

## Description

In bug bounty platforms like HackerOne, analysts may inadvertently paste sensitive data like session cookies while reproducing vulnerabilities. This procedure guides discovering such leaks by inspecting report responses for unredacted HTTP request details, targeting web-based platforms without IP-bound sessions.

## Requirements

1. Access to the bug bounty platform and relevant reports
2. Basic web browsing tools
3. No special network access beyond standard HTTP/HTTPS

## Defense

Defensive measures and detection strategies:

- Implement automatic redaction of sensitive data in report comments
- Monitor for unusual access patterns post-comment posting

## Objectives

1. Identify leaked session cookies
2. Extract usable credential data
3. Prepare for impersonation

## Instructions

### Step 1: Review Report Comments

**Context**: Scan the report for analyst responses containing code snippets.

Inspect comments for copied cURL commands or console logs that include 'Cookie' headers.

> Look for patterns like 'Cookie: session=eyJ...' and note the value.

### Step 2: Validate Leak

**Context**: Confirm the leaked data is a valid session cookie.

Test the cookie in a private browser session to see if it grants access.

> Ensure no malicious use during validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Browser-Console]]

## Tags

- [[commands/curl-with-session-cookie]]
- [[credential-theft]]
