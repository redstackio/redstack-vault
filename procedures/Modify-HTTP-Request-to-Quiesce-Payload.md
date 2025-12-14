---
id: proc-modify-quiesce-001
tags:
  - dos
  - payload
  - modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:32:38.706Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Modify-HTTP-Request-to-Quiesce-Payload

## Summary

This procedure modifies a captured HTTP GET request to a PUT method with a JSON payload that sets the application state to 'quiesce', exploiting the lack of authorization to trigger a DoS condition.

## Description

Targeting endpoints like https://dss.api.playstation.com/api/application/state in the PlayStation REST API, this involves altering the request in Burp Repeater to include the necessary headers and body. No authentication is required due to the vulnerability, leading to application shutdown and 502 errors. Prerequisites include a captured request from prior interception.

## Requirements

1. Captured GET request in Burp Repeater
2. Knowledge of the target endpoint and quiesce payload format
3. Burp Suite Repeater tab active

## Defense

Defensive measures and detection strategies:

- Require API keys or JWT tokens for state-modifying endpoints
- Rate-limit PUT requests to sensitive paths
- Log and alert on unexpected method changes or quiesce invocations

## Objectives

1. Craft an unauthenticated PUT request with quiesce state
2. Ensure payload validity for server acceptance
3. Prepare for transmission to induce outage

## Instructions

### Step 1: Update Method and Headers

**Context**: Change the request type and add JSON support to mimic a legitimate state update.

In Repeater, edit the first line to: PUT /api/application/state HTTP/1.1. Add header: Content-Type: application/json. Burp will auto-add Content-Length.

> This transforms the request into a state-changing operation without auth.

### Step 2: Insert Quiesce Payload

**Context**: Add the JSON body to set the app state to quiesce.

In the request body section, enter: {"appState":"quiesce"}

> Validates as JSON and targets the vulnerable state parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- dos
- payload
- modification
