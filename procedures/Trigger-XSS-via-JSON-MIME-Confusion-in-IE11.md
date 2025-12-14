---
id: proc-trigger-mapbox-xss-ie11
tags:
  - xss
  - mime-confusion
  - ie11
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-get-styles-trigger]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.319Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-JSON-MIME-Confusion-in-IE11

## Summary

This procedure triggers the stored XSS payload by retrieving the affected Mapbox style in Internet Explorer 11, exploiting the absence of the X-Content-Type-Options: nosniff header to cause the browser to misinterpret the JSON response as HTML, leading to script execution.

## Description

The Mapbox Styles API returns style data in JSON format without the X-Content-Type-Options: nosniff header. In IE11, this allows MIME sniffing, where the browser treats the response as HTML if it contains HTML-like content (e.g., the injected <script> tag). When a victim accesses the style URL, the payload executes in their browser context, potentially hijacking sessions or stealing data. Modern browsers do not exhibit this behavior due to stricter MIME handling.

## Requirements

1. Access to the affected style URL
2. Internet Explorer 11 environment for testing or victim simulation
3. Network access to api.mapbox.com

## Defense

Defensive measures and detection strategies:

- Set X-Content-Type-Options: nosniff on all JSON API responses to prevent MIME sniffing
- Deprecate support for legacy browsers like IE11
- Use strict CSP headers to block unauthorized script execution
- Log and alert on anomalous browser user agents accessing styles

## Objectives

1. Cause IE11 to execute the stored JavaScript payload
2. Demonstrate client-side impact like data exfiltration
3. Highlight legacy browser vulnerabilities in API design

## Instructions

### Step 1: Simulate Victim Access

**Context**: Direct a browser request to the style retrieval endpoint using an IE11 user agent to mimic the victim.

**Command** ([[commands/curl-get-styles-trigger]]):
```bash
curl -X GET "https://api.mapbox.com/styles/v1/{username}/{style_id}?access_token={your_token}" \
  -H "User-Agent: Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 10.0; Trident/7.0)"
```

> This fetches the JSON response. In a real IE11 browser, open the URL directly; the lack of nosniff header triggers HTML parsing and script execution.

### Step 2: Observe Execution

**Context**: In IE11, the response is rendered as HTML, executing the script (e.g., alert or beacon).

No command; monitor browser console or network tab for execution indicators like outgoing requests to attacker domains.

### Step 3: Validate Impact

**Context**: Confirm no execution in non-vulnerable browsers for comparison.

**Command** ([[commands/curl-get-styles-modern]]):
```bash
curl -X GET "https://api.mapbox.com/styles/v1/{username}/{style_id}?access_token={your_token}" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

> Modern browsers treat it as JSON without execution, verifying the IE11-specific issue.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-get-styles-trigger]]
- [[commands/curl-get-styles-modern]]

## Tools Used


## Tags

- [[xss]]
- [[ie11]]
- [[mime-confusion]]
