---
id: 14c670f1-36d3-4323-9358-e230354ebf15
name: Mutated-XSS-with-Relative-Path-Overwrite
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:43.916452+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - mutated-xss
  - ie8-ie9
  - relative-path-overwrite
  - xss
commands: []
platforms:
  - Web
  - Browser
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Mutated-XSS-with-Relative-Path-Overwrite

## Summary

Mutated XSS with Relative Path Overwrite is a client-side execution technique that exploits vulnerabilities in the Listing ID parameter of a web application, specifically targeting Internet Explorer 8 and 9. By injecting a mutated JavaScript payload that leverages relative path manipulation and encoding to bypass input validation and XSS filters, an attacker can execute arbitrary code in the victim's browser context, enabling session hijacking, data theft, or further exploitation.

## Description

This procedure targets legacy browsers like IE8 and IE9 where certain HTML parsing quirks allow for relative path overwrites combined with mutated payloads to evade traditional XSS defenses. The attack manipulates the URL path to inject a script that alters the DOM, specifically using a custom <listing> tag to store encoded malicious content, which is then retrieved and executed via JavaScript. This bypasses output encoding by exploiting how IE handles innerHTML and script evaluation in vulnerable parameters. In a real-world scenario, this could occur in search or listing features of e-commerce or directory applications where user input is reflected without proper sanitization. Success leads to arbitrary JavaScript execution, allowing attackers to steal cookies, keystrokes, or redirect users. Prerequisites include identifying reflector points in the Listing ID parameter through manual testing or automated scanning.

## Requirements

1. Access to a vulnerable web application with a reflector in the Listing ID parameter (e.g., via direct URL manipulation or form submission).
2. Knowledge of the specific vulnerability in the Listing ID handling, confirmed through testing for XSS reflections.
3. Internet Explorer 8 or 9 installed on the testing or target machine, as the technique relies on legacy parsing behaviors.
4. Basic web proxy tool (optional, for intercepting and modifying requests) to craft and test payloads.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding) on all user-controlled parameters like Listing ID.
- Deploy a Content Security Policy (CSP) to restrict inline script execution and external resource loading.
- Regularly update and patch web applications to address known XSS vulnerabilities, and avoid supporting legacy browsers like IE8/9.
- Monitor for anomalous JavaScript execution via client-side logging or Web Application Firewalls (WAFs) that detect encoded payloads and DOM manipulations.

## Objectives

1. Inject and execute malicious JavaScript code on a vulnerable web application to demonstrate XSS.
2. Gain unauthorized access to sensitive information, such as session cookies or user data.
3. Take control of user sessions to perform actions on behalf of the victim.

## Instructions

### Step 1: Identify the Vulnerable Parameter

**Context**: Locate the Listing ID parameter in the web application, typically in URLs or forms for listing or search functionality, and confirm it reflects user input without sanitization.

Navigate to the application's listing or search page and append or submit a test string like "test" to the Listing ID parameter. Observe if it appears unencoded in the response HTML.

> If the input is reflected as-is (e.g., <div>Listing ID: test</div>), proceed; otherwise, test variations to confirm vulnerability.

### Step 2: Craft the Mutated Payload

**Context**: Prepare the payload using encoding and relative path overwrite to bypass filters. This step uses a pre-defined code snippet that exploits IE's handling of custom tags and innerHTML.

Reference the payload code [[codes/IE8-Mutated-XSS-Relative-Path-Overwrite-Payload]] and customize if needed (though it's static for this technique).

The payload structure:
- Uses a <listing> tag to hold an encoded <img> with onerror handler.
- Follows with a <script> that retrieves and alerts the content, triggering execution.

### Step 3: Inject the Payload

**Context**: Submit the crafted payload into the Listing ID parameter to trigger reflection and execution in the browser.

Construct the request, e.g., via URL: https://vulnerable-app.com/listing?id=<listing id=x>&lt;img src=1 onerror=alert(1)&gt;</listing><script>alert(document.getElementById('x').innerHTML)</script>

Load the page in IE8 or IE9. The relative path overwrite ensures the script executes in the page context.

> Use browser developer tools (F12 in IE) to inspect the DOM for confirmation of injection.

### Step 4: Verify Execution

**Context**: Confirm the payload executes by observing the alert or any side effects, such as data exfiltration to an attacker-controlled endpoint.

Upon successful load, an alert box should appear displaying the injected content. For real attacks, replace alert(1) with data-stealing code like document.cookie.

> If no execution occurs, check for WAF blocks or adjust encoding to evade filters.
