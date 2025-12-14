---
id: proc-37signals-capture-code-001
tags:
  - oauth2
  - code-capture
  - redirect
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:30:07.305Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Capture-Authorization-Code-from-Redirect

## Summary

This procedure involves intercepting the authorization code sent via redirect after the CSRF submission succeeds.

## Description

Following the POST to /authorization.json, the endpoint redirects to the specified redirect_uri with ?code= appended. The attacker hosts a server at this URI to log the code for the next step.

## Requirements

1. Control over redirect_uri
2. Web server to handle GET requests
3. Monitoring for incoming redirects

## Defense

Defensive measures and detection strategies:

- Validate redirect URIs strictly against registered values
- Log all authorization redirects
- Rate-limit authorization attempts

## Objectives

1. Receive the temporary authorization code
2. Log it for token exchange
3. Confirm exploitation success

## Instructions

### Step 1: Set Up Redirect Listener

**Context**: Host a simple endpoint to capture the query param.

Use a tool like ngrok or a local server to expose https://attacker.com/callback, logging GET requests.

**Expected Output**: Access log showing /callback?code=abc123.

### Step 2: Extract Code

**Context**: Parse the redirect URL.

From logs, extract the code value.

**Expected Output**: Isolated code string, e.g., 'abc123'.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth2
- code-capture
