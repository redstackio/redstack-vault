---
id: proc-send-verify-dos-001
tags:
  - dos
  - verification
  - impact
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Firefox-Developer-Tools]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:32:38.703Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Send-Modified-Request-and-Verify-DoS

## Summary

This procedure executes the modified PUT request to quiesce the application and verifies the resulting denial-of-service by observing error responses on API endpoints.

## Description

After payload modification, this sends the request to https://dss.api.playstation.com/api/application/state, causing the app to enter an unreachable state for over an hour. Verification involves re-accessing the endpoint or related paths to confirm 502 Bad Gateway errors, demonstrating the DoS impact without authentication.

## Requirements

1. Modified PUT request ready in Burp Repeater
2. Access to the target API for follow-up checks
3. Browser or tool for refreshing endpoints

## Defense

Defensive measures and detection strategies:

- Implement idempotency checks for state changes to prevent repeated quiesce
- Monitor application logs for unauthorized state transitions
- Use circuit breakers to isolate quiesce effects

## Objectives

1. Transmit the quiesce payload successfully
2. Observe immediate and sustained application unavailability
3. Confirm high-impact DoS

## Instructions

### Step 1: Transmit the Request

**Context**: Send the payload to trigger the state change.

In Burp Repeater, click Send to execute the PUT request.

> Server processes the request, quiescing the application if vulnerable.

### Step 2: Check for Errors

**Context**: Validate the DoS by attempting access to affected endpoints.

Refresh https://dss.api.playstation.com/api/application/state or visit https://dss.api.playstation.com/api/application.wadl. Expect 502 within 15 seconds.

> Repeated requests can extend outage; use Firefox Dev Tools Network tab for monitoring.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Firefox-Developer-Tools]]

## Tags

- dos
- verification
- impact
