---
id: proc-001
name: Test-Reflected-XSS-with-HTML-Injection
tags:
  - xss
  - reflected-xss
  - html-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-html-injection-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:50.048Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Reflected-XSS-with-HTML-Injection

## Summary

This procedure tests for reflected XSS vulnerabilities by injecting HTML tags into a web application's search parameter, confirming if user input is reflected without sanitization. In the Panther.com case, it verifies that the search endpoint renders injected HTML, setting the stage for more advanced exploitation.

## Description

The attack targets public-facing web search functionalities where user input in URL parameters is directly echoed back into the HTML response without proper escaping. By navigating to the endpoint with benign HTML tags (e.g., <h1> and <font>), an attacker can observe if the browser interprets and renders the tags. This is a low-risk initial probe that reveals sanitization weaknesses. Prerequisites include browser access to the site; no authentication is needed. Expected outcomes include visible HTML rendering, indicating vulnerability to further payloads.

## Requirements

1. Web browser with developer tools for inspecting rendered HTML
2. Direct internet access to the target site (panther.com/search)
3. Optional: Command-line tool like curl for scripted testing

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding (e.g., using HTML entity encoding) on all user inputs reflected in responses
- Deploy Content Security Policy (CSP) headers to restrict inline HTML and script execution
- Monitor for anomalous search queries containing HTML tags via WAF logs or SIEM

## Objectives

1. Confirm reflection of unsanitized HTML in the browser
2. Identify the exact parameter vulnerable to injection
3. Establish proof-of-concept for escalation to JavaScript execution

## Instructions

### Step 1: Craft and Navigate to Test URL

**Context**: Prepare a URL with encoded HTML tags in the search parameter to test for reflection without triggering obvious filters.

**Command** ([[commands/curl-html-injection-test]]):
```bash
curl -s "https://panther.com/search/Users%3Ch1%3EHello,%20I%20am%3C/h1%3E%3Cfont%20color=red%3E%20Ibrahimatix0x01%3C/font%3E" | grep -i "h1"
```

> This curl command fetches the page and greps for the <h1> tag to confirm presence in the response. Expected output includes the raw HTML with tags unescaped. Then, paste the URL into a browser to view rendering.

### Step 2: Verify Rendering in Browser

**Context**: Load the URL in a browser to check if the HTML executes as intended.

No specific command; manually visit https://panther.com/search/Users%3Ch1%3EHello,%20I%20am%3C/h1%3E%3Cfont%20color=red%3E%20Ibrahimatix0x01%3C/font%3E.

> Observe the page source or DOM inspector; successful execution shows a styled heading and red text, confirming the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-html-injection-test]]

## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[html-injection]]
