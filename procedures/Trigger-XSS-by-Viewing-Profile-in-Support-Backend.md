---
id: p4d5e6f7-g8h9-0123-defg-4567890123
tags:
  - xss
  - execution
  - backend
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.788Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Viewing-Profile-in-Support-Backend

## Summary

This procedure authenticates to the Support Backend and views the affected user's profile, triggering the stored XSS payload in the rendered skill names for arbitrary JavaScript execution.

## Description

The vulnerability lies in lib/support/app/controllers/support/tables/columns/pentester_profile_skills.rb, where skill names are joined and inserted into HTML without sanitization, allowing script execution in title or span elements. In production, inline scripts may be blocked, but this demonstrates potential impact.

## Requirements

1. Support Backend access on port 8080
2. Valid support credentials
3. Profile with malicious skill assigned

## Defense

Defensive measures and detection strategies:

- Apply Content-Security-Policy to block inline scripts
- Sanitize outputs in view rendering
- Monitor for XSS payload executions in logs

## Objectives

1. Access Support Backend
2. Navigate to user profile
3. Execute injected JavaScript

## Instructions

### Step 1: Authenticate to Backend

**Context**: Sign in at http://localhost:8080/support.

Enter support credentials.

### Step 2: View User Profile

**Context**: Go to http://localhost:8080/support/users/hacker to render the profile.

The payload triggers on load.

**Expected Output**: JavaScript alert or execution in browser console.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
