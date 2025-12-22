---
tags:
  - session-cookie
  - web-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Man in the Browser]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 206d53a3-325c-4f94-8542-0a97ebbcc174
created_at: '2025-12-13T23:56:20.326Z'
updated_at: '2025-12-13T23:56:20.326Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Man in the Browser]]'
---
# Obtain Initial Session Cookie

## Summary

This procedure involves accessing a public documentation page on uber.readme.io to obtain an initial connect.sid session cookie, which is necessary for subsequent authentication steps in web-based attacks.

## Description

By loading the deep-linking documentation page, the server sets a session cookie that can be used to authenticate a user session. This is a foundational step in attacks requiring authenticated access, such as injecting malicious content into editable features. The target environment is a web application powered by AngularJS, and the expected outcome is capturing a valid cookie for further requests.

## Requirements

1. Network access to https://uber.readme.io/docs/deep-linking.
2. Web browser or HTTP client capable of capturing cookies.
3. No prior credentials needed for this initial access.

## Defense

Defensive measures and detection strategies:

- Monitor for unusual access patterns to documentation pages.
- Implement strict session management and cookie security flags (e.g., HttpOnly, Secure).

## Objectives

1. Obtain a connect.sid cookie for session initiation.
2. Prepare for authentication without triggering alerts.
3. Enable access to authenticated endpoints.

## Instructions

### Step 1: Access Documentation Page

**Context**: Load the page to trigger cookie issuance.

Navigate to https://uber.readme.io/docs/deep-linking in a browser or use an HTTP GET request to receive the cookie in the response headers.

> This sets the initial session cookie without authentication.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Man in the Browser]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- session-cookie
- web-access
