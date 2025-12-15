---
id: proc-uuid-3
tags:
  - payload-injection
  - dos
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:55.787Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Inject-Large-Markdown-Payload-via-Interception

## Summary

This procedure intercepts and modifies a reply request to insert an excessively large Markdown payload, initiating resource exhaustion on the Discourse backend.

## Description

The attack targets the POST /t/:id/posts endpoint in Discourse, where large inputs (~800k chars) cause prolonged Markdown parsing. Scenario: Authenticated user submits oversized content. Outcomes: Server-side delay. Prerequisites: Proxy interception and payload file.

## Requirements

1. Burp Suite configured as proxy
2. Large payload file (e.g., from GitHub: https://github.com/theteatoast/theteatoast.github.io/blob/main/payload.txt)
3. Active session and topic access

## Defense

Defensive measures and detection strategies:

- Enforce input length limits (e.g., 65k chars max) on reply fields
- Implement request body size checks and early rejection

## Objectives

1. Replace reply content with large Markdown
2. Trigger excessive processing
3. Confirm payload delivery

## Instructions

### Step 1: Intercept Reply Request

**Context**: Start the reply submission to capture the base request.

Use browser with Burp proxy; click reply and type minimal text, then submit.

> Burp intercepts POST request. Expected: Request body with 'post[raw]' parameter.

### Step 2: Modify and Forward

**Context**: Inject the oversized payload to exploit the lack of validation.

In Burp Repeater, replace 'post[raw]' value with content from payload.txt (~800k chars).

> Forward the request. Expected: Server accepts but processes slowly.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- payload-injection
- dos
- web
