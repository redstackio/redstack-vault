---
tags:
  - idor
  - modification
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 9720353e-3f90-4c67-9c18-8c8172f34724
created_at: '2025-12-14T17:25:47.348Z'
updated_at: '2025-12-14T17:25:47.348Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Hacker-Username-Parameter

## Summary

This core exploitation procedure alters the hacker_username parameter in the intercepted POST request to target a different program participant, bypassing authorization checks.

## Description

Exploiting the IDOR, change hacker_username from the original (e.g., jong_jong) to the victim's (e.g., japzdivino) in the /hacker_reviews request. The root cause is separate checks for report and user authorization, allowing reviews for any participant. This targets HackerOne's web API. Forwarding the modified request posts the feedback to the wrong profile. Preconditions: victim in program, proxy intercept active.

## Requirements

1. Intercepted request in proxy
2. Knowledge of victim's username
3. Victim's participation in the program

## Defense

Defensive measures and detection strategies:

- Validate username matches report submitter ID server-side
- Log and alert on parameter mismatches in requests

## Objectives

1. Exploit IDOR to target unauthorized user
2. Forward request without validation failure
3. Trigger feedback posting and email

## Instructions

### Step 1: Edit Parameter in Proxy

**Context**: Locate and modify the vulnerable field.

In Burp Repeater or Interceptor, change hacker_username=jong_jong to hacker_username=japzdivino.

### Step 2: Forward Modified Request

**Context**: Send the altered request to the server.

Click 'Forward' or 'Send' to execute the POST.

**Expected Output**: Server accepts request (200 OK), no error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[modification]]
- [[web]]
