---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - injection
  - owasp
  - owasp top 10
  - Reflected XSS
  - Web Applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Bypass-Reflected-XSS-Filter-Using-Burp-Intruder

## Summary

This procedure demonstrates how to bypass web application filters that block most HTML tags and JavaScript event attributes in reflected XSS vulnerabilities by systematically testing allowed elements using Burp Suite's Intruder tool. It involves enumerating permitted tags and attributes to craft an executable payload that triggers an alert with document cookies, enabling session hijacking or further exploitation.

## Description

Reflected XSS occurs when user input is unsafely reflected back in the server's response, allowing injection of malicious scripts. Many applications implement partial filters to block common XSS vectors like <script> tags or onload events, but inconsistencies in filtering can be exploited. This technique uses Burp Intruder's payload positioning to brute-force HTML tags and attributes from an XSS evasion cheat sheet, identifying unblocked elements (e.g., <body> tag with onresize event). Once identified, a targeted payload is constructed to execute JavaScript in the browser context. This is effective against WAFs or custom sanitizers that whitelist specific tags/attributes. The procedure assumes a reflected XSS in a search parameter and requires proxying traffic through Burp Suite.

## Requirements

1. Burp Suite Professional or Community Edition installed and configured as a browser proxy.
2. Access to a vulnerable web application with a reflected input field (e.g., search box).
3. Browser configured to route traffic through Burp (e.g., Firefox with FoxyProxy).
4. Reference to an XSS filter evasion cheat sheet (e.g., OWASP XSS Filter Evasion Cheat Sheet for tags and events).
5. Basic knowledge of HTTP requests and Burp Suite navigation.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and output encoding using libraries like OWASP ESAPI or DOMPurify.
- Deploy Content Security Policy (CSP) headers to restrict inline scripts and unsafe attributes.
- Use Web Application Firewalls (WAFs) with machine learning-based anomaly detection for payload variations.
- Enable browser security features like XSS Auditor (deprecated in modern browsers) or strict CSP reporting.
- Monitor application logs for suspicious HTTP 400 responses or repeated Intruder-like requests from the same IP.

## Objectives

1. Identify the single allowed HTML tag and event attribute in a filtered reflected XSS context.
2. Craft and execute a functional XSS payload to steal document cookies via alert.
3. Demonstrate filter bypass without relying on blocked common vectors like <img onerror>.

## Instructions

### Step 1: Test Standard XSS Payload and Confirm Blocking

**Context**: Begin by injecting a common reflected XSS payload to verify the filter is active and blocks execution. This establishes the baseline for bypass attempts.

Navigate to the vulnerable search endpoint in your proxied browser (e.g., https://example.com/search?q=). Enter a standard payload like `<img src=1 onerror=alert(document.cookie)>` and submit. Intercept the request in Burp Suite's Proxy > HTTP history if needed.

**Expected Output**: The application reflects the input but no alert pops up; the response may show the payload stripped or sanitized, often with an error or HTTP 200 without execution.

### Step 2: Send Request to Burp Intruder for Tag Enumeration

**Context**: Use Burp Intruder to automate testing of HTML tags in the reflected parameter, identifying which ones are not blocked (e.g., resulting in HTTP 200 instead of 400).

Right-click the intercepted search request in Burp Proxy and select "Send to Intruder." In the Positions tab, clear default positions and set the search parameter value to `<§§>` (place cursor between < > and add two payload positions with §). Switch to the Payloads tab, load a list of HTML tags from an XSS cheat sheet (copy-paste all tags like body, iframe, etc.), set payload type to "Simple list," and start the attack.

**Expected Output**: Most payloads return HTTP 400 (blocked), but allowed tags like "body" return HTTP 200, indicating reflection without rejection.

### Step 3: Enumerate Allowed Attributes/Events for the Permitted Tag

**Context**: With the allowed tag identified (e.g., <body>), test event attributes to find executable JavaScript handlers like onresize, which can trigger code without common blocks.

Return to the Intruder Positions tab, update the search parameter to `<body%20§>` (URL-encode space as %20, add one payload position after). In Payloads, load a list of JavaScript event attributes from the XSS cheat sheet (e.g., onresize, onload, onerror). Restart the attack.

**Expected Output**: Blocked events return HTTP 400; allowed ones like "onresize" return HTTP 200, confirming the attribute is reflected.

### Step 4: Craft and Execute the Bypass Payload

**Context**: Combine the allowed tag and attribute into a full XSS payload to execute JavaScript. Use the code snippet [[codes/Body-Tag-Onresize-XSS-Payload]] for the exact structure, substituting the lab URL or target.

Construct the URL: `https://target.com/search?q=""><body onresize=alert(document.cookie)>` (close any quotes in the reflected context). Load this in the browser to trigger the alert.

Include the payload code block here for reference:

```html
<body onresize=alert(document.cookie)>
```

**Expected Output**: An alert dialog displays the document's cookies, confirming successful XSS execution and potential session theft.

### Step 5: Verify and Iterate if Needed

**Context**: Confirm the payload works across variations and test for further exploitation (e.g., replacing alert with data exfiltration).

Submit the payload multiple times, observing network traffic in Burp for any additional blocks. If onresize fails in production, repeat Steps 2-3 with other discovered tags/attributes.

**Expected Output**: Consistent alert execution without blocks; cookies visible for hijacking.
