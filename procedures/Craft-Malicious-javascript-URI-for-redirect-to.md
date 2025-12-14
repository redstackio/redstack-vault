---
tags:
  - payload-crafting
  - xss
  - javascript-uri
type: procedure
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
updated_at: '2025-12-13T23:52:49.925Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 94d6e30a-075d-4b53-bfe8-e77b0404c5bd
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-javascript-URI-for-redirect-to

## Summary

This procedure details the creation of a malicious URL exploiting the redirect_to parameter in GoCD's loading page by embedding a javascript: URI to inject and prepare an XSS payload for execution.

## Description

Following source code review, craft a URL that appends ?redirect_to=javascript:alert("XSS") to the loading page endpoint. The payload leverages the query parsing in redirectToLanding, where locationData[2] captures the javascript: scheme, leading to execution upon decoding. This targets web browsers interacting with GoCD during startup, with outcomes including payload readiness for testing. Requires knowledge of URL encoding and JavaScript.

## Requirements

1. Target GoCD URL (e.g., http://target/loading/new.loading.page.html)
2. Text editor or browser URL bar for construction
3. Understanding of javascript: protocol

## Defense

Defensive measures and detection strategies:

- Sanitize query parameters to strip or block javascript: schemes
- Employ URL allowlisting for redirects
- Log and alert on suspicious parameter values

## Objectives

1. Generate a functional XSS payload URL
2. Ensure compatibility with the vulnerable parsing logic
3. Prepare for safe testing in a controlled environment

## Instructions

### Step 1: Identify Base URL

**Context**: Start with the vulnerable endpoint.

Use the GoCD loading page URL: http://target-gocd/loading/new.loading.page.html.

**Expected Output**: Base URL ready for parameter append.

### Step 2: Append Malicious Parameter

**Context**: Construct the query string with javascript: payload.

Add ?redirect_to=javascript:alert("XSS"). No additional encoding needed as the function decodes it directly.

**Expected Output**: Full URL: http://target-gocd/loading/new.loading.page.html?redirect_to=javascript:alert("XSS").

### Step 3: Verify Payload Syntax

**Context**: Check for parsing issues.

Ensure the alert payload is properly quoted and the scheme is lowercase javascript: to match execution.

**Expected Output**: Validated payload that will trigger window.location assignment to the JS URI.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- payload-crafting
- xss
- javascript-uri
