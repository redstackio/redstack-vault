---
tags:
  - xss
  - payload-craft
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
updated_at: '2025-12-14T00:11:15.865Z'
sub_techniques: []
id: b7cee38f-a5ad-494f-8974-abfaed210ec4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Craft-XSS-Payload-for-JavaScript-Injection

## Summary

This procedure constructs a URL-encoded JavaScript payload that exploits the reflected input in the JS object to execute arbitrary code, such as an alert.

## Description

Targeted at the Equifax vulnerability, the payload breaks out of the string by closing quotes, injecting a new property with an array, and using .map to execute code. Encoding ensures URL compatibility. This step transitions from reconnaissance to exploitation in XSS attacks, resulting in a deliverable malicious link. Requires URL encoding knowledge; tested in browser.

## Requirements

1. Text editor or online URL encoder
2. Understanding of JS injection techniques
3. Confirmed reflection context

## Defense

Defensive measures and detection strategies:

- Validate and escape all dynamic JS properties
- Use parameterized JS templates
- Log and block encoded payloads in WAF rules

## Objectives

1. Create a syntactically correct injection payload
2. Encode for URL transmission
3. Ensure execution of proof-of-concept code like alert

## Instructions

### Step 1: Design Raw Payload

**Context**: Build JS to close the string and inject executable code.

**Instructions**: Start with the reflected string and append: " , internalSearchTerm: ["broook"].map(alert) , numOfSearchResultsReturned: "b

> This creates an array and maps alert over it, executing on load.

### Step 2: URL Encode Payload

**Context**: Convert special characters to evade URL parsing issues.

**Instructions**: Encode the payload to: %22%20%2C%20internalSearchTerm%3A%20%5B%22broook%22%5D.map%28alert%29%20%2C%20numOfSearchResultsReturned%3A%20%22b

> Use an online encoder or browser console (encodeURIComponent).

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
- [[payload]]
