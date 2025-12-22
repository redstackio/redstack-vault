---
tags:
  - csrf
  - form-submission
  - unauthorized-add
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:22.449Z'
sub_techniques: []
id: 0ef49ff6-473a-425a-85eb-1256c2c4f37f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Execute-CSRF-Form-Submission

## Summary

This procedure executes the CSRF attack by submitting a forged form to the delight.im add movie/series endpoint, adding unauthorized content to the victim's account using their session.

## Description

The delight.im add functionality lacks CSRF protection, allowing POST requests without token validation. When the malicious page loads, JavaScript submits the form with the victim's cookies, mimicking a legitimate action and resulting in state change without consent.

## Requirements

1. Active victim session in browser
2. Loaded malicious HTML PoC from previous procedure
3. Valid form parameters (name, year, string) for the endpoint

## Defense

Defensive measures and detection strategies:

- Validate CSRF tokens on all POST endpoints
- Use SameSite cookies to prevent cross-site requests
- Rate-limit additions to detect anomalous activity
- Alert users on unexpected library changes

## Objectives

1. Forge and submit the state-changing request
2. Confirm unauthorized addition succeeds
3. Demonstrate impact of missing CSRF controls

## Instructions

### Step 1: Load Malicious Page in Victim Browser

**Context**: Ensure the PoC page is visited while authenticated.

Victim opens the hosted URL (e.g., http://attacker.com/movie.html) in their browser logged into delight.im.

> Page loads silently; JavaScript triggers form submit immediately.

### Step 2: Monitor Form Submission

**Context**: Verify the POST request is sent to the vulnerable endpoint.

Use browser dev tools (Network tab) to observe the request.

> Request details: POST https://delight.im/add-movie with body {name: "Malicious Movie", year: "2023", string: "tt1234567"}, including session cookies.

### Step 3: Validate Addition

**Context**: Check the victim's account for the added content.

Refresh the delight.im library or profile page.

> Expected: New movie/series appears without user initiation, confirming successful exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- form-exploit
- session-hijack
