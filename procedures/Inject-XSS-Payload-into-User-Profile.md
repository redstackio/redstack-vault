---
tags:
  - xss
  - injection
  - profile-modification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a81d1876-b363-4152-a09a-e64d3dc3738b
created_at: '2025-12-14T03:15:27.005Z'
updated_at: '2025-12-14T03:15:27.005Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-User-Profile

## Summary

This procedure involves modifying a user's profile on Udemy to inject a malicious XSS payload into the firstname field, enabling it to be reflected in search results for subsequent exploitation.

## Description

In the context of Udemy's autocomplete search vulnerability, user-supplied data like the firstname is not properly sanitized when included in search responses. By setting the firstname to a payload such as `"><img src=>`, an attacker can store the injection point. When another user searches for terms matching this username, the payload reflects in the JSON response, executing JavaScript in the viewer's browser. This step requires an authenticated Udemy account and targets the profile edit functionality.

## Requirements

1. Valid Udemy account with profile edit permissions
2. Web browser access to https://www.udemy.com
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding for all user profile fields
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor profile changes for suspicious patterns like script tags

## Objectives

1. Persist XSS payload in user profile data
2. Prepare for reflection in search autocomplete
3. Enable client-side JavaScript execution on trigger

## Instructions

### Step 1: Access Profile Settings

**Context**: Log in and navigate to the account profile to locate the firstname edit field.

Go to https://www.udemy.com/user/edit-account/ and find the firstname input.

### Step 2: Inject and Save Payload

**Context**: Enter the XSS payload to break out of any context and inject HTML/JS.

Set the firstname to: `"><img src=>` (or extend to `<script>alert(1)</script>` for testing).

Click save to update the profile.

> The profile updates without error, storing the payload for search indexing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[injection]]
