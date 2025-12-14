---
id: uuid-proc-2
name: Input-Invalid-Server-URI-to-Trigger-Error
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.550Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploitation for Client Execution]]'
sub_techniques: []
tags:
  - xss
  - nextcloud
  - invalid-uri
commands: []
platforms:
  - Windows
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---

# Input-Invalid-Server-URI-to-Trigger-Error

## Summary

This procedure involves entering an invalid server URI in the Nextcloud desktop client's login form to elicit an error response, exposing the XSS vulnerability in the unsanitized alert box.

## Description

By inputting a URI that results in an HTTP error (e.g., 403 Forbidden) from an attacker-controlled server, the client displays an alert box that renders the response body as HTML without sanitization. This step assumes proxy interception is set up and targets Windows environments where the client interprets HTML with elevated local zone permissions, enabling file:// protocol abuse.

## Requirements

1. Nextcloud client open at login form
2. Attacker-controlled server or MITM proxy (Burp) to handle the request
3. Network connectivity to the invalid URI endpoint

## Defense

Defensive measures and detection strategies:

- Sanitize all error message displays in client applications
- Implement content security policies to block file:// execution

## Objectives

1. Trigger the vulnerable error alert box
2. Ensure response is controllable for payload injection
3. Validate error handling flaw without execution yet

## Instructions

### Step 1: Enter Invalid URI

**Context**: Input a URI designed to return an error, routing through the proxy.

In the server address field, type: http://attacker-site.com/invalid-path

> The client sends an HTTP request to the URI.

### Step 2: Receive Error Response

**Context**: Confirm the error triggers the alert box.

Ensure the server responds with 403 and a body containing placeholder text.

> Alert box pops up displaying the raw response, ready for HTML injection in the next step.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- nextcloud
- invalid-uri
