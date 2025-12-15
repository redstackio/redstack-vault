---
tags:
  - access-bypass
  - web
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 431a55e0-0265-40ad-a4f7-2cfb4512fcd1
created_at: '2025-12-14T17:30:07.257Z'
updated_at: '2025-12-14T17:30:07.257Z'
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Created-Blog-URL-with-New-Account

## Summary

Use the new ineligible account's session to access the blog URL created via the bypassed request, confirming draft visibility.

## Description

After the modified request succeeds, the server creates a draft under the new account. Accessing the Location header URL with the correct session allows viewing without further checks, exploiting the incomplete validation.

## Requirements

1. Location URL from previous response
2. Browser logged in as new account
3. No proxy interference

## Defense

Defensive measures and detection strategies:

- Ensure all blog accesses require full eligibility re-check
- Audit creation logs against access logs for anomalies
- Use short-lived drafts with expiration

## Objectives

1. Load the unauthorized draft
2. Verify association with new account
3. Prepare for editing

## Instructions

### Step 1: Copy Blog URL

**Context**: Extract the redirect target.

From the 302 response in Burp, copy the Location header value (e.g., https://lichess.org/blog/my-unauthorized-post).

### Step 2: Navigate and View

**Context**: Access with new session to confirm control.

In a clean browser session logged in as the new account, paste and visit the URL.

**Expected Output**: Draft blog page loads, showing the original intercepted content.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access-bypass]]
- [[web]]
