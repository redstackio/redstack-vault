---
tags:
  - xss
  - recon
  - web
  - bypass
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
updated_at: '2025-12-14T03:16:14.535Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 71427cc8-f683-43c0-8ceb-8a694bf90f08
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-Search-Parameter-for-XSS-Escaping-Issues

## Summary

This procedure tests the search functionality of a web application, such as Adobe eDex, for reflected XSS vulnerabilities by probing input escaping mechanisms, particularly focusing on how the system handles unencoded versus URL-encoded special characters like '='.

## Description

In the context of the Adobe eDex search endpoint (http://edex.adobe.com/search/global/), the system implements a basic filter that strips unencoded '=' characters from user input to mitigate XSS risks. However, it fails to decode or sanitize URL-encoded equivalents (%3D), allowing attackers to bypass this protection. This procedure involves accessing the endpoint with test payloads to observe reflection behavior, identifying the weakness that enables subsequent exploitation. Expected outcomes include confirmation of incomplete sanitization, setting the stage for payload injection in a real attack scenario targeting victim browsers.

## Requirements

1. Web browser with developer tools (e.g., Chrome Inspector) for viewing page source
2. Direct internet access to the target URL (http://edex.adobe.com/search/global/)
3. Basic understanding of URL encoding and XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation that decodes and sanitizes URL-encoded inputs before processing
- Use Content Security Policy (CSP) to restrict script execution
- Monitor server logs for suspicious search queries containing encoded characters like %3D

## Objectives

1. Verify if the search parameter reflects user input without proper escaping
2. Confirm the stripping of unencoded '=' while allowing %3D to pass through
3. Establish proof-of-concept for filter bypass

## Instructions

### Step 1: Access Search Endpoint and Test Unencoded Input

**Context**: Begin by submitting a basic payload with an unencoded '=' to check the default filtering behavior.

Navigate to http://edex.adobe.com/search/global/test=alert(1) in your browser. Inspect the page source (right-click > Inspect) to see if the '=' is stripped from the reflected output.

> The reflected search term should show 'testalert(1)' without the '=', confirming the strip.

### Step 2: Test URL-Encoded Equivalent

**Context**: Follow up by encoding the '=' as %3D to test if the filter handles decoding.

Navigate to http://edex.adobe.com/search/global/test%3Dalert(1). Inspect the page source again to observe if '%3D' remains unprocessed and reflected as-is.

> The output should reflect 'test=alert(1)' after decoding, indicating the bypass vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- web
- recon
