---
id: proc-002
name: Test-Input-Reflection-in-Search
tags:
  - xss
  - reflection-test
  - web
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-reflection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:16:20.116Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Test-Input-Reflection-in-Search

## Summary

This procedure tests whether user input in the search parameter is reflected back into the page source, specifically in inline JavaScript, without sanitization, indicating a potential XSS vulnerability.

## Description

By submitting a harmless search term like 'chron0x' to /search/node/chron0x, the response is inspected for direct insertion into JavaScript variables, such as var internalPath = 'search/node/chron0x';. This reflection without encoding suggests the input can be manipulated to inject code.

## Requirements

1. Identified search endpoint from prior recon
2. Browser or curl for requests
3. Ability to view page source

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs before insertion into scripts
- Encode dynamic content in JavaScript contexts
- Monitor for anomalous search queries in logs

## Objectives

1. Confirm input reflection
2. Locate exact insertion point
3. Assess sanitization level

## Instructions

### Step 1: Submit Benign Search

**Context**: Perform a search to observe reflection.

Use [[commands/curl-test-reflection]]:

```bash
curl -X GET "https://target.com/search/node/chron0x" | grep internalPath
```

> Expected output: var internalPath ='search/node/chron0x'; in the response.

### Step 2: Inspect Page Source

**Context**: Manually view the full page to confirm context.

Load the URL in a browser and view source (Ctrl+U).

> Look for unescaped user input in <script> tags.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-reflection]]

## Tools Used

- [[tools/curl]]

## Tags

- [[xss]]
- [[web]]
