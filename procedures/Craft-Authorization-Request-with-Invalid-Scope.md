---
id: uuid-craft-oauth-request
tags:
  - oauth
  - url-crafting
  - invalid-scope
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:26.390Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Craft-Authorization-Request-with-Invalid-Scope

## Summary

This procedure constructs a malicious OAuth authorization request URL that includes an invalid scope parameter to trigger an error response, exploiting the open redirect to the client-specified URI.

## Description

Per RFC6749 section 4.1.2.1, authorization servers must redirect to the provided redirect_uri on errors like invalid_request (e.g., unknown scope) without user interaction. Using the registered client_id, craft a GET request to the /authorize endpoint with response_type=code, valid client_id, invalid scope (e.g., WRONG_SCOPE), and attacker redirect_uri. This targets web-based OAuth servers. Expected outcome: A URL that, when accessed, causes automatic redirect.

## Requirements

1. Valid client_id from prior registration
2. Knowledge of the /authorize endpoint URL (e.g., http://victim.com/authorize)
3. Attacker-controlled redirect_uri

## Defense

Defensive measures and detection strategies:

- Reject or validate redirect_uris in requests against registered values
- Return error pages instead of redirects for validation errors
- Log and alert on requests with invalid scopes from suspicious URIs

## Objectives

1. Build a URL that fails validation due to invalid scope
2. Include attacker redirect_uri to hijack the error flow
3. Prepare URL for distribution to victims

## Instructions

### Step 1: Assemble URL Parameters

**Context**: Combine OAuth parameters into a query string for the /authorize endpoint.

Construct the URL manually:

Base: http://victim.com/authorize

Parameters:
- response_type=code
- client_id=bc88FitX1298KPj2WS259BBMa9_KCfL3
- scope=WRONG_SCOPE
- redirect_uri=http://attacker.com

Full URL example: http://victim.com/authorize?response_type=code&client_id=bc88FitX1298KPj2WS259BBMa9_KCfL3&scope=WRONG_SCOPE&redirect_uri=http://attacker.com

> Expected output: Validly formatted OAuth request URL.

### Step 2: Validate URL Structure

**Context**: Ensure the URL adheres to OAuth syntax to avoid early rejection.

Test the URL in a browser or tool without submitting; check for parameter encoding issues.

> Expected output: No syntax errors; parameters parse correctly.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[oauth]]
- [[url-crafting]]
- [[invalid-scope]]
