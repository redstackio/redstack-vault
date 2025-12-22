---
tags:
  - recon
  - xss
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-fetch-urbandictionary]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:15:52.800Z'
sub_techniques: []
id: a078efe1-8879-4d46-93bb-032a6b2a3ac5
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Urban Dictionary Search Endpoint

## Summary

This procedure identifies the vulnerable search endpoint in Urban Dictionary by accessing the define page and inspecting for reflection of the 'term' parameter in the page source, confirming potential for Reflective XSS.

## Description

In the attack scenario, attackers manually navigate to the /define.php endpoint with a test term and use browser developer tools to examine the HTML source. The 'term' input is reflected into a JavaScript object (Page.globals.normalized) inside a <script> tag without sanitization, setting the stage for XSS exploitation. This step requires only public web access and is typically performed in a reconnaissance phase targeting public-facing web applications.

## Requirements

1. Web browser with developer tools enabled
2. Internet access to www.urbandictionary.com
3. Basic knowledge of HTML/JS inspection

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict inline scripts
- Sanitize and escape user inputs before insertion into JS contexts
- Monitor for anomalous search queries with script tags in logs

## Objectives

1. Confirm reflection of user input in script context
2. Identify lack of escaping for XSS potential
3. Gather baseline for payload crafting

## Instructions

### Step 1: Access the Endpoint

**Context**: Navigate to the search page to trigger reflection.

**Command** ([[commands/curl-fetch-urbandictionary]]):
```bash
curl "http://www.urbandictionary.com/define.php?term=test" | grep -i "normalized"
```

> This fetches the page and searches for the reflected 'normalized' property. Expected output shows "normalized": "test" in script tag.

### Step 2: Inspect Source

**Context**: Manually view source in browser for detailed analysis.

No command needed; right-click > View Page Source and search for 'Page.globals'.

> Look for unsanitized input within double quotes.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-urbandictionary]]

## Tools Used


## Tags

- [[recon]]
- [[xss]]
