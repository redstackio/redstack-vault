---
id: proc-003
tags:
  - mattermost
  - request-capture
  - burp-suite
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:07.521Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Capture Legitimate Post Request with Burp Suite

## Summary

This procedure intercepts a valid HTTP POST request for posting a message in a Mattermost channel while permissions are granted, using Burp Suite to store it for later replay in escalation attacks.

## Description

With Burp Suite proxying traffic, a user posts a message in the target channel, capturing the request to the API endpoint (e.g., /api/v4/posts). This exploits the fact that initial requests are authorized via session tokens. Target: Mattermost web app. Outcome: Reusable request demonstrating the vulnerability.

## Requirements

1. Burp Suite installed and configured as browser proxy
2. Active session in target channel with posting permissions
3. Knowledge of Mattermost API endpoints

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens and rate limiting on POST endpoints
- Log and alert on repeated or anomalous API calls
- Use short-lived session tokens with permission scoping

## Objectives

1. Post a legitimate message
2. Intercept and save the HTTP request
3. Enable replay for bypass testing

## Instructions

### Step 1: Configure Proxy and Post Message

**Context**: Set up interception for channel posts.

**Instructions**: In Burp Suite, enable Proxy > Intercept, post 'has permission to comment in channel' in 'mikefourchannel' via UI, capture the POST to /api/v4/posts in Intercept tab.

> Request includes channel ID, message payload, and auth headers.

### Step 2: Forward to Repeater

**Context**: Store for replay.

**Instructions**: Forward the captured request to Repeater, inspect payload (e.g., JSON with "message": "...", "channel_id": "...").

> Request ready for modification and replay.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[mattermost]]
- [[request-capture]]
- [[tools/Burp-Suite]]
