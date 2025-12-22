---
type: procedure
description: >-
  Bypass web application XSS filters that block common tags by leveraging
  allowed SVG elements and events to execute JavaScript.
verified: true
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - injection
  - owasp
  - owasp top 10
  - reflected-xss
  - web-applications
commands:
  - '[[commands/curl-test-reflected-search-payload]]'
tools:
  - '[[tools/Burp-Suite]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Bypass-Reflected-XSS-Filter-Using-SVG-Discard-Tag

## Summary

This procedure outlines how to identify and exploit a reflected XSS vulnerability in a web application where common XSS tags like <img> with onerror are blocked, but certain SVG elements and attributes are permitted. By using Burp Suite's Intruder to fuzz allowed tags and attributes, an attacker can craft a payload utilizing the <svg><discard> element with the onbegin event to execute arbitrary JavaScript, such as alert(1), demonstrating code execution.

## Description

Reflected XSS occurs when user input is immediately reflected back in the server's response without proper sanitization, allowing injection of malicious scripts. In this scenario, the application filters out standard XSS vectors but permits some SVG markup, which can be abused due to SVG's support for event handlers like onbegin. The technique involves systematically testing tags and attributes to find unfiltered ones, then combining them into a functional payload. This is commonly seen in search parameters or query strings on web applications. The target environment is a web app with a reflected input field, such as a search box, running over HTTP/HTTPS. Success results in JavaScript execution in the victim's browser, potentially leading to session hijacking, data theft, or further exploitation.

## Requirements

1. Network access to the vulnerable web application (e.g., via browser or proxy).
2. Burp Suite Professional or Community Edition installed and configured as a proxy.
3. A list of XSS payloads, such as from the PortSwigger XSS Cheat Sheet (manually curated for tags and attributes).
4. Basic knowledge of HTTP requests, URL encoding, and browser developer tools.
5. The application must reflect user input in the response (e.g., in error messages or search results).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding) for all user inputs, specifically targeting SVG namespaces.
- Deploy Content Security Policy (CSP) headers to restrict script execution, including inline scripts and event handlers (e.g., script-src 'self').
- Use Web Application Firewalls (WAFs) with rules to detect and block SVG-based payloads and unusual event attributes.
- Sanitize SVG inputs by disallowing or parsing event handlers and scriptable elements; libraries like DOMPurify can help.
- Monitor application logs for HTTP 400 responses on fuzzing attempts and anomalous JavaScript execution in client-side logs.

## Objectives

1. Identify blocked versus allowed HTML/SVG tags and attributes in the reflected input.
2. Craft and deliver a functional XSS payload using permitted SVG elements to execute JavaScript.
3. Verify successful code execution via browser alert or console output.
4. Demonstrate the bypass in a controlled environment to assess impact.

## Instructions

### Step 1: Test Basic XSS Payload to Confirm Filtering

**Context**: Begin by submitting a standard XSS payload to verify that common vectors are blocked, typically resulting in a 400 Bad Request response. This establishes the baseline filter behavior.

Use [[commands/curl-test-reflected-search-payload]] to send the request:

```bash
curl -X GET "http://$_TARGET_URL/?search=<img%20src=1%20onerror=alert(1)>" -v
```

> This command sends a URL-encoded basic <img> payload to the search parameter. The -v flag provides verbose output to inspect response headers and status. Expect a 400 status if filtered.

### Step 2: Intercept Request and Configure Burp Intruder for Tag Fuzzing

**Context**: Switch to an interactive proxy setup to fuzz multiple payloads efficiently. Intercept the search request in Burp Suite and send it to Intruder to test various tags against the filter.

Configure Burp Suite ([[tools/Burp-Suite]]) as follows:
1. Set your browser to proxy through Burp (default: 127.0.0.1:8080).
2. Submit a search query (e.g., any term) and intercept the GET/POST request in Burp Proxy.
3. Right-click the intercepted request and select "Send to Intruder."
4. In the Intruder Positions tab, clear all positions and highlight the search parameter value (e.g., §search_term§), then click "Add §" to mark it as the payload position.

> No specific command here; this is GUI-based. Ensure Burp is running and proxying traffic.

### Step 3: Load and Test XSS Tags in Intruder

**Context**: Populate Intruder with a list of potential XSS tags to identify which ones are allowed (200 OK) versus blocked (400). Use a curated list from an XSS cheat sheet, focusing on SVG-related tags.

In Burp Intruder Payloads tab:
1. Manually add or paste a list of tags (e.g., <svg>, <discard>, <img>, <script>, etc.) into the payload list. Avoid external clipboard copies for reproducibility; example payloads: <svg>, <discard>, <animate>.
2. Set payload type to "Simple list."
3. Click "Start attack" and review the response table.

Observe lengths, status codes, and rendered responses. SVG <discard> should return 200, indicating it's allowed.

> Filter responses by status code in Burp to quickly spot allowed tags.

### Step 4: Fuzz Attributes for Allowed Tags

**Context**: Once an allowed tag like <discard> is identified, test its attributes to find executable event handlers, such as onbegin, which can trigger JavaScript.

Return to Intruder:
1. Update the base request with <svg><discard $_ATTRIBUTE=1></svg> in the search parameter, marking $_ATTRIBUTE as the position.
2. Load a list of event attributes (e.g., onload, onerror, onbegin, onclick) into payloads.
3. Start the attack and inspect responses.

The onbegin attribute should return 200, while others are blocked.

> Use Burp's response viewer to check if the attribute is reflected without filtering.

### Step 5: Craft and Test the Full Bypass Payload

**Context**: Combine the allowed tag and attribute into a complete payload that closes any preceding attributes and injects executable JS. URL-encode for transmission.

Use [[commands/curl-test-reflected-search-payload]] to test the crafted payload:

```bash
curl -X GET "http://$_TARGET_URL/?search=%22%3E%3Csvg%3E%3Cdiscard%20onbegin=alert(1)%3E" -v
```

> This sends the encoded payload "><svg><discard onbegin=alert(1)>. Expect 200 OK with the payload reflected. To verify JS execution, load the same URL in a browser: http://target/?search="><svg><discard onbegin=alert(1)>. An alert box should pop up if successful.

For the payload itself, reference [[codes/SVG-Discard-Onbegin-XSS-Payload]].
