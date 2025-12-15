---
tags:
  - race-condition
  - 2fa-reset
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.387Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 173f6695-79e6-455a-9bf8-d007494ad86d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate Multiple Parallel 2FA Reset Requests

## Summary

This procedure involves sending concurrent requests to the 2FA reset endpoint to create multiple active reset processes, exploiting the absence of request synchronization in the HackerOne platform.

## Description

In the context of the HackerOne 2FA reset vulnerability, this step targets the reset process where concurrent requests are not properly locked or synchronized. By initiating multiple parallel POST requests to the reset endpoint, an attacker can queue several 24-hour reset timers simultaneously. This sets up the race condition for later exploitation. The target environment is a web application like HackerOne, requiring initial access to the account's email or login to trigger the resets. Expected outcomes include multiple notification emails, each confirming a separate reset request.

## Requirements

1. Access to the target's account email for receiving notifications
2. Ability to interact with the web interface or send HTTP requests (e.g., via browser or script)
3. Knowledge of the 2FA reset endpoint URL (typically under account settings)

## Defense

Defensive measures and detection strategies:

- Implement request deduplication or locking mechanisms (e.g., using Redis locks) for reset endpoints
- Rate-limit concurrent reset requests per user/IP
- Log and alert on multiple simultaneous reset initiations

## Objectives

1. Create multiple active 2FA reset processes to bypass single-request controls
2. Receive confirmations for each request to verify parallelism
3. Set the stage for race condition exploitation by leaving extra requests active

## Instructions

### Step 1: Prepare the Environment

**Context**: Log in to the target account or use an authenticated session to access the 2FA reset functionality. Identify the reset endpoint via browser inspection (e.g., Network tab in DevTools).

No specific command, but simulate with browser: Open multiple tabs or use console to send requests.

### Step 2: Send Concurrent Requests

**Context**: Use developer tools or a simple script to fire off 2-3 POST requests simultaneously to the endpoint, such as `/api/account/2fa/reset`, with parameters like user ID or email.

Example using browser console (inferred for actionability):

```javascript
// In browser console, repeat rapidly or use setTimeout for parallelism
fetch('/api/account/2fa/reset', {method: 'POST', credentials: 'include'}).then(r => r.json()).then(console.log);
```

> This sends a POST request; repeat 2-3 times quickly. Expected output: JSON response confirming reset initiation, and emails arriving.

### Step 3: Verify Multiple Notifications

**Context**: Check the email inbox associated with the account for multiple distinct reset notifications.

Monitor emails for unique reset codes or timers.

**Expected Output**: 2+ emails with 24-hour expiration notices.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- race-condition
- 2fa-reset
