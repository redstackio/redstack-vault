---
id: p4d5e6f7-g8h9-0123-defg-4567890123
tags:
  - api-testing
  - oauth
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:28:28.754Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-API-Connection-Attempt

## Summary

This procedure tests an initial API connection attempt post-cookie injection to observe the setup for DoS confirmation.

## Description

After cookie injection, attempting to connect via the 'Explore API' feature redirects to the authorization endpoint, which may still prompt but sets up for failure on refresh. Targets the OAuth apps page. Prerequisites: Injected cookies and created app. Expected: Authorization prompt without immediate block.

## Requirements

1. Malicious cookies set.
2. Access to https://www.tumblr.com/oauth/apps.
3. Created OAuth app.

## Defense

Defensive measures and detection strategies:

- Log failed authorization attempts.
- Alert on repeated connection failures.

## Objectives

1. Trigger OAuth authorization flow.
2. Observe redirect behavior.
3. Prepare for session refresh test.

## Instructions

### Step 1: Return to OAuth Apps

**Context**: Navigate back to the apps dashboard.

Visit https://www.tumblr.com/oauth/apps.

> List of apps displays.

### Step 2: Click Explore API

**Context**: Initiate connection to the app.

Select the created app and click 'Explore API'.

> Redirects to https://www.tumblr.com/oauth/authorize?oauth_token=*&source=console with auth prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- api-testing
- oauth
- web

