---
id: proc-imgur-intercept-request-93154
tags:
  - csrf
  - web
  - interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:03.368Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept Report Submission Request

## Summary

This procedure captures the POST request for abuse reporting on Imgur using an intercepting proxy, revealing the 'Sid' token used for CSRF protection.

## Description

During CSRF testing, configure a proxy like Burp Suite to intercept traffic, then submit the report form to capture the request. The request targets the meme abuse endpoint and includes session-bound tokens. This step is crucial for analyzing and modifying the request in a web-based attack on Imgur's platform. Prerequisites include proxy setup and authentication; outcome is a paused request ready for tampering.

## Requirements

1. Intercepting proxy tool installed and running (e.g., Burp Suite).
2. Browser proxy settings configured to route through the tool (e.g., 127.0.0.1:8080).
3. Active Imgur session.

## Defense

Defensive measures and detection strategies:

- Log all intercepted or modified requests at the proxy level.
- Enforce HTTPS to encrypt traffic and complicate interception.
- Detect proxy usage via timing anomalies or user-agent inconsistencies.

## Objectives

1. Capture the full POST request structure.
2. Identify CSRF tokens like 'Sid' in the body.
3. Pause execution for modification without server interaction.

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception before submission.

Launch Burp Suite and enable intercept mode in the Proxy tab.

> Browser traffic now routes through the proxy; confirm by visiting a test site.

### Step 2: Submit and Intercept

**Context**: Trigger the request to capture it.

Click 'Report' in the dialog; the tool will pause the POST request.

> Inspect the request: Look for POST to /report endpoint with 'Sid' parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web]]
- [[interception]]
