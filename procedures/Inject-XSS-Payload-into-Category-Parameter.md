---
tags:
  - payload-injection
  - xss
  - url-encoding
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.407Z'
sub_techniques: []
id: b822301d-423d-45c1-bf83-500fbb21391a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Category-Parameter

## Summary

This procedure crafts and inserts a reflected XSS payload into the category parameter, exploiting the lack of sanitization to break out of a script tag and inject executable JavaScript.

## Description

The vulnerability stems from the category parameter being inserted into a <script> tag without HTML or JS escaping. The payload closes the script tag, injects an SVG element with an onload handler, and executes alert(document.domain) to prove execution. URL encoding ensures the payload survives transmission, targeting mobile browsers for client-side impacts like data exfiltration.

## Requirements

1. Loaded photos page URL
2. Knowledge of URL encoding
3. Browser or proxy for parameter modification

## Defense

Defensive measures and detection strategies:

- Escape user input in script contexts (e.g., replace < with &lt;)
- Use JSON encoding for dynamic script values
- Deploy Web Application Firewall (WAF) rules to block common XSS payloads

## Objectives

1. Break out of the reflected script context
2. Inject harmless proof-of-concept JavaScript
3. Encode payload for reliable delivery

## Instructions

### Step 1: Craft Raw Payload

**Context**: Design the payload to close the script and inject SVG.

Use: "--></script><svg/onload=';alert(document.domain);'>"

This closes the existing <script> tag, adds a new closing tag, and injects an SVG that executes on load.

### Step 2: URL Encode Payload

**Context**: Encode special characters for URL safety.

Convert to: %22--%3E%3C%2Fscript%3E%3Csvg%2Fonload%3D%27%3Balert%28document.domain%29%3B%27%3E

Append to the category parameter in the URL.

**Expected Output**: Encoded string ready for insertion, e.g., ?category=%22--%3E%3C%2Fscript%3E%3Csvg%2Fonload%3D%27%3Balert%28document.domain%29%3B%27%3E

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[payload-injection]]
- [[xss]]
