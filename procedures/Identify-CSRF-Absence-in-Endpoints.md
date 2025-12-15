---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - csrf
  - web
  - php
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:50.164Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-CSRF-Absence-in-Endpoints

## Summary

This procedure examines network requests from account settings actions to confirm the absence of CSRF tokens, highlighting reliance on session cookies and sequential user IDs for protection.

## Description

CSRF vulnerabilities arise when state-changing POST requests lack unique tokens to verify request origin. In Atavist Magazine, endpoints for email changes, credit card deletions, and subscription cancellations use POST methods without such protections. The attack scenario involves an authenticated user tricked into submitting forged requests. Prerequisites include an active session from the prior account creation. Outcomes reveal exploitable endpoints like /cms/ajax/cancel_subscription.php.

## Requirements

1. Active authenticated session from account creation.
2. Browser developer tools or proxy like Burp Suite for request inspection.
3. Knowledge of HTTP request structures.

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all state-changing endpoints.
- Log and alert on requests missing expected tokens or from unusual referers.

## Objectives

1. Capture and analyze sensitive POST requests.
2. Verify lack of anti-CSRF measures.
3. Document vulnerable parameters like user IDs.

## Instructions

### Step 1: Trigger Sensitive Actions

**Context**: Generate traffic by performing actions in settings.

Change email address in settings form and submit. Monitor Network tab for the POST request.

**Expected Output**: Request to /cms/ajax/change_email.php with parameters like user_id=123&new_email=attacker@example.com.

### Step 2: Inspect for CSRF Tokens

**Context**: Check headers and body for protection mechanisms.

Examine the request: Look for X-CSRF-Token header or hidden form fields. Repeat for credit card deletion (/cms/ajax/delete_credit_card.php) and subscription cancel.

**Expected Output**: No tokens present; only Cookie: session_id and user_id parameter.

### Step 3: Note Identification Weaknesses

**Context**: Identify reliance on predictable IDs.

Observe sequential user IDs (e.g., user_id=456) in requests, which can be guessed or enumerated.

**Expected Output**: Confirmation of weak session validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[php]]
