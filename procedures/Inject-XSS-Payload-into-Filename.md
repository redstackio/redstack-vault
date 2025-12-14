---
tags:
  - xss
  - payload-injection
  - filename-modify
type: procedure
tools:
  - '[[tools/LiveHTTPHeaders]]'
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
updated_at: '2025-12-14T03:15:41.577Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 472fd045-2ffe-4cd4-880c-04edf8519c57
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into Filename

## Summary

This procedure modifies the filename parameter in a captured HTTP file upload request to include a JavaScript XSS payload, exploiting improper escaping in the server's JSON error response for code injection.

## Description

Targeting vulnerabilities in web file upload handlers like Udemy's, this step crafts a reflected XSS by embedding HTML/JS breakers and a script tag in the filename. The payload `'><img src=x onerror=alert(1)>` breaks out of JSON strings and executes on reflection. Prerequisites include a captured request from the previous step. Outcome: A tampered request poised to trigger XSS upon replay.

## Requirements

1. Captured HTTP request from LiveHTTPHeaders
2. Knowledge of the filename parameter's position in multipart data
3. Basic understanding of XSS payloads for JSON contexts

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in error responses, especially filenames
- Use JSON encoders to prevent breakout attacks
- Log and alert on anomalous filename characters like < > "

## Objectives

1. Embed a functional XSS payload in the filename
2. Preserve request integrity for successful replay
3. Ensure payload evasion of basic filters

## Instructions

### Step 1: Locate and Edit Filename

**Context**: Access the editable request body to target the specific parameter.

**Instructions**: In LiveHTTPHeaders, select the captured POST request, navigate to the body section, and find the line with `filename="original_name"`. Replace the value with `'><img src=x onerror=alert(1)>`.

> This injects the payload to close any quoting and inject <img> tag for JS execution.

### Step 2: Validate Modification

**Context**: Confirm the change without altering other parts.

**Instructions**: Review the full request body to ensure the Content-Type and other fields remain unchanged, then prepare to resume.

> Expected: Payload visible in filename, request syntax valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/LiveHTTPHeaders]]

## Tags

- [[xss]]
- [[payload-injection]]
