---
id: proc-inject-twitter-xss
tags:
  - xss
  - stored-xss
  - javascript
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.368Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Scheduled-Tweet

## Summary

This procedure exploits insufficient input sanitization in the Twitter Ads tweet composition field by injecting a malicious JavaScript payload into a scheduled tweet, leading to stored XSS that executes when the tweet is rendered for other users.

## Description

The vulnerability allows unsanitized user input in the compose tweet field to be stored and later rendered without proper escaping on the tweets page. By using a payload like `'><svg/onload=prompt(123);>'`, the attacker injects HTML/JavaScript that triggers on page load for viewers with access to the ad account. This is particularly effective for scheduled tweets, as the payload persists until the schedule time or deletion. Prerequisites include access to the tweets page; outcomes include arbitrary JS execution in victim browsers, such as alerting or stealing session cookies.

## Requirements

1. Access to the ad account's tweets page.
2. Permissions to compose and schedule tweets.
3. Knowledge of basic XSS payloads.

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in tweet storage and rendering (e.g., using HTML entity encoding).
- Implement Content Security Policy (CSP) to restrict inline script execution.
- Monitor for anomalous tweet content containing script tags or event handlers.

## Objectives

1. Bypass input validation to store executable JavaScript.
2. Achieve persistent XSS affecting multiple authorized users.
3. Enable client-side attacks like session theft upon rendering.

## Instructions

### Step 1: Open Compose Tweet Interface

**Context**: Initiate the composition to access the vulnerable input field.

On the tweets page (https://ads.twitter.com/accounts/{account_id}/tweets), click the 'Compose Tweet' button to open the dialog.

> The text input field appears, ready for content entry.

### Step 2: Enter Malicious Payload

**Context**: Inject the XSS payload to exploit lack of sanitization.

In the tweet text field, enter: `'><svg/onload=prompt(123);>'`. This closes any open tags and injects an SVG element that executes JS on load.

> The payload is accepted without validation errors; no immediate execution occurs.

### Step 3: Schedule the Tweet for Storage

**Context**: Store the payload persistently by scheduling rather than posting immediately.

Select 'Schedule tweet' in the dialog, set a future time (e.g., current time + 5 minutes), and click 'Tweet now' to schedule.

> A confirmation appears, and the tweet shows in the scheduled list with the payload stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- twitter-ads
