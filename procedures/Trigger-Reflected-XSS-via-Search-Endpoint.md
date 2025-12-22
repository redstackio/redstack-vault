---
tags:
  - xss
  - reflected-xss
  - search-endpoint
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-udemy-autocomplete-search]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 22d67d03-7569-48fd-8ca6-40787b455e87
created_at: '2025-12-14T03:15:27.003Z'
updated_at: '2025-12-14T03:15:27.003Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Reflected-XSS-via-Search-Endpoint

## Summary

This procedure triggers the reflected XSS by querying Udemy's autocomplete search endpoint with a term that matches the injected payload, causing JavaScript execution in the response context.

## Description

After injecting the payload into the firstname, this step accesses the /autocomplete/search/ endpoint with the term parameter set to a value that searches for the malicious username. The endpoint reflects unsanitized user data in its JSON response, allowing the payload to execute as HTML/JS in the browser. Impacts include session hijacking or data theft. This targets public users viewing search results and can be done anonymously.

## Requirements

1. Injected payload in a user profile (from prior procedure)
2. Access to Udemy's search functionality
3. Tool like curl or browser for HTTP requests

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in API responses, especially JSON
- Implement strict output encoding (e.g., JSON.stringify for strings)
- Rate-limit search queries and log anomalous terms

## Objectives

1. Reflect the injected payload in search response
2. Execute arbitrary JavaScript in victim browser
3. Achieve client-side compromise like cookie theft

## Instructions

### Step 1: Prepare Search Term

**Context**: Identify or craft a search term that will match the injected username containing the payload.

Use the username or partial match to trigger inclusion in results.

### Step 2: Send Request to Endpoint

**Context**: Issue an HTTP GET to the autocomplete endpoint with the encoded term parameter.

**Command** ([[commands/curl-udemy-autocomplete-search]]):
```bash
curl "https://www.udemy.com/autocomplete/search/?cl=EyNkHjsRED4T&displayType=json&cf=ExRONTsRED5COkUCGxAHKV8HaTMPDBFu&count=4&term=%22%3E%3Cimg+src%3D%3E"
```

> The response JSON includes the reflected payload, parsed as HTML in the browser, executing the script (e.g., broken img tag triggers error or onload JS).

### Step 3: Verify Execution

**Context**: Observe the response in a browser to confirm XSS fires.

Load the URL in a browser viewing search results; check console for execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-udemy-autocomplete-search]]

## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[endpoint-exploitation]]
