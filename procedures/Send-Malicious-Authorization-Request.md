---
id: proc-send-auth-request-mobilevikings
tags:
  - xss
  - authorization
  - propagation
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:35.694Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Send-Malicious-Authorization-Request

## Summary

This procedure uses the tainted user name to send an authorization request to a victim, embedding the stored XSS payload in the request data for later reflection.

## Description

The Mobile Vikings authorization feature allows users to request permissions from others. By sending a request from an account with a malicious user name, the payload is associated with the request and stored in the recipient's pending authorizations, setting up for XSS execution upon interaction.

## Requirements

1. Attacker account with injected XSS payload in user name
2. Knowledge of victim's email or account identifier
3. Access to the authorization request interface

## Defense

Defensive measures and detection strategies:

- Sanitize all user-generated data in authorization requests
- Rate-limit authorization requests to prevent abuse
- Alert on suspicious request patterns

## Objectives

1. Propagate the payload to the victim's account view
2. Ensure the request appears legitimate
3. Await victim interaction

## Instructions

### Step 1: Navigate to Authorization Section

**Context**: From the dashboard, locate the feature to request authorizations from other users.

Log in and go to the account management area.

### Step 2: Initiate Request to Victim

**Context**: Enter the victim's details to send the request, carrying the tainted user name.

Fill in the form with the victim's email and submit. The system will notify the victim.

### Step 3: Confirm Propagation

**Context**: If possible, verify the request is pending (requires victim-side access or social engineering).

Check for send confirmation and monitor for victim response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- authorization
