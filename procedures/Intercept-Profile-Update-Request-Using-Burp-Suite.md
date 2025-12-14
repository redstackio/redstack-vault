---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - intercept
  - burp-suite
  - request-capture
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
updated_at: '2025-12-14T17:33:12.268Z'
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
# Intercept-Profile-Update-Request-Using-Burp-Suite

## Summary

This procedure uses Burp Suite to capture the HTTP POST request generated when updating the profile, allowing analysis of vulnerable parameters.

## Description

With an authenticated session, trigger the profile update action on the account page at https://███████/signIn/account. Burp Suite intercepts the request, revealing the ID parameter and email field. This is crucial for identifying the IDOR flaw. Expected outcome is a modifiable request in Burp Repeater.

## Requirements

1. Burp Suite installed and proxy configured (e.g., browser proxy to 127.0.0.1:8080)
2. Authenticated session
3. Target account page accessible

## Defense

Defensive measures and detection strategies:

- HTTPS enforcement with HSTS
- Request signing or CSRF tokens
- Proxy detection via headers

## Objectives

1. Capture legitimate update request
2. Identify modifiable parameters
3. Prepare for parameter tampering

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception in Burp Suite.

Launch Burp Suite, enable Intercept in Proxy tab, and configure browser to use Burp as proxy.

> Expected output: Traffic routed through Burp.

### Step 2: Trigger and Intercept Request

**Context**: Click the update button to generate and capture the POST.

On the account page, click the 'update' button at the top middle.

> Expected output: Request paused in Burp with POST to update endpoint, showing ID and email params.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- interception
- proxy
- http-manipulation
