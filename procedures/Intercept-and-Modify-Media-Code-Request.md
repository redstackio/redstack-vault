---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - idor
  - request-modification
  - proxy-intercept
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.582Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Intercept-and-Modify-Media-Code-Request

## Summary

This procedure details intercepting HTTP requests during survey saves in Crowdsignal and modifying the media_code parameter to exploit the IDOR vulnerability, allowing reference to unauthorized media IDs.

## Description

The IDOR arises from insufficient ownership validation on the media_code parameter in POST requests to survey edit endpoints. By using a proxy like Burp Suite, attackers intercept the request, substitute the media_code with a 7-digit sequential ID from another user, and forward it. This works for questions, headers, footers, and polls, potentially exposing private media stored in S3-like services.

## Requirements

1. Configured proxy tool (e.g., Burp Suite) with browser integration
2. Active survey in edit mode
3. Knowledge of target victim's approximate media ID (guessed sequentially)

## Defense

Defensive measures and detection strategies:

- Server-side ownership checks on media_code against user/session
- Log and alert on anomalous media_code values in requests
- Use non-sequential, unpredictable IDs for media

## Objectives

1. Capture the baseline save request
2. Tamper with media_code to bypass access controls
3. Forward request to test unauthorized access

## Instructions

### Step 1: Set Up Proxy and Add Question

**Context**: Prepare interception by adding a survey element.

Add a 'Free Text' question in the survey editor and configure browser proxy to Burp (e.g., set proxy to 127.0.0.1:8080).

> Proxy captures all traffic; ensure intercept is on for POST requests.

### Step 2: Trigger Save and Intercept

**Context**: Generate the vulnerable request.

Edit the question and click Save to send POST to /surveys/:id/edit.

> Intercepted request shows JSON/form with media_code parameter.

### Step 3: Modify Parameter

**Context**: Exploit IDOR by changing the reference.

In Burp Repeater or Interceptor, edit media_code from original (e.g., own ID) to victim's 7-digit ID like '2013124'.

> Ensure request format remains valid (e.g., JSON: {"media_code": "2013124"}).

### Step 4: Forward and Observe

**Context**: Submit to server for exploitation.

Click Forward or Go in Burp to send the modified request.

> Server responds with 200 if successful, no ownership check.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[request-modification]]
