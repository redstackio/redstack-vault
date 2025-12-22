---
tags:
  - request-modification
  - http-post
  - sentry
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:18.301Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6b443cf7-6d76-4142-a0f7-686da151cc6f
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Request-to-Trigger-Disclosure

## Summary

This procedure modifies an intercepted GET request to the Sentry /api/20/store endpoint into a POST request with specific headers to bypass normal behavior and elicit a response containing sensitive data.

## Description

Misconfigured Sentry instances may process POST requests to the store endpoint without validation, leading to information disclosure. Using Burp Repeater, the attacker alters the method and headers to simulate an error event submission. This targets unauthenticated access, revealing server internals upon response. Prerequisites: Identified endpoint from prior steps.

## Requirements

1. Burp Repeater with captured GET request to /api/20/store
2. Knowledge of required headers for POST simulation
3. Target endpoint confirmed accessible

## Defense

Defensive measures and detection strategies:

- Validate HTTP methods on internal endpoints (e.g., reject POST if unintended)
- Implement rate limiting on API paths
- Sanitize responses to remove debug info in error trackers

## Objectives

1. Convert GET to POST to trigger store functionality
2. Add headers mimicking legitimate error submission
3. Obtain raw response for rendering

## Instructions

### Step 1: Copy Request to Repeater

**Context**: Prepare the base request for modification.

In Burp Proxy, right-click the intercepted request to /api/20/store and send to Repeater.

> Request loaded in Repeater tab for editing.

### Step 2: Change Method and Headers

**Context**: Alter to POST and set headers to evade filters.

Edit the raw request: Change 'GET' to 'POST'. Add/update headers: Host: target.com, Content-Type: application/x-www-form-urlencoded, Content-Length: 0, Sec-Fetch-Site: same-origin, Sec-Fetch-Mode: cors, Sec-Fetch-Dest: empty, Accept: */*, Accept-Language: en-US,en;q=0.5, Accept-Encoding: gzip, deflate, br. Set body empty.

> Modified request ready; headers simulate browser POST.

### Step 3: Send Modified Request

**Context**: Execute to receive the exploitable response.

Click 'Send' in Repeater.

> HTTP 200 response with unsanitized data.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[modification]]
- [[exploit]]
- [[http]]
