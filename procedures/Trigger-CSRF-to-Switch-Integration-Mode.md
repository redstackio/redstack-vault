---
id: proc-trigger-csrf-switch
tags:
  - csrf
  - mode-switch
  - exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:42.925Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-CSRF-to-Switch-Integration-Mode

## Summary

This procedure executes the CSRF attack by having the admin's browser send the forged GET request to the Slack endpoint, switching the GitHub integration to unauthenticated mode and disabling functionality.

## Description

The lack of CSRF protection on the /services/{CODE}?no_auth_mode=1 endpoint allows the img src to trigger the change using the admin's session cookies. Target is Slack's web services. Prerequisites: Admin visit to malicious page. Expected outcome: Integration loses GitHub auth, disrupting notifications.

## Requirements

1. Admin visiting the hosted page
2. Valid URI with parameter
3. Admin's active Slack session

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens for all GET/POST to sensitive endpoints
- Rate-limit requests to integration URIs
- Alert on mode changes in integrations

## Objectives

1. Modify integration settings unauthorized
2. Switch to unauthenticated mode
3. Cause functional disruption

## Instructions

### Step 1: Load Malicious Page

**Context**: Admin accesses the page, triggering img fetch.

No specific command; browser automatically GETs the src URI.

> Request sent with admin's cookies, processed by Slack.

### Step 2: Confirm Trigger

**Context**: Observe if request succeeds.

No specific command; check Slack for confirmation (e.g., via screenshot or admin report).

> Endpoint responds with mode switch confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[exploit]]
