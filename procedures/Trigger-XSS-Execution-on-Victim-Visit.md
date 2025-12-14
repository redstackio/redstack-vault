---
tags:
  - xss-execution
  - javascript
  - api-abuse
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/stored-xss-alert-payload]]'
  - '[[commands/stored-xss-delete-site-payload]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: low
impact_level: high
detection_risk: high
sub_techniques: []
id: 76b8c4af-de66-4217-930b-c373be761f7e
created_at: '2025-12-13T23:52:55.357Z'
updated_at: '2025-12-13T23:52:55.357Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-on-Victim-Visit

## Summary

Wait for or induce the victim to visit the affected goal page, triggering the stored XSS payload to execute arbitrary JavaScript in their browser.

## Description

Once injected, the payload renders unsanitized in the Title field. Victim's visit to the page (e.g., checking goals) executes the JS, potentially alerting, stealing sessions, or calling APIs like DELETE /api/v6/site/everything with credentials.

## Requirements

1. Injected payload in victim's goal page
2. Victim's login and navigation to page
3. No additional attacker action post-injection

## Defense

Defensive measures and detection strategies:

- Output encoding for user-generated content
- JS error monitoring for onerror triggers
- API rate limiting and audit for destructive calls

## Objectives

1. Execute payload in victim context
2. Achieve impact like site deletion
3. Validate full chain success

## Instructions

### Step 1: Ensure Victim Access

**Context**: Payload awaits rendering.

**Instructions**: Revoke shared access if needed; wait for victim to log in.

**Expected Output**: Victim unaffected until visit.

### Step 2: Observe Execution

**Context**: Payload triggers on load.

**Command** ([[commands/stored-xss-alert-payload]]):
```javascript
"><img src=x onerror=alert()>
```

> Victim sees alert popup on page load.

### Step 3: Confirm Destructive Impact

**Context**: Advanced payload executes API call.

**Command** ([[commands/stored-xss-delete-site-payload]]):
```javascript
<script>eval(atob("..."))</script>
```

> Monitors for successful DELETE response; site data removed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/stored-xss-alert-payload]]
- [[commands/stored-xss-delete-site-payload]]

## Tools Used


## Tags

- [[trigger]]
- [[Execution]]
