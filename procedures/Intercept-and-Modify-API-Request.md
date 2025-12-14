---
tags:
  - xss
  - api
  - interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 60b76b3d-9f7a-4abc-b7a8-050e0f2565db
created_at: '2025-12-14T00:11:16.422Z'
updated_at: '2025-12-14T00:11:16.422Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Intercept and Modify API Request

## Summary

This procedure uses a proxy tool to intercept and alter the API request for creating a scheduled post on Reddit, injecting a malicious JavaScript payload.

## Description

By intercepting the HTTP request with Burp Suite, the hyperlink in the request body is modified to use a 'javascript:' scheme, bypassing client-side filters. This allows the malicious link to be stored server-side. The expected outcome is a post with an executable JavaScript link.

## Requirements

1. Burp Suite or similar proxy tool installed
2. Browser configured to route traffic through the proxy
3. Knowledge of HTTP request structures

## Defense

Defensive measures and detection strategies:

- Enforce server-side filtering of URI schemes
- Log and alert on modified requests with suspicious payloads

## Objectives

1. Inject malicious payload into API request
2. Bypass validation checks
3. Store exploitable post on server

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to capture requests.

Launch Burp Suite and configure your browser to use it as a proxy (e.g., 127.0.0.1:8080).

### Step 2: Intercept Request and Inject Payload

**Context**: Modify the captured request.

When creating the post, intercept the request in Burp's Proxy tab. Edit the hyperlink field to 'javascript:alert(document.cookie)' and forward the request.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- api
- interception
