---
tags:
  - xss
  - social-engineering
  - authorization
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.741Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 51f09344-7a10-4d9c-b487-c46572964b2f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Send-Authorization-Request-to-Victim

## Summary

This procedure sends an authorization request from the attacker's account to a target victim, embedding the stored XSS payload in the username for reflection upon victim interaction.

## Description

After injecting the payload, the attacker uses the Mobile Vikings authorization feature to request access or sharing with the victim (e.g., User B). This action stores the request with the malicious username and notifies the victim via email, including a link to the requests page. No sanitization occurs, allowing the payload to propagate. Prerequisites: Attacker account with payload set; victim's identifier (email/username). Outcomes: Request queued, victim lured to interact.

## Requirements

1. Attacker account with injected XSS payload
2. Victim's username or email
3. Access to authorization request interface

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected user data in notifications and request UIs
- Rate-limit authorization requests to prevent abuse
- Log and alert on suspicious request patterns (e.g., high volume from one user)

## Objectives

1. Dispatch authorization request with embedded payload
2. Trigger victim notification
3. Set up reflection points

## Instructions

### Step 1: Navigate to Authorization Feature

**Context**: Locate the tool for sending requests.

Log in as attacker and go to the account or sharing section where authorization requests are initiated.

### Step 2: Target the Victim

**Context**: Specify the victim to receive the request.

Enter the victim's username (User B) or email and submit the authorization request.

> The system processes the request, associating the attacker's malicious username.

### Step 3: Confirm Dispatch

**Context**: Verify the request was sent.

Check for a success message or sent requests log; victim should receive an email with a link to https://mobilevikings.com/account/requests/.

**Expected Output**: Confirmation UI or email log entry.

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
- [[authorization]]
- [[web]]
