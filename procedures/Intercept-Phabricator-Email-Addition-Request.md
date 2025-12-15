---
id: intercept-request-uuid
name: Intercept-Phabricator-Email-Addition-Request
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.836Z'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Adversary-in-the-Middle]]'
sub_techniques:
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
tags:
  - request-interception
  - proxy
  - phabricator
commands: []
platforms:
  - Web
tools:
  - '[[tools/SandroProxy]]'
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---

# Intercept-Phabricator-Email-Addition-Request

## Summary

This procedure captures the HTTP POST request sent when adding an email in Phabricator, including critical session cookies and CSRF tokens, using a mobile proxy tool.

## Description

The email addition form submits a POST to `/settings/user/(username)/page/email/` with parameters like `csrf`, `email`, and `submit`. Intercepting this allows modification for injection attacks. Target mobile traffic on Android for realism. Prerequisites: Proxy configured on the device, active session.

## Requirements

1. SandroProxy.apk installed and running on Android device
2. Proxy configured to capture all HTTP/HTTPS traffic (install CA certificate)
3. Victim's session active in browser

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS with HSTS to complicate interception
- Detect proxy usage via inconsistent TLS fingerprints

## Objectives

1. Capture the full request details
2. Extract session and CSRF tokens
3. Prepare for replay

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception.

Launch SandroProxy and enable capture for all requests.

> Expected output: Proxy listening on local port.

### Step 2: Submit Form

**Context**: Trigger the request.

In the browser, fill email form with placeholder and submit.

> Expected output: Request paused in proxy interface.

### Step 3: Inspect Request

**Context**: Analyze captured data.

View headers (e.g., `X-Phabricator-Csrf`, `Cookie`) and body (e.g., `email=test@example.com`).

> Expected output: Full request logged for editing.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques

- [[LLMNR-NBT-NS Poisoning and SMB Relay]] LLMNR/NBT-NS Poisoning and Relay (adapted for proxy MITM)

## Commands Used

None

## Tools Used

- [[tools/SandroProxy]]

## Tags

- [[request-interception]]
- [[proxy]]
- [[phabricator]]
