---
tags:
  - xss
  - reflection-test
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
updated_at: '2025-12-14T00:11:15.887Z'
sub_techniques: []
id: 9022a1a2-2c5d-48d7-8c88-ace4129de8dc
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Test-Input-Reflection-in-Equifax-Search-Query

## Summary

This procedure tests whether user input in the 'q' parameter of the Equifax search endpoint is reflected back in the response without sanitization, laying the groundwork for XSS exploitation.

## Description

In a web-based attack scenario targeting public-facing search functionality, this step involves submitting a harmless test string to observe if it echoes back into the page content. The target is the Equifax personal search at https://www.equifax.com/personal/search. Successful reflection indicates a potential injection point for malicious payloads, leading to client-side JavaScript execution. Prerequisites include a standard web browser and internet access; no authentication is required.

## Requirements

1. Web browser with developer tools
2. Public access to the target URL
3. Basic understanding of URL parameters

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding for all user inputs in JavaScript contexts
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for unusual search query patterns in server logs

## Objectives

1. Confirm if the 'q' parameter is reflected unsanitized
2. Identify the exact location of reflection for payload crafting
3. Establish proof-of-concept for further exploitation

## Instructions

### Step 1: Navigate to Search Endpoint

**Context**: Access the vulnerable search page and append a test input to the query parameter to simulate user search behavior.

**Instructions**: Open your web browser and enter the following URL in the address bar:

https://www.equifax.com/personal/search?q=broook

> This submits 'broook' as the search term. The page should load search results without errors, indicating the input was processed.

### Step 2: Observe Initial Response

**Context**: Verify that the page renders normally, suggesting the input was accepted and potentially reflected.

**Instructions**: Load the page and note any search results or messages containing 'broook'.

> Expected: The term appears in visible content or metadata, confirming server-side processing without immediate rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web-vulnerability]]
